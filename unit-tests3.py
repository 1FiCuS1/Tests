import unittest

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
     "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен",
     "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов",
     "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


class TestFindMentorPairs(unittest.TestCase):
    def find_mentor_pairs(self, courses, mentors):
        pairs = []
        for i in range(len(courses)):
            for j in range(i + 1, len(courses)):
                common_mentors = set(mentors[i]) & set(mentors[j])
                if common_mentors:
                    pairs.append(
                        f"На курсах '{courses[i]}' и '{courses[j]}' преподают: {', '.join(common_mentors)}")
        return pairs

    def test_find_mentor_pairs(self):
        result = self.find_mentor_pairs(courses, mentors)

        expected_result = [
            "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим",
            "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман",
            "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений",
            "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим",
            "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений",
            "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар"
        ]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()