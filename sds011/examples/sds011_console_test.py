import csv

from sds011 import SDS011

port = "/dev/ttyUSB0"

sds = SDS011(port=port, use_database=True)
# one measurement every 5 minutes offers decent granularity
# and at least a few years of lifetime to the sensor
# sds.set_working_period(rate=5)
print(sds)

try:
    with open("measurments.csv", "w") as csvfile:
        log = csv.writer(
            csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        logcols = ["timestamp", "pm2.5", "pm10", "device_id"]
        log.writerow(logcols)
        while True:
            meas = sds.read_measurement()
            vals = [str(meas.get(k)) for k in logcols]
            log.writerow(vals)
            csvfile.flush()
            print(vals)

except KeyboardInterrupt:
    # sds.sleep()
    sds.__del__()
