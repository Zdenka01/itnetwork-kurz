from modules.person import Person

class EvidenceIS:
    def __init__(self):
        self.insured_members = []

    def start(self):
        """Main method"""
        print(f"{'-'*26}\n   Evidence pojištěných\n{'-'*26}\n")
        print("Zvolte akci:")
        print("1 - Registrace nového pojištěnce")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Ukončit program")
        print(" ")

        while True:
            action = input("Zvolte akci: ")
            self._print_newline()
            if action == "1":
                self.register_new_member()
                continue
            elif action == "2":
                self.list_members()
                continue
            elif action == "3":
                self.search_member()
                continue
            elif action == "4":
                exit()
            else:
                print("Zvolte prosím akci v rozsahu 1-4")
                continue

    def register_new_member(self):
        """Registruje nového člena"""
        try:
            name    = input("Zadejte jméno pojištěnce: ")
            surname = input("Zadejte příjmení pojištěnce: ")
            age     = int(input("Zadejte věk pojištěnce: "))
            phone   = int(input("Zadejte telefonní číslo pojištěnce: ").replace(" ", ""))
            if not all([name.replace(" ", "").isalpha(), surname.replace(" ", "").isalpha()]):
                raise ValueError
        except ValueError:
            print("\nVložené údaje mají špatný formát, zkuste to prosím znovu\n")
            self.register_new_member()

        new_person = Person(name=name, surname=surname, age=age, phone=phone)
        self.insured_members.append(new_person)
        print(f"\nOsoba byla úspěšně vložena do evidence\n")

    def search_member(self):
        """Umožňuje vyhledat existujícího uživatele dle jména nebo příjmení"""
        query = input("Zadejte jméno NEBO příjmení uživatele, kterého chcete vyhledat: ").strip().lower()
        result = [member for member in self.insured_members if query in [member.name.lower(), member.surname.lower()]]
        if result:
            for person in result:
                self._pretty_print_member(person)
        else:
            print("Osoba nebyla v evidenci nalezena")
        self._print_newline()

    def list_members(self):
        """Vylistuje tabulku všech evidovaných (pojištěných) osob"""
        if self.insured_members:
            for person in self.insured_members:
                self._pretty_print_member(person)
        else:
            print("Evidence pojištěných je prázdná, nejprve prosím zaregistrujte nového pojištěnce")
        self._print_newline()

    def _pretty_print_member(self, person):
        for info_column in [person.name, person.surname, person.age, person.phone]:
            print(self._fixed_length(info_column), end="")
        self._print_newline()

    def _fixed_length(self, text, length=15):
        text = str(text)
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " " * length)[:length]
        return text

    def _print_newline(self):
        print(" ")