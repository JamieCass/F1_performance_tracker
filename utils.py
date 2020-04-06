import time

def timetaken(start, stepname=''):
  end = time.time()
  hours, rem = divmod(end-start, 3600)
  minutes, seconds = divmod(rem, 60)
  print(stepname+':',"{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
  return end

#
# start_time = time.time()
# start_time
#
# timetaken(start_time, stepname='jamie test')
