# pygwy-txt-analysis-applications

A script to analyze AFM scans.

## Requirements

install the pygwy-txt-analysis package from https://github.com/UP-Smart-Soft-Matter/pygwy-txt-analysis/releases

````shell
pip install path/to/pygwy-txt-analysis-[VERSION].tar.gz
````
## How to Use
1. Select the folder containing the `.txt` scan files when prompted.
2. Set scan sizes (`scan_size_x`, `scan_size_y`) in micrometers.
3. Optionally configure peak detection using `PeakFinderSettings`. Example:


```python
peak_finder_settings = pygwy_txt_analysis.PeakFinderSettings(prominence=0.3e-7)
```


4. The script will:
- Load each `.txt` file in order.
- Create and display heatmaps (`plot_scan`) and central profiles (`plot_profile`).
- Detect peaks and valleys (`plot_debug`).
- Export statistics as JSON in an `export` folder.


5. Aggregate statistics are plotted using `StatJson` and exported to CSV for height and period:


```python
stats = pygwy_txt_analysis.StatJson(os.path.join(basepath, 'export'))
stats.plot(0, x_label, x_unit) # height
stats.plot(1, x_label, x_unit) # period
stats.export_plot_data(0)
stats.export_plot_data(1)
```
---