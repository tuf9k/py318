# Функция для чтения данных из файла
def read_file(filename):
    shows = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            day, time, kanal, type_, name = line.strip().split(maxsplit=4)
            shows.append({
                'day': day,
                'time': time,
                'kanal': kanal,
                'type': type_,
                'name': name
            })
    return shows

# a) Названия передач в указанный день и время
def shows_in_time(shows, day, start_time, end_time):
    return [s['name'] for s in shows if s['day'] == day and start_time <= s['time'] <= end_time]

# б) Названия передач в указанный день на указанном канале
def shows_on_kanal(shows, day, kanal):
    return [s['name'] for s in shows if s['day'] == day and s['kanal'] == kanal]

# в) Информация об указанном фильме
def movie_info(shows, movie_name):
    for s in shows:
        if s['name'] == movie_name:
            return s
    return "Такой передачи на данной неделе нет"

# г) Канал и время передачи "Поле чудес"
def find_pole_chudes(shows):
    for s in shows:
        if s['name'] == 'Поле чудес':
            return f"Канал: {s['kanal']}, Время: {s['time']}"
    return "Передача 'Поле чудес' не найдена"

# д) Передачи, транслирующиеся в одно и то же время
def duplicate_shows(shows):
    times = {}
    for s in shows:
        if s['time'] in times:
            times[s['time']].append(s['name'])
        else:
            times[s['time']] = [s['name']]
    return {t: names for t, names in times.items() if len(names) > 1}

# е) Передачи в указанное время
def shows_at_time(shows, time):
    return [s['name'] for s in shows if s['time'] == time]

# ж) Самая продолжительная передача в понедельник
def longest_show(shows, day):
    # Предположим, что продолжительность не указана, вернем первую найденную
    return next((s['name'] for s in shows if s['day'] == day), None)

# з) Передачи, завершающие эфир каждый день
def final_shows(shows):
    days = {}
    for s in shows:
        if s['day'] not in days or s['time'] > days[s['day']]['time']:
            days[s['day']] = s
    return {day: s['name'] for day, s in days.items()}


filename = 'TV_for13_2.txt'
shows = read_file(filename)

print("a)", shows_in_time(shows, "Понедельник", "10:00", "12:00"))
print("б)", shows_on_kanal(shows, "Понедельник", "Канал1"))
print("в)", movie_info(shows, "Название1"))
print("г)", find_pole_chudes(shows))
print("д)", duplicate_shows(shows))
print("е)", shows_at_time(shows, "10:00"))
print("ж)", longest_show(shows, "Понедельник"))
print("з)", final_shows(shows))