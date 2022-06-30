from io import BytesIO
import io
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote, urlparse, parse_qs
from base64 import b64encode as enc64
from base64 import b64decode as dec64
import sqlite3
from PIL import Image
import base64 
import qrcode

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        import models 
        import views.client as client_view

        #self.send_response(200)
        #self.send_header('Content-Type', 'text/html, charset="utf-8"')
        #self.end_headers()


        if ("clients/" in self.path):

            import views.clients as clients_view
            
            try:
                client_id = int(self.path.split('/')[-1]) # ['', 'clients', :id]
                print(client_id)

                sqlite_connection = sqlite3.connect('./database/database.db')
                cursor = sqlite_connection.cursor()
                print("Successfully Connected to SQLite")

                cursor.execute("SELECT * FROM Clients WHERE id=?", (client_id,))
                client = cursor.fetchall()
                print(client)
                cursor.close()

                result = clients_view.render_client(client)
                result = bytes(result, 'utf-8')
                #img = qrcode.make("http://localhost:8000/clients/{}".format(client_id))

                data_qr = "http://localhost:8000/clients/{}".format(client_id)
                image = qrcode.make(data_qr)
                image.save("image.jpg")
                #qr = qrcode.QRCode(
                #    version=1,
                #    error_correction=qrcode.constants.ERROR_CORRECT_L,
                #    box_size=10,
                #    border=4,
                #)
                #qr.add_data(data_qr)
                #qr.make(fit=True)

                #img = qr.make_image(fill_color="black", back_color="white")  

                #def image_to_byte_array(image: Image) -> bytes:
                #    imgByteArr = io.BytesIO()
                #    image.save(imgByteArr, format=image.format)
                #    imgByteArr = imgByteArr.getvalue()
                #    return imgByteArr    

                def binary_pict(pict):
                    with open(pict, "rb") as f:
                        binary = enc64(f.read())
                    return binary

                def export_image(binary):
                    photo = BytesIO(dec64(binary))
                    pillow = Image.open(photo)
                    x = pillow.show()      

                self.send_response(200)
                self.send_header('Content-Type', 'text/html, charset="utf-8"')
                self.end_headers()
                self.wfile.write(result)
                self.wfile.write(bytes(export_image(binary_pict("image.jpg")), "utf-8"))  #bytes(f, "utf-8"), image_to_byte_array(img), Image.open("image.jpg")
                

            except sqlite3.Error as err:
                print(err)
                cursor.close()
                self.send_response(500)
                
            except ValueError as err:
                self.send_response(400)
                self.wfile.write(bytes('Error!\n', 'utf-8'))
                self.wfile.write(bytes('Invalid `id` format', 'utf-8'))


        elif ("clients" in self.path): # localhost:8000/clients

            import views.clients as clients_view

            try:
                sqlite_connection = sqlite3.connect('./database/database.db')
                cursor = sqlite_connection.cursor()
                print("Successfully Connected to SQLite")

                cursor.execute("SELECT * FROM Clients")
                clients = cursor.fetchall()
                cursor.close()

                result = clients_view.render_client(clients)
                result = bytes(result, 'utf-8')

                self.send_response(200)
                self.send_header('Content-Type', 'text/html, charset="utf-8"')
                self.end_headers()
                self.wfile.write(result)

            except sqlite3.Error as err:
                print(err)
                cursor.close()
        
            finally:
                if (sqlite_connection):
                    sqlite_connection.close()

        else: # localhost:8080....

            self.send_response(200)
            self.send_header('Content-Type', 'text/html, charset="utf-8"')
            self.end_headers()
    
            c = models.client.Client('Игорь', 'Войтенко', 'voytenko_igor@gmail.com', 423450) 
            result = client_view.render_client(c)
            result = bytes(result, 'utf-8')
            self.wfile.write(result)

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()

        # Парсим в словарь
        parsed_body = parse_qs(unquote(body.decode('utf-8')))
        print(parsed_body)
        # Индекс сохраняется как строка -> нужно преобрзовать
        parsed_body["index"][0] = int(parsed_body["index"][0])

        # Сохраняем в БД
        try:
            sqlite_connection = sqlite3.connect('./database/database.db')
            cursor = sqlite_connection.cursor()
            print("Successfully Connected to SQLite")

            sql = """
                INSERT INTO 
                Clients(`firstname`, `lastname`, `email`, `index`)
                VALUES (?, ?, ?, ?)
            """

            cursor.execute(sql, (parsed_body["firstname"][0], parsed_body["lastname"][0], parsed_body["email"][0],
                parsed_body["index"][0]))
            sqlite_connection.commit()
            print("INSERTED")
            cursor.close()

        except sqlite3.Error as err:
            print(err)
            cursor.close()
        
        finally:
            if (sqlite_connection):
                sqlite_connection.close()

        # Отправляем ОК
        self.wfile.write("OK".encode('utf-8'))



httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()