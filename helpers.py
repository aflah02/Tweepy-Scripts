def get_friend_names(api, username):
    user = api.get_user(username)
    ls_friends = []
    for friend in user.friends():
        ls_friends.append(friend.screen_name)
    return ls_friends