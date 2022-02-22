from requests_html import HTMLSession
session = HTMLSession()


# Selected Direction: New York
# Selected Stop: BOULEVARD EAST + 66TH ST. (New York)
# Selected Stop: 21890
def get_bus_schedule(bus_stop_id=21890):
    if bus_stop_id == 21890:
        url = f'https://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=165&direction=New+York&id={bus_stop_id}&showAllBusses=on'
    elif bus_stop_id == 32084:
        url = f'https://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=126&direction=New+York&id={bus_stop_id}&showAllBusses=on'
    elif bus_stop_id == 26229:
        url = f'https://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=165&direction=Westwood&id={bus_stop_id}&showAllBusses=on'
    else:
        url = f'https://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=165&direction=New+York&id={bus_stop_id}&showAllBusses=on'
    print(url)
    r = session.get(url)
    res = r.html.find('.larger')
    res_arr = []
    for i in range(0, len(res)):
        if (i % 2) == 0:
            res_arr.append(res[i].text.replace(u'\xa0', ' '))
        else:
            index = len(res_arr) - 1
            res_arr[index] = res_arr[index] + ' - ' + res[i].text.replace(u'\xa0', ' ')

    bus_schedule = res_arr
    return bus_schedule


