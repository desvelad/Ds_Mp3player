# Daisyxmusic (Telegram bot projesi)
# Telif Hakkı (C) 2021 Inukaasith 

# Bu program ücretsiz bir yazılımdır: yeniden dağıtabilir ve / veya
# GNU Affero Genel Kamu Lisansı koşulları altında
# Özgür Yazılım Vakfı tarafından yayınlanan
# Lisans veya (sizin tercihinize göre) daha sonraki bir sürüm.

# Bu program faydalı olması umuduyla dağıtılmaktadır,
# HİÇBİR GARANTİ OLMAKSIZIN; zımni garanti bile olmadan
# SATILABİLİRLİK VEYA BELİRLİ BİR AMACA UYGUNLUK. Bakın
# Daha fazla ayrıntı için GNU Affero Genel Kamu Lisansı.
#
# GNU Affero Genel Kamu Lisansının bir kopyasını almış olmalısınız
# bu programla birlikte. Değilse, <https://www.gnu.org/licenses/> adresine bakın.



dan  pyrogram  ithalat  Client , filtreler
dan  pyrogram . türler  Message , InlineKeyboardMarkup , InlineKeyboardButton içe  aktarır

dan  konfigürasyon dosyasında  ithalat  BOT_NAME  olarak  bn




@ M üş teri . on_message ( filtreler . komut ( "başlat" ) ve  filtreler . ö zel  &  ~  filtreler . kanal )
eşzamansız  def  start ( _ , mesaj : Mesaj ):
    mesaj ı bekleyin . yan ı t_metni (
        f ""  "Merhaba 👋! Telegram Gruplarının sesli sohbetlerinde müzik çalabiliyorum Sizi şaşırtacak pek çok harika özelliğim var! \ n \ n 🔴 Telegram gruplarınızın sesli sohbetlerinizde müzik çalmamı ister misiniz? Beni nasıl kullanabileceğinizi öğrenmek için lütfen \ 'Kullanım Kılavuzu \' tıklayın. \ n \ n 🔴 Grubunuzun sesli sohbetinde müzik çalabilmek için Asistanın grubunuzda olması gerekir. \ n \ n 🔴Daha fazla bilgi ve komut için [Komutlar] (https://telegra.ph/RgMusic-05-11) \ n \ n A @ RickGrimes_1 tarafından ... bir proje " " " ,
        answer_markup = InlineKeyboardMarkup (
            [ 
                [
                    InlineKeyboardButton (
                        "📜 Manuel komutlar 📜" , url = "https://telegra.ph/RgMusic-05-11" )
                  ], [
                    InlineKeyboardButton (
                        "👨‍💻 Güncelleme 👨‍💻" , url = "https://t.me/RgBotSupport"
                    )
                ], [ 
                    InlineKeyboardButton (
                        "Sohbet Grup 🎙️" , url = "https://t.me/RgSohbet"
                    )
                 ], [
                    İ nlineKeyboardButton (
                        "🎧RgMusic'i Grubunuza ekle" ,
                             url = f "http://t.me/RgMusiccbot" ,
            ]
        ),
     disable_web_page_preview = Doğru
    )

@ Müşteri . on_message ( filtreler . komut ( "başlat" ) &  ~ filtreler . özel  &  ~ filtreler . kanal )
eşzamansız  def  gstart ( _ , mesaj : Mesaj ):
       mesajı bekleyin . answer_text ( "" "** 🔴 Müzik çalar yayında **" "" ,
      answer_markup = InlineKeyboardMarkup (
            [
                [
                    InlineKeyboardButton (
                        "🎙️ ​​Destek Grubu 🎙️" , url = "https://t.me/RgBotSupport" )
                ]
            ]
        )
   )