confirm_total = 1.5 * 2;

total_1 = confirm_total + 1.65 * 10 + 1.65 * 1
total_2 = confirm_total + 1.65 * 10 + 1.65 * 2
total_3 = confirm_total + 1.65 * 6 + 1.75 * 4 + 1.75 * 1
total_4 = confirm_total + 1.65 * 6 + 1.75 * 4 + 1.75 * 2

print('total1:' + str(total_1))
print('total2:' + str(total_2))
print('total3:' + str(total_3))
print('total4:' + str(total_4))
print()

change_base = 1.85
for change_index in range(3, 12):
    change_total = confirm_total + 1.65 * (change_index - 3) + 2 * 0.8 * change_base
    for i in range(change_index + 2, 13):
        change_total += change_base
    change_total += change_base * 1 / 12 * (12 - change_index + 1)

    print('change total' + str(change_index) + ':' + str(change_total))
