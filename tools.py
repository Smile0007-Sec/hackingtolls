#! / usr / bin / env python
'' '
SigPloit Utama
Dibuat pada 1 Feb 2018
@ penulis: loay
@lisensi: Lisensi MIT
'' '

impor  sys
impor  os
 sinyal impor
 waktu impor
dari  ss7 . pelacakan  impor  *
dari  ss7 . impor intersepsi  * 
dari  ss7 . impor penipuan  * 
dari  ss7 . dos  impor  *
dari  ss7main  import  *
dari  gtpmain  import  *
dari  gtp  import  *
dari  colorama  import  init
dari  termcolor  import  cprint
dari  pyfiglet  impor  figlet_format


def  banner ( kata ):
    bentuk huruf  =  '' ' \
       | | | | | | | |
  XXX | XXX | XXX | X | | XXX | XXX |! |
  XX | XX | XX | | | | | "|
  XX | XX | XXXXXXX | XX | XXXXXXX | XX | XX | # |
XXXXX | XXX | XX | XXXXX | XX | XXX | XXXXX | $ |
XXX X | XXX | XXX X | X | X XXX | XXX | X XXX |% |
  XX | XX | XX | XXX | XXX | XX | XXX X | & |
  XXX | XXX | X | X | | | | '|
   XX | X | X | X | X | X | XX | (|
  XX | X | X | X | X | X | XX |) |
       | XX | XX | XXXXXXX | XX | XX | | * |
       | X | X | XXXXX | X | X | | + |
       | | | XXX | XXX | X | X |, |
       | | | XXXXX | | | | - |
       | | | | XXX | XXX | XXX |. |
      X | X | X | X | X | X | X | / |
  XXX | XX | XX | XX | XX | XX | XXX | 0 |
   X | XX | XX | X | X | X | XXXXX | 1 |
XXXXX | XX | X | XXXXX | X | X | XXXXXXX | 2 |
XXXXX | XX | X | XXXXX | X | XX | XXXXX | 3 |
X | XX | XX | XX | XXXXXXX | X | X | 4 |
XXXXXXX | X | X | XXXXXX | X | XX | XXXXX | 5 |
XXXXX | XX | X | XXXXXX | XX | XX | XXXXX | 6 |
XXXXXX | XX | X | X | X | X | X | 7 |
XXXXX | XX | XX | XXXXX | XX | XX | XXXXX | 8 |
XXXXX | XX | XX | XXXXXX | X | XX | XXXXX | 9 |
   X | XXX | X | | X | XXX | X |: |
  XXX | XXX | | XXX | XXX | X | X |; |
    X | X | X | X | X | X | X | <|
       | | XXXXXXX | | XXXXXXX | | | = |
  X | X | X | X | X | X | X |> |
XXXXX | XX | X | XXX | X | | X |? |
XXXXX | XX | X XXX X | X XXX X | X XXXX | X | XXXXX | @ |
   X | XX | XX | XX | XXXXXXX | XX | XX | A |
XXXXXX | XX | XX | XXXXXX | XX | XX | XXXXXX | B |
XXXXX | XX | X | X | X | XX | XXXXX | C |
XXXXXX | XX | XX | XX | XX | XX | XXXXXX | D |
XXXXXXX | X | X | XXXXX | X | X | XXXXXXX | E |
XXXXXXX | X | X | XXXXX | X | X | X | F |
21.45 | 6 8 | 7 | 2 lat | x1 x5 | 9 4 | 31,74 | G |
XX | XX | XX | XXXXXXX | XX | XX | XX | H |
  XXX | X | X | X | X | X | XXX | I |
      X | X | X | X | XX | XX | XXXXX | J |
