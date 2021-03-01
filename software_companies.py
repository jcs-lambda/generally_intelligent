"""SoftwareCompanies class definition"""


class SoftwareCompanies:
    def produceData(self, names: [str], process: [str], cost: [int], amount: [int], company1: str, company2: str) -> [str]:
        processed_by = {
            name: process[i].split(' ')
            for i, name in enumerate(names)
        }

        can_process = {}
        for i, companies in enumerate(process):
            for company in companies.split():
                if company in can_process:
                    can_process[company].add(names[i])
                else:
                    can_process[company] = set([names[i]])

        seen = set()
        successes = []
        stack = [[company2, x] for x in can_process[company2]]
        while len(stack) > 0:
            path = stack.pop(-1)
            step = path[-1]
            for x in can_process[step]:
                new_path = path.copy()
                new_path.append(x)
                if x == company1:
                    successes.append(new_path)
                else:
                    if tuple(new_path) not in seen:
                        stack.append(new_path)
                        seen.add(tuple(new_path))

        companies = set()
        for success in successes:
            for company in success:
                companies.add(company)

        return sorted(companies)


if __name__ == '__main__':
    sc = SoftwareCompanies()

    example = {
        'names': ["topcoder", "doodle", "nasa", "ninny", "idm", "noname", "kintel"],
        'process': ["doodle nasa noname", "idm ninny noname", "idm ninny noname", "kintel", "kintel", "", ""],
        'cost': [1, 2, 7, 4, 6, 1, 2],
        'amount': [50, 10, 11, 9, 14, 11, 23],
        'company1': 'topcoder',
        'company2': 'kintel',
    }

    # print(example)
    print(sc.produceData(**example))
