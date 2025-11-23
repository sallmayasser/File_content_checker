from(bucket: "vm_metrics")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "flag_check" and r._field == "flag")
  |> timeShift(duration: -2h)  // to adjust the timezone diffrence 
  |> sort(columns: ["_time"])