XX | XX | XX | XXX | XX | XX | XX | K |
X | X | X | X | X | X | XXXXXXX | L |
XX | XX XX | XXXX | XXX | XX | XX | XX | M |
XX | XX X | XXX | XXX | XXX | X XX | XX | N |
XXXXXXX | XX | XX | XX | XX | XX | XXXXXXX | O |
XXXXXX | XX | XX | XXXXXX | X | X | X | P |
XXXXX | XX | XX | XX | XXX | XX | XXXX X | Q |
XXXXXX | XX | XX | XXXXXX | XX | XX | XX | R |
_IMSI | 0x1 GT | PC | _IMEI | CI | Kc 421 | _HLR_ | S |
XXXXXXX | X | X | X | X | X | X | T |
XX | XX | XX | XX | XX | XX | XXXXX | U |
XX | XX | XX | XX | XX | XX | X | V |
XX | XXX | XXX | XXX | XXX | XXX | XX XX | W |
XX | XX | XX | X | XX | XX | XX | X |
XX | XX | XX | X | X | X | X | Y |
XXXXXXX | X | X | X | X | X | XXXXXXX | Z |
XXXXX | X | X | X | X | X | XXXXX | [|
X | X | X | X | X | X | X | \ |
XXXXX | X | X | X | X | X | XXXXX |] |
   X | XX | XX | | | | | ^ |
       | | | | | | XXXXXXX | _ |
       | XXX | XXX | X | X | | | `|
       | XX | XX | XX | XXXXXX | XX | XX | a |
       | XXXXX | XX | XXXXX | XX | XX | XXXXX | b |
       | XXXX | XX | X | X | XX | XXXX | c |
       | XXXXX | XX | XX | XX | XX | XXXXX | d |
       | XXXXXX | X | XXXXX | X | X | XXXXXX | e |
       | XXXXXX | X | XXXXX | X | X | X | f |
       | XXXX | XX | X | X gtp | XX | XXXX | g |
       | XX | XX | XXXXXX | XX | XX | XX | h |
       | E | n | C | r | P | T | i |
       | X | X | X | X | XX | XXXX | j |
       | XX | XX | XXXX | XX | XX | XX | k |
       | GT | PC | x7 | x6 | x8 | Penipuan | l |
       | XX | XX XX | X XX X | XX | XX | XX | m |
       | XX | XX X | XXX | XXX | X XX | XX | n |
       | SGSN | XX | XX | XX | XX | gGsN | o |
       | Lacak | 6 8 | si | kredit | Kc | G | p |
       | XXXX | XX | XX | XXX | XX | XXX X | q |
       | XXXXX | XX | XX | XXXXX | XX | XX | r |
       | XXXX | X | XXXX | X | XX | XXXX | s |
       | --USIM-- | x0 | x2 | x3 | x8 | x6 | t |
       | XX | XX | XX | XX | XX | XXXX | u |
       | XX | XX | XX | XX | XX | XX | v |
       | XX | XX | XX | X XX X | XX XX | XX | w |
       | XX | XX | XX | XX | XX | XX | x |
       | XX | XX | X | X | X | X | y |
       | XXXXXX | X | X | X | X | XXXXXX | z |
  XXX | X | X | XX | X | X | XXX | {|
   X | X | X | | X | X | X ||i>
  XXX | X | X | XX | X | X | XXX |} |
XX | XXX | XX | | | | | ~ |
'' ' . garis terpisah ()

    table  = {}
    untuk  formulir  dalam  bentuk huruf :
        jika  '|'  dalam  bentuk :
            tabel [ formulir [ - 2 ]] =  bentuk [: - 3 ]. split ( '|' )

    ROWS  =  len ( meja . Nilai-nilai () [ 0 ])

    untuk  baris  dalam  rentang ( ROWS ):
        untuk  c  dalam  kata :
             tabel cetak [ c ] [ baris ],
        mencetak
    mencetak



def  mainMenu ():
    os . sistem ( 'bersih' )

    spanduk ( 'SigPloit' )
    cetak  " \ 033 [33m [-] [-] \ 033 [0m \ t \ t Signaling Exploitation Framework \ t \ 033 [33m [-] [-] \ 033 [0m"
    cetak  " \ 033 [33m [-] [-] \ 033 [0m \ t \ t \ t Versi: \ 033 [31mBETA 1.1 \ 033 [0m \ t \ t \ 033 [33m [-] [-] \ 033 [ 0m "
    cetak  " \ 033 [33m [-] [-] \ 033 [0m \ t \ t Penulis: \ 033 [32mLoay AbdelRazek (@sigploit) \ 033 [0m \ t \ 033 [33m [-] [-] \ 033 [ 0m \ n "
    mencetak
    cetak  "Kontributor:"

    cetak  " \ t \ 033 [31mRosalia D'Alessandro \ 033 [0m"
    cetak  " \ t \ 033 [31mIlario Dal Grande \ 033 [0m"
    mencetak
    mencetak
    mencetak
    mencetak
    mencetak
    cetak  "Modul" . rjust ( 10 ) +  " \ t \ t \ t Deskripsi"
    cetak  "-------- --------------------"
    cetak  "0) SS7" . rjust ( 8 ) +  " \ t \ t 2G / 3G Serangan Suara dan SMS"
    cetak  "1) GTP" . rjust ( 8 ) +  " \ t \ t serangan Data 3G / 4G"
    cetak  "2) Diameter" . rjust ( 13 ) +  " \ t \ t Serangan Data 4G"
    cetak  "3) SIP" . rjust ( 8 ) +  " \ t \ t serangan 4G IMS"

    mencetak
    print  "atau keluar untuk keluar dari SigPloit \ n " . rjust ( 28 )

    choice  =  raw_input ( " \ 033 [34msig \ 033 [0m \ 033 [37m> \ 033 [0m" )

    jika  pilihan  ==  "0" :
        os . sistem ( 'bersih' )
        ss7main . attackMenu ()

     pilihan  elif ==  "1" :
        os . sistem ( 'bersih' )
        prep ()
     pilihan  elif ==  "2" :
        cetak  " \ n \ 033 [34m [*] \ 033 [0mDiameter akan diperbarui dalam rilis versi 3 .."
        cetak  " \ 033 [34m [*] \ 033 [0mKembali ke Menu Utama"
        waktu . tidur ( 2 )
        mainMenu ()
     pilihan  elif ==  "3" :
        cetak  " \ n \ 033 [34m [*] \ 033 [0mSIP akan diperbarui dalam rilis versi 4 .."
        cetak  " \ 033 [34m [*] \ 033 [0mKembali ke Menu Utama"
        waktu . tidur ( 2 )
        mainMenu ()
    elif  pilihan  ==  "keluar"  atau  pilihan  ==  "keluar" :
        cetak  ' \ n Anda sekarang keluar dari SigPloit ...'
        waktu . tidur ( 1 )
        sys . keluar ( 0 )
    lain :
        print  ' \ n \ 033 [31m [-] Error: \ 033 [0m Harap Masukkan Pilihan yang Valid (0 - 3)'
        waktu . tidur ( 2 )
        mainMenu ()


def  signal_handler ( sinyal , bingkai ):
    mencetak
    cetak  ' \ n Anda sekarang keluar dari SigPloit ...'
    waktu . tidur ( 1 )
    sys . keluar ( 0 )


sinyal . sinyal ( signal . SIGINT , signal_handler )

jika  __name__  ==  '__main__' :
    mainMenu ()

jika  __name__  ==  '__sigploit__' :
    ss7tracking ()
    ss7 interception ()
    ss7fraud ()
    ss7dos ()
    attackMenu ()
    prep ()
    gtpattacksv2 ()
    gtpinfo ()
    mainMenu ()
