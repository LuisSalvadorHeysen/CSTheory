def aggregate_logs(logs):
    user_history = {}

    for log in logs:
        parts = log.split(' ')

        if len(parts) != 3:
            raise ValueError(f"missing action")

        timestamp, user_id, action = parts

        if user_id not in user_history:
            user_history[user_id] = {"LOGIN" : 0, "LOGOUT" : 0, "QUERY" : 0}

        if action not in user_history[user_id]:
            raise ValueError(f"invalid action {action}")
        
        user_history[user_id][action] += 1

    return user_history


def main():
    logs = [
            "100 alice LOGIN",
            "101 bob QUERY",
            "102 alice QUERY",
            "103 alice LOGOUT",
            "104 bob LOGIN"
            ]

    print(aggregate_logs(logs))

if __name__ == "__main__":
    main()
