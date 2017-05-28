class ActivitySelector:

    def show_activities(self, activities):
        sorted_activities, sorted_times = self.sort(activities)
        i = 0
        doable_activities = {}
        doable_activities[sorted_activities[i]] = sorted_times[i]

        for j in range(1, len(sorted_activities)):
            if sorted_times[i][1] < sorted_times[j][0]:
                i = j
                doable_activities[sorted_activities[i]] = sorted_times[i]

        return doable_activities


    def sort(self, activities):
        sorted_values = sorted(activities.values(), key=lambda tup: tup[1])

        keys = []
        for time in sorted_values:
            key = list(activities.keys())[list(activities.values()).index(time)]
            keys.append(key)

        return keys, sorted_values

