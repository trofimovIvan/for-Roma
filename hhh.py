def print_cords_in_file(part_list, v_list, now):
    moment_file = open('C:/Users/Home/PycharmProjects/project2/data/test_1'
                       '/xyz cor/moment{}.xyz'.format(now), 'w')
    print('{}'.format(len(part_list)), file=moment_file)
    print('Lattice="7.0 0.0 0.0 0.0 7.0 0.0 0.0 0.0 7.0" Properties=pos:R:3:velo:R:3 Time={}'.format(moment),
          file=moment_file)

    for i in range(len(part_list)):
        state_part = [part_list[i][0], part_list[i][1], part_list[i][2], v_list[i][0], v_list[i][1], v_list[i][2]]
        print('{}'.format(state_part[0]), '{}'.format(state_part[1]), '{}'.format(state_part[2]),
              '{}'.format(state_part[3]), '{}'.format(state_part[4]), '{}'.format(state_part[5]), file=moment_file)