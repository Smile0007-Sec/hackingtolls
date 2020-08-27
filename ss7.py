#! / usr / bin / env python
# pengkodean: utf-8
'' '
SS7 utama 
@ Penulis: Loay Abdelrazek
@hak cipta: 2018. Semua hak dilindungi undang-undang.
@lisensi: Lisensi MIT
'' '

impor  os
 waktu impor
impor  ss7 . pelacakan
impor  ss7 . penipuan
impor  ss7 . penangkapan
impor  ss7 . dos
import  sigploit



def  bersih ():

    os . sistem ( "rm -f * .xml" )

def  ss7tracking ():
    os . sistem ( 'bersih' )

    print  " \ 033 [31mLocation Tracking \ 033 [0m" . tengah ( 105 , "#" )
    print  " \ 033 [34mPilih Pesan dari bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    cetak  "Pesan" . rjust ( 10 ) +  " \ t \ t \ t Deskripsi"
    cetak  "-------- ------------"
    cetak  "0) SendRoutingInfo" . rjust ( 21 ) +  " \ t \ t Pelacakan Lokasi, digunakan untuk merutekan panggilan dapat diblokir"
    print  "1) ProvidSubsriberInfo" . rjust ( 26 ) +  " \ t Pelacakan Lokasi yang Andal"
    cetak  "2) SendRoutingInfoForSM" . rjust ( 26 ) +  " \ t Pelacakan Lokasi yang Andal, jika perutean SMS ke rumah tidak diterapkan, harus dijalankan dua kali untuk memeriksa balasan yang konsisten"
    print  "3) AnyTimeInterrogation" . rjust ( 26 ) +  " \ t Pelacakan Lokasi, diblokir oleh sebagian besar operator"
    cetak  "4) SendRoutingInfoForGPRS" . rjust ( 28 ) +  " \ t Pelacakan lokasi, digunakan untuk data rute, itu akan mengambil SGSN GT"

    mencetak
    print  "atau ketik kembali untuk kembali ke Menu Serangan" . rjust ( 42 )

    choice  =  raw_input (
        " \ 033 [37m ( \ 033 [0m \ 033 [2; 31mtracking \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        ss7 . pelacakan . sri ()
     pilihan  elif ==  "1" :
        ss7 . pelacakan . psi ()
     pilihan  elif ==  "2" :
        ss7 . pelacakan . srism ()
     pilihan  elif ==  "3" :
        ss7 . pelacakan . ati ()
     pilihan  elif ==  "4" :
        ss7 . pelacakan . srigprs ()
    elif  pilihan  ==  "kembali" :
        attackMenu ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0 - 4)'
        waktu . tidur ( 1,5 )
        ss7tracking ()


def  ss7interception ():
    os . sistem ( 'bersih' )

    cetak  " \ 033 [31mInterception \ 033 [0m" . tengah ( 105 , "#" )
    print  " \ 033 [34mPilih Pesan dari bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    cetak  "Pesan" . rjust ( 10 ) +  " \ t \ t \ t \ t Deskripsi"
    cetak  "-------- -----------"
    cetak  "0) UpdateLocation" . rjust ( 20 ) +  " \ t \ t \ t Intersepsi SMS Tersembunyi"

    mencetak
    print  "atau ketik kembali untuk kembali ke Menu Serangan" . rjust ( 42 )

    choice  =  raw_input (
        " \ 033 [37m ( \ 033 [0m \ 033 [2; 31minterception \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        ss7 . intersepsi . ul ()

    elif  pilihan  ==  "kembali" :
        attackMenu ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0)'
        waktu . tidur ( 1,5 )
        ss7 interception ()


def  ss7fraud ():
    os . sistem ( 'bersih' )

    cetak  " \ 033 [31mFraud & Info \ 033 [0m" . tengah ( 105 , "#" )
    print  " \ 033 [34mPilih Pesan dari bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    cetak  "Pesan" . rjust ( 10 ) +  " \ t \ t \ t \ t Deskripsi"
    cetak  "-------- ------------"
    cetak  "0) SendIMSI" . rjust ( 14 ) +  " \ t \ t \ t \ t Mengambil IMSI pelanggan"
    cetak  "1) MTForwardSMS" . rjust ( 18 ) +  " \ t \ t \ t SMS Phishing dan Spoofing"
    cetak  "2) InsertSubscriberData" . rjust ( 26 ) +  " \ t \ t Maniuplasi Profil Pelanggan"
    print  "3) SendAuthenticationInfo" . rjust ( 28 ) +  " \ t \ t pengambilan Vektor Otentikasi Pelanggan"

    mencetak
    print  "atau ketik kembali untuk kembali ke Menu Serangan" . rjust ( 42 )

    choice  =  raw_input (
        " \ 033 [37m ( \ 033 [0m \ 033 [2; 31mfraud \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        ss7 . penipuan . simsi ()
     pilihan  elif ==  "1" :
        ss7 . penipuan . mtsms ()
     pilihan  elif ==  "2" :
        ss7 . penipuan . isd ()
     pilihan  elif ==  "3" :
        ss7 . penipuan . sai ()
    elif  pilihan  ==  "kembali" :
        attackMenu ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0-3)'
        waktu . tidur ( 1,5 )
        ss7fraud ()


def  ss7dos ():
    os . sistem ( 'bersih' )

    cetak  " \ 033 [31mDenial of Service \ 033 [0m" . tengah ( 105 , "#" )
    print  " \ 033 [34mPilih Pesan dari bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    cetak  "Pesan" . rjust ( 10 ) +  " \ t \ t \ t \ t Deskripsi"
    cetak  "-------- ------------"
    cetak  "0) PurgeMS-Subscriber DoS" . rjust ( 28 ) +  " \ t \ t serangan DoS massal pada Pelanggan untuk mengeluarkan mereka dari jaringan"

    mencetak
    print  "atau ketik kembali untuk kembali ke Menu Serangan" . rjust ( 42 )

    choice  =  raw_input (
        " \ 033 [37m ( \ 033 [0m \ 033 [2; 31mdos \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        ss7 . dos . pembersihan ()
    elif  pilihan  ==  "kembali" :
        attackMenu ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0)'
        waktu . tidur ( 1,5 )
        ss7dos ()


def  attackMenu ():
    os . sistem ( 'bersih' )

    print  " \ 033 [34mPilih Dari Kategori Serangan Di Bawah \ 033 [0m" . tengah ( 105 , "#" )
    mencetak
    cetak  "0) Pelacakan Lokasi" . rjust ( 23 )
    cetak  "1) Intersepsi Panggilan dan SMS" . rjust ( 31 )
    print  "2) Penipuan & Pengumpulan Info" . rjust ( 28 )
    cetak  "3) DoS" . rjust ( 9 )
    mencetak
    print  "atau ketik kembali untuk kembali ke menu utama" . rjust ( 42 )
    mencetak

    choice  =  raw_input (
        " \ 033 [37m ( \ 033 [0m \ 033 [2; 31mattacks \ 033 [0m \ 033 [37m)> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        ss7tracking ()

     pilihan  elif ==  "1" :
        ss7 interception ()

     pilihan  elif ==  "2" :
        ss7fraud ()

     pilihan  elif ==  "3" :
        ss7dos ()

    elif  pilihan  ==  "kembali" :
        sigploit . mainMenu ()
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0 - 3)'
        waktu . tidur ( 1,5 )
        attackMenu ()
