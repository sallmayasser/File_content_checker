from(bucket: "vm_metrics")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "tail" and r._field == "flag")
  |> timeShift(duration: -2h)  // to adjust the timezone diffrence 
  |> aggregateWindow(every: 15m, fn: mean, createEmpty: false)
  |> sort(columns: ["_time"])
