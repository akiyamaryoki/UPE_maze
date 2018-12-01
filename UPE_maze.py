#!/usr/bin/python
import requests


def solve_maze(curr, visited, token_url):
    visited.append(curr)

    left_attempt = requests.post(token_url, data={"action": "LEFT"}).json()["result"]
    if left_attempt == "SUCCESS":
        if [curr[0] - 1, curr[1]] not in visited:
            visited.append([curr[0] - 1, curr[1]])
            print("LEFT")
            return solve_maze([curr[0] - 1, curr[1]], visited, token_url)
        else:
            ret = requests.post(token_url, data={"action": "RIGHT"}).json()["result"]
            print("RIGHT")
    elif left_attempt == "END":
        return True

    right_attempt = requests.post(token_url, data={"action": "RIGHT"}).json()["result"]
    if right_attempt == "SUCCESS":
        if [curr[0] + 1, curr[1]] not in visited:
            visited.append([curr[0] + 1, curr[1]])
            print("RIGHT")
            return solve_maze([curr[0] + 1, curr[1]], visited, token_url)
        else:
            ret = requests.post(token_url, data={"action": "LEFT"}).json()["result"]
            print("LEFT")
    elif right_attempt == "END":
        return True

    up_attempt = requests.post(token_url, data={"action": "UP"}).json()["result"]
    if up_attempt == "SUCCESS":
        if [curr[0], curr[1] - 1] not in visited:
            visited.append([curr[0], curr[1] - 1])
            print("UP")
            return solve_maze([curr[0], curr[1] - 1], visited, token_url)
        else:
            ret = requests.post(token_url, data={"action": "DOWN"}).json()["result"]
            print("DOWN")
    elif up_attempt == "END":
        return True

    down_attempt = requests.post(token_url, data={"action": "DOWN"}).json()["result"]
    if down_attempt == "SUCCESS":
        if [curr[0], curr[1] + 1] not in visited:
            visited.append([curr[0], curr[1] + 1])
            print("DOWN")
            return solve_maze([curr[0], curr[1] + 1], visited, token_url)
        else:
            ret = requests.post(token_url, data={"action": "UP"}).json()["result"]
            print("UP")
    elif down_attempt == "END":
        return True

    return False

def main():
    post_url = 'http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/session'
    r = requests.post(post_url, data={"uid": "304767119"})
    token = r.json()["token"]

    token_url = 'http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=' + token

    for i in range(0, 5):

        r2 = requests.get(token_url)
        print(r2.json())

        level = r2.json()["total_levels"]
        #row = int(r2.json()["maze_size"][0])
        #col = int(r2.json()["maze_size"][1])
        curr = r2.json()["current_location"]

        visited = list()

        solve_maze(curr, visited, token_url)


if __name__ == "__main__":
    main()