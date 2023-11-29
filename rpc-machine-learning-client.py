#import package sebagai client
import xmlrpc.client

#membuat proxy RPC ke server
proxy = xmlrpc.client.ServerProxy("http://192.168.56.1:5000/")

#looping untuk input 
while (True) :
    print('tuliskan exit Untuk Keluar')
    path = input("Masukkan Path Gambar : ")
    if path == 'exit':
        break
    #Memanggil fungsi dari server 
    hasil = proxy.rpsClassification(path)
    #Menampilkan hasil 
    print(f"Hasil Prediksi adalah {hasil}")
    
   


