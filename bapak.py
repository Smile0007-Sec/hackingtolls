#! / usr / bin / env python
'' '
GTP Utama
Dibuat pada 18 Juni 2018
@ penulis: loay
'' '
impor  os
 waktu impor
impor  sys
impor  gtp . info
impor  gtp . penipuan
import  sigploit


dari  gtp . gtp_v2_core . utilitas . configuration_parser  import  parseConfigs

config_file =  ''
remote_net  = ''
mendengarkan  =  Benar
verbositas  =  2
output_file  = 'results.csv'

def  gtpinfo ():
    os . sistem ( 'bersih' )
    print  " \ 033 [31mInformation Gathering \ 033 [0m" . tengah ( 105 , "#" )
    print  " \ 033 [34mPilih Serangan dari bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    cetak  "Serangan" . rjust ( 10 ) +  " \ t \ t \ t \ t Deskripsi"
    cetak  "-------- ------------"
    cetak  "0) GTP Nodes Discovery" . rjust ( 25 ) +  " \ t \ t NE Discovery, menggunakan: EchoRequest, CreateSession, DeleteSession atau DeleteBearer Messages"
    cetak  "1) TEID Allocation Discovery" . rjust ( 31 ) +  " \ t \ t TEID Discovery, menggunakan: CreateSession, ModifyBearer atau CreateBearer Messages"

    mencetak
    print  "atau ketik kembali untuk kembali ke Menu Serangan" . rjust ( 42 )

    choice  =  raw_input ( " \ 033 [37m ( \ 033 [0m \ 033 [2; 31minfo \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        gtp . info . nediscover ()
     pilihan  elif ==  "1" :
        gtp . info . teidiscover ()
    elif  pilihan  ==  "kembali" :
  		gtpattacksv2 ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0-1)'
        waktu . tidur ( 1,5 )
        gtpinfo ()

def  gtpfraud ():
    os . sistem ( 'bersih' )
    cetak  " \ 033 [31mFraud \ 033 [0m" . tengah ( 105 , "#" )
    print  " \ 033 [34mPilih Serangan dari bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    cetak  "Serangan" . rjust ( 10 ) +  " \ t \ t \ t \ t Deskripsi"
    cetak  "-------- ------------"
    cetak  "0) Tunnel Hijack" . rjust ( 19 ) +  " \ t \ t TEID Hijack, menggunakan: ModifyBearerRequest Message, TunnelHijack.cnf"

    mencetak
    print  "atau ketik kembali untuk kembali ke Menu Serangan" . rjust ( 42 )

    choice  =  raw_input ( " \ 033 [37m ( \ 033 [0m \ 033 [2; 31minfo \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        gtp . penipuan . thijack ()
    elif  pilihan  ==  "kembali" :
        gtpattacksv2 ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0)'
        waktu . tidur ( 1,5 )
        gtpfraud ()



def  gtpattacksv2 ():
    os . sistem ( 'bersih' )

    print  " \ 033 [34mPilih Dari Kategori Serangan Di Bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    print  "0) Pengumpulan Informasi" . rjust ( 27 )
    cetak  "1) Penipuan" . rjust ( 11 )
    mencetak
    print  "atau ketik kembali untuk kembali ke menu utama" . rjust ( 42 )
    mencetak

    choice  =  raw_input (
        " \ 033 [37m ( \ 033 [0m \ 033 [2; 31mattacks \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        gtpinfo ()
     pilihan  elif ==  "1" :
        gtpfraud ()
    elif  pilihan  ==  'kembali' :
    	sigploit . mainMenu ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0-1)'
        waktu . tidur ( 1,5 )
        gtpattacksv2 ()

def  showOptions ( config_file = '' , remote_net = '' , listening = True , verbosity = 2 , output_file = 'results.csv' ):

    cetak ( ' \ n      Opsi                     \ t \ t \ t \ t \ t Nilai' )
    cetak ( '-------- ------' )
    print ( '      \ 033 [34mconfig \ 033 [0m {: <15s} \ t \ t \ t \ 033 [31m% s \ 033 [0m' . format ( 'path to konfigurasi file' )) % config_file
    mencetak ( '      \ 033 [34mtarget \ 033 [0m {: <15s} \ t \ 033 [31m% s \ 033 [0m' . Format ( 'contoh: 10.10.10.1/32 atau 10.10.10.0/24' )) % remote_net
    print ( '      \ 033 [34mlistening \ 033 [0m {: <15s} \ t \ 033 [31m% s \ 033 [0m' . format ( 'menerima balasan dari target, default: True' )) % mendengarkan
    print ( '      \ 033 [34mverbosity \ 033 [0m {: <15s} \ t \ t \ t \ 033 [31m% d \ 033 [0m' . format ( 'versbosity level, default: 2' )) % verbosity
    cetak ( '      \ 033 [34moutput \ 033 [0m {: <15s} \ t \ t \ 033 [31m% s \ 033 [0m \ n ' . format ( 'file keluaran, default: result.csv' )) % output_file
   

def  helpmenu ():

    cetak ( ' \ n      Deskripsi Perintah' )
    cetak ( '--------- ------------' )
    print ( '      \ 033 [34mshow options \ 033 [0m tampilkan opsi yang diperlukan untuk menjalankan serangan' )
    print ( '      \ 033 [34mset \ 033 [0m setel nilai untuk opsi' )
    print ( "      \ 033 [34mrun \ 033 [0m jalankan exploit" )
    print ( "      \ 033 [34mhelp \ 033 [0m tampilkan menu ini" )
    print ( "      \ 033 [34mback \ 033 [0m kembali ke serangan GTP" )
    cetak ( "      \ 033 [34mexit \ 033 [0m keluar SigPloit \ n " )
  

def  prep ():
    mencetak
    cetak  "Modul" . rjust ( 10 ) +  " \ t \ t Deskripsi"
    cetak  "-------- ------------"
    cetak  "0) GTPv1" . rjust ( 8 ) +  " \ t \ t Serangan Data 3G"
    cetak  "1) GTPv2" . rjust ( 8 ) +  " \ t \ t Serangan Data 4G"
    mencetak
    print  "atau ketik kembali untuk kembali ke Menu Utama" . rjust ( 39 )

    choice  =  raw_input ( " \ 033 [34mgtp \ 033 [0m \ 033 [37m> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        cetak  " \ n \ 033 [34m [*] \ 033 [0mGTPv1 akan diperbarui dalam rilis versi 2.1 .."
        cetak  " \ 033 [34m [*] \ 033 [0mKembali ke Menu GTP"
        waktu . tidur ( 2 )
        os . sistem ( 'bersih' )
        prep ()

     pilihan  elif ==  "1" :
        gtpattacksv2 ()

    elif  pilihan  ==  "kembali" :
        sigploit . mainMenu ()
