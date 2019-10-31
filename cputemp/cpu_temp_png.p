set terminal png size 1000,500
set output "cpu_temp.png"
set title "Pi CPU Temp"
set xlabel "Time"
set ylabel "Temp"
set grid
set key off
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time
set format x "%H:%M"
set yrange [50:90]
set datafile separator ","
plot "cpu_temp.csv" using 1:2 with lines
