from recognizers.ip import is_ip, lookup_ip
from output import output_to_file, print_json, print_table
from recognizers.social import check_username

def dispatch(args: list[str]):
    if args[0] == "ip":
        if len(args) < 2:
            print("Please provide an IP address.")
            return
        ip = args[1]
        if not is_ip(ip):
            print("Please provide a valid IP address.")
            return
        res = lookup_ip(ip)
        if res is None:
            print("Failed to lookup IP address.")
            return
        print_table([res])
        print_json(res)
        output_to_file(res, "ip_result.json")
    elif args[0] == "social":
        if len(args) < 2:
            print("Please provide a username.")
            return
        username = args[1]
        res = check_username(username)
        print_table([res])
        print_json(res)
        output_to_file(res, "social_result.json")
    else:
        print("Invalid command.")
