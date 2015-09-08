d = {'0': (-60, -60, 20), '1': (20, -40, 20), '2': (-40, 20, 20), '3': (60, 60, 20)}
for i in range(4):
        bc = d[str(i)]
        print "%d,%d,%d" % (bc[0], bc[1], bc[2])
        print "%d,%d,%d" % (bc[0] + 20, bc[1], bc[2])
        print "%d,%d,%d" % (bc[0] + 20, bc[1] + 20, bc[2])
        print "%d,%d,%d" % (bc[0], bc[1] + 20, bc[2])
