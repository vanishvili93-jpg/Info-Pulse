import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://steadypulsejw.com/click?key=fefb4fd98eb34f1989dfda638b3d082b", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Czytaj", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Czytaj teraz", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Czytaj teraz", url="https://steadypulsejw.com/click?key=fefb4fd98eb34f1989dfda638b3d082b")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"))
    text = ("📰 *Witamy w Codzienne Tematy.*\n\n"
        "Kazdego dnia wybor artykulow o kulturze, "
        "podrozach, kuchni, nauce i technologii "
        "— do czytania w spokoju w chacie.\n\n"
        "Aby rozpoczac, nacisnij *Tematy dnia*.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Kultura — jesienne wystawy", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Kuchnia — polskie przepisy", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Podroze — piec miasteczek", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"))
    text = ("📋 *Tematy dnia*\n\n"
        "Trzy lektury wybrane na dzis. "
        "Kazda w calosci w chacie.\n\n"
        "*Kultura* — jesienne wystawy: piec "
        "wydarzen w polskich muzeach.\n\n"
        "*Kuchnia* — polskie klasyki: cztery "
        "tradycyjne przepisy.\n\n"
        "*Podroze* — piec polskich miasteczek "
        "na jesienny weekend.\n\n"
        "Nacisnij tytul, zeby otworzyc artykul.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"))
    text = ("🎨 *Jesienne wystawy: piec wydarzen "
        "w polskich muzeach*\n\n"
        "Muzea otwieraja nowy sezon.\n\n"
        "*Warszawa — Muzeum Narodowe*\n"
        "Wielka retrospektywa polskiego malarstwa "
        "miedzywojennego. Rzadko pokazywane dziela "
        "z prywatnych kolekcji i materialy "
        "archiwalne.\n\n"
        "*Krakow — Muzeum Sztuki Wspolczesnej MOCAK*\n"
        "Nowe pokolenie polskich artystow. "
        "Instalacje, wideo i rzezba w dialogu "
        "ze stala kolekcja.\n\n"
        "*Gdansk — Muzeum Narodowe*\n"
        "Sztuka Pomorza od sredniowiecza po "
        "wspolczesnosc. Sad Ostateczny Memlinga "
        "w nowym swietle.\n\n"
        "*Wroclaw — Muzeum Wspolczesne*\n"
        "Fotografia dokumentalna Dolnego Slaska. "
        "Czarno-biale reportaze o przemianach "
        "regionu.\n\n"
        "*Poznan — Muzeum Narodowe*\n"
        "Malarstwo Mlodej Polski i secesja. "
        "Wyspianski, Mehoffer i Malczewski "
        "obok sztuki wspolczesnej.\n\n"
        "_Godziny otwarcia na stronach muzeow._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"))
    text = ("🍳 *Polskie klasyki: cztery "
        "tradycyjne przepisy*\n\n"
        "Polska kuchnia to skarb "
        "regionalnych smakow.\n\n"
        "*Pierogi ruskie*\n"
        "Ciasto z nadzieniem z ziemniakow, "
        "twarogu i smazonej cebuli. Gotowane "
        "i podsmazione na masle. Klasyk "
        "niedzielnego obiadu.\n\n"
        "*Bigos*\n"
        "Kiszona kapusta, mieso, kielbasa, "
        "suszone grzyby i sliwki. Duszony "
        "godzinami — im dluzej, tym lepszy. "
        "Potrawa mysliwska.\n\n"
        "*Zurek*\n"
        "Zakwas zytni, biala kielbasa, "
        "jajko i ziemniaki. Podawany "
        "w chlebie lub na talerzu. Smak "
        "polskiej Wielkanocy.\n\n"
        "*Sernik*\n"
        "Twarog, jajka, maslo i cukier. "
        "Pieczony do zlotego koloru. "
        "Najlepszy na drugi dzien, kiedy "
        "smaki sie polacza.\n\n"
        "_Proporcje wedlug wlasnego gustu._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"))
    text = ("🏠 *Piec polskich miasteczek "
        "na jesienny weekend*\n\n"
        "*Kazimierz Dolny (Lubelskie)*\n"
        "Renesansowe kamienice nad Wisla. "
        "Galerie, kawiarnie i widok z Gory "
        "Trzech Krzyzy. Jesienia magiczny.\n\n"
        "*Zalipie (Malopolskie)*\n"
        "Malowana wies — kwiaty na scianach "
        "domow, studniach i plotach. Tradycja "
        "ktora zyje od ponad stu lat.\n\n"
        "*Sandomierz (Swietokrzyskie)*\n"
        "Stare Miasto na lesie, podziemna "
        "trasa turystyczna i Brama Opatowska. "
        "Jeden z najpiekniejszych rynkow "
        "w Polsce.\n\n"
        "*Lanckorona (Malopolskie)*\n"
        "Drewniane domy na zboczu gory. "
        "Ruiny zamku, cisza i widok na "
        "Tatry w pogodne dni.\n\n"
        "*Frombork (Warminsko-Mazurskie)*\n"
        "Miasto Kopernika nad Zalewem "
        "Wislanym. Katedra na wzgorzu, "
        "muzeum i spokojne wieczory "
        "nad woda.\n\n"
        "_Rezerwacja noclegu z wyprzedzeniem._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Slownik", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Najczescsze pytania", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Kontakt", callback_data="contact"), types.InlineKeyboardButton(text="🏛 O nas", callback_data="about"))
    text = ("🏛 *Podsumowanie*\n\n"
        "Z tego menu mozesz:\n\n"
        "• Przeczytac *tematy dnia* i nasze artykuly.\n"
        "• Przegladac sekcje: Kultura, "
        "Podroze, Kuchnia, Nauka.\n"
        "• Sprawdzic slownik i najczestsze pytania.\n"
        "• Poznac nas i skontaktowac sie z redakcja.\n\n"
        "Aby przeczytac pelne wydanie, "
        "uzyj przycisku ponizej.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"))
    text = ("📖 *Krotki slownik*\n\n"
        "*Redakcja* — zespol, ktory wybiera "
        "i przygotowuje teksty.\n\n"
        "*Felieton* — artykul opiniotwrczy "
        "otwierajacy sekcje.\n\n"
        "*Fotoreportaz* — opowiesc dziennikarska "
        "zbudowana na fotografiach.\n\n"
        "*Tresc ponadczasowa* — tekst, ktorego "
        "aktualnosc nie zalezy od wiadomosci "
        "dnia.\n\n"
        "*Korespondent* — dziennikarz relacjonujacy "
        "z terenu.\n\n"
        "*Rubryka* — stala sekcja poswiecona "
        "konkretnemu tematowi.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"))
    text = ("❓ *Najczestsze pytania*\n\n"
        "*Czy ten bot jest oficjalny?*\n"
        "Codzienne Tematy to niezalezny "
        "projekt redakcyjny.\n\n"
        "*Jak czesto jest aktualizowany?*\n"
        "Wybor jest odswiezany sezonowo.\n\n"
        "*Jak wylaczyc powiadomienia?*\n"
        "W ustawieniach czatu Telegram.\n\n"
        "*Czy moge udostepnic artykul?*\n"
        "Tak, uzywajac opcji udostepniania "
        "w Telegram.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"), types.InlineKeyboardButton(text="🏛 O nas", callback_data="about"))
    text = ("✏️ *Kontakt*\n\n"
        "Do korespondencji redakcyjnej:\n"
        "• E-mail: redakcja@codziennetematy.pl\n\n"
        "*Wydawca*\n"
        "Codzienne Tematy Sp. z o.o.\n"
        "ul. Nowy Swiat 35\n"
        "00-029 Warszawa\n"
        "Polska\n\n"
        "Uwagi czytelnikow w dni robocze.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Podsumowanie", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Kontakt", callback_data="contact"))
    text = ("🏛 *O nas*\n\n"
        "Codzienne Tematy to niezalezny "
        "projekt redakcyjny poswiecony "
        "kulturze, podrozom, kuchni "
        "i technologii.\n\n"
        "Redakcja codziennie wybiera "
        "wartosciowe tresci dla "
        "swiadomej przerwy od codziennosci.\n\n"
        "Ta edycja Telegram jest stworzona "
        "do wygodnego czytania w chacie.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Tematy dnia", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Witamy! Nacisnij *Tematy dnia*, zeby rozpoczac.", parse_mode="Markdown", reply_markup=markup)


print("Codzienne Tematy Bot is running...")
bot.infinity_polling()
