from datetime import date, datetime
import os

def clear_screen():
    if os.name == "nt":   
        os.system("cls")
    else:
        os.system("Clear")

def digital_clock(hous , minutes):
    digit_str = {
        "0" : {
            "1st" : "╭──╮",
            "2nd" : "│  │",
            "3rd" : "╰──╯"
        },
        "1" : {
            "1st" : "  |",
            "2nd" : "  |",
            "3rd" : "  |"
        },
        "2" : {
            "1st" : " ──╮",
            "2nd" : "╭──╯",
            "3rd" : "╰── "
        },
        "3" : {
            "1st" : " ──╮",
            "2nd" : " ──┤",
            "3rd" : " ──╯"
        },
        "4" : {
            "1st" : "╷  ╷",
            "2nd" : "╰──┤",
            "3rd" : "   ╵"
        },
        "5" : {
            "1st" : "╭── ",
            "2nd" : "╰──╮",
            "3rd" : " ──╯"
        },
        "6" : {
            "1st" : "╭── ",
            "2nd" : "├──╮",
            "3rd" : "╰──╯"
        },
        "7" : {
            "1st" : " ──╮",
            "2nd" : "   │",
            "3rd" : "   |"
        },
        "8" : {
            "1st" : "╭──╮",
            "2nd" : " ├──┤",
            "3rd" : "╰──╯"
        },
        "9" : {
            "1st" : "╭──╮",
            "2nd" : "╰──┤",
            "3rd" : " ──╯"
        }
    }
    first , second , third = [] , [] , []
    for i in hours:
        first.append(digit_str[i]["1st"])
        second.append(digit_str[i]["2nd"])
        third.append(digit_str[i]["3rd"])

    first.append(" ╷ ")
    second.append("   ")
    third.append(" ╵ ")

    for i in minutes:
        first.append(digit_str[i]["1st"])
        second.append(digit_str[i]["2nd"])
        third.append(digit_str[i]["3rd"])

    return "\n".join([
        " " + " ".join(first),
        " " + " ".join(second),
        " " + " ".join(third)
    ]) + "\n"

if __name__ == "__main__":
    hours , minutes = datetime.now().strftime("%I %M").split()
    clear_screen()

    print(digital_clock(hours, minutes))
    
    
