# %% import
from matplotlib import pyplot as plt
import os
from numpy.typing import ArrayLike
from cycler import cycler

# %% データ生成

y_data: ArrayLike = [
    [80, 70, 60, 90, 70],
    [50, 60, 70, 80, 90],
    [90, 95, 90, 80, 100],
]
x_data: ArrayLike = ["April", "May", "June", "July", "August"]
legends: ArrayLike = ["A", "B", "C"]
title: str = "Test Scores"
x_label: str = "Month held"
y_label: str = "Score [points]"

fig_ext: str = "png"
os.makedirs("result", exist_ok=True)

# %% 000 デフォルトのグラフ

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, marker="o")
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)
fig.show()
fig.savefig(f"result/000.{fig_ext}")

# %% 001 フォントを変更する

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, marker="o")
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)
fig.show()
fig.savefig(f"result/001.{fig_ext}")

# %% 002 線の幅とマーカーの大きさを変更する

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)
fig.show()
fig.savefig(f"result/002.{fig_ext}")

# %% 003 補助線を引く

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)
ax.grid(True, which="both")
ax.set_axisbelow(True)
fig.show()
fig.savefig(f"result/003.{fig_ext}")

# %% 004 枠を消す

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)
ax.grid(True, which="both")
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.show()
fig.savefig(f"result/004.{fig_ext}")

# %% 005 枠線を太くする
plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)
ax.grid(True, which="both")
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
fig.show()
fig.savefig(f"result/005.{fig_ext}")

# %% 006 目盛りを内側にする

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)
ax.grid(True, which="both")
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
fig.show()
fig.savefig(f"result/006.{fig_ext}")

# %% 007 凡例をグラフに埋め込む

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
# ax.legend(legends)
for index, legend in enumerate(legends):
    x_loc: float = (len(x_data) - 1.0) + len(x_data) * 0.04
    ax.text(
        x_loc,
        ax.lines[index].get_data()[1][-1],
        legend,
        color=colors[index],
        va="center",
    )
ax.grid(True, which="both")
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
fig.show()
fig.savefig(f"result/007.{fig_ext}")

# %% 008 文字の大きさを変更する

fontsize_title: float = 32.0
fontsize_label: float = 24.0
fontsize_legend: float = 24.0
fontsize_tick: float = 18.0

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title, fontsize=fontsize_title)
ax.set_xlabel(x_label, fontsize=fontsize_label)
ax.set_ylabel(y_label, fontsize=fontsize_label)
for index, legend in enumerate(legends):
    x_loc: float = (len(x_data) - 1.0) + len(x_data) * 0.04
    ax.text(
        x_loc,
        ax.lines[index].get_data()[1][-1],
        legend,
        color=colors[index],
        va="center",
        fontsize=fontsize_legend,
    )
ax.tick_params(axis="x", labelsize=fontsize_tick)
ax.tick_params(axis="y", labelsize=fontsize_tick)
ax.grid(True, which="both")
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
fig.show()
fig.savefig(
    f"result/008.{fig_ext}",
    bbox_inches="tight",
    pad_inches=0.1,
)

# %% 009 文字とグラフの間隔を変更する

fontsize_title: float = 32.0
fontsize_label: float = 24.0
fontsize_legend: float = 24.0
fontsize_tick: float = 18.0

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure()
ax = fig.add_subplot(111)
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(title, fontsize=fontsize_title, pad=fontsize_title * 0.75)
ax.set_xlabel(x_label, fontsize=fontsize_label, labelpad=fontsize_label * 0.75)
ax.set_ylabel(y_label, fontsize=fontsize_label, labelpad=fontsize_label * 0.75)
for index, legend in enumerate(legends):
    x_loc: float = (len(x_data) - 1.0) + len(x_data) * 0.04
    ax.text(
        x_loc,
        ax.lines[index].get_data()[1][-1],
        legend,
        color=colors[index],
        va="center",
        fontsize=fontsize_legend,
    )
ax.tick_params(axis="x", labelsize=fontsize_tick, pad=4.5)
ax.tick_params(axis="y", labelsize=fontsize_tick, pad=4.5)
ax.grid(True, which="both")
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
fig.show()
fig.savefig(
    f"result/009.{fig_ext}",
    bbox_inches="tight",
    pad_inches=0.1,
)

# %% 010 色を変更する

fontsize_title: float = 32.0
fontsize_label: float = 24.0
fontsize_legend: float = 24.0
fontsize_tick: float = 18.0

color_face: str = "#fafafa"
color_title: str = "#282828"
color_label: str = "#282828"
color_legend: str = "#282828"
color_grid: str = "#c0c0c0"
color_tick: str = "#424242"
# NOTE: Reference :
# https://www3.dic-global.com/dic-graphics/navi/color/pdf/cud_guidebook.pdf
colors: list[str] = [
    "#005aff",
    "#f6aa00",
    "#03af7a",
    "#ff4b00",
    "#9467bd",
    "#804000",
    "#ff8082",
    "#84919e",
    "#fff100",
    "#4dc4ff",
]

plt.rcParams["font.family"] = "Ricty diminished"

fig = plt.figure(facecolor=color_face)
ax = fig.add_subplot(111)
ax.set_facecolor(color_face)
ax.set_prop_cycle(cycler("color", colors))
for y in y_data:
    ax.plot(x_data, y, linewidth=3.0, marker="o", markersize=8.0)
ax.set_title(
    title,
    fontsize=fontsize_title,
    pad=fontsize_title * 0.75,
    color=color_title,
)
ax.set_xlabel(
    x_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
ax.set_ylabel(
    y_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
for index, legend in enumerate(legends):
    x_loc: float = (len(x_data) - 1.0) + len(x_data) * 0.04
    ax.text(
        x_loc,
        ax.lines[index].get_data()[1][-1],
        legend,
        color=colors[index],
        va="center",
        fontsize=fontsize_legend,
    )
ax.tick_params(axis="x", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.tick_params(axis="y", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.grid(True, which="both", color=color_grid)
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
ax.spines["left"].set_color(color_tick)
ax.spines["bottom"].set_color(color_tick)
fig.show()
fig.savefig(
    f"result/010.{fig_ext}",
    bbox_inches="tight",
    pad_inches=0.1,
)

# %% 011 あるデータだけ強調する

fontsize_title: float = 32.0
fontsize_label: float = 24.0
fontsize_legend: float = 24.0
fontsize_tick: float = 18.0

color_face: str = "#fafafa"
color_title: str = "#282828"
color_label: str = "#282828"
color_legend: str = "#282828"
color_grid: str = "#c0c0c0"
color_tick: str = "#424242"
colors: list[str] = [
    "#005aff",
    "#f6aa00",
    "#03af7a",
    "#ff4b00",
    "#9467bd",
    "#804000",
    "#ff8082",
    "#84919e",
    "#fff100",
    "#4dc4ff",
]
focus_indexes: list[int] = [1]
focus_color: str = colors[1]
not_focus_color: str = "#c3c3c3"

plt.rcParams["font.family"] = "Ricty diminished"

data_num: int = len(y_data)
colors: list[str] = [not_focus_color] * data_num
z_orders: list[int] = [1] * data_num
font_weights: list[str] = ["normal"] * data_num

if focus_indexes is not None and 0 < len(focus_indexes):
    for index, focus_index in enumerate(focus_indexes):
        if data_num <= focus_index:
            raise ValueError(f'"focus_index" {focus_index} is out of range.')
        colors[focus_index] = focus_color
        z_orders[focus_index] = 2
        font_weights[focus_index] = "bold"

fig = plt.figure(facecolor=color_face)
ax = fig.add_subplot(111)
ax.set_facecolor(color_face)
ax.set_prop_cycle(cycler("color", colors))
for index, y in enumerate(y_data):
    ax.plot(
        x_data,
        y,
        linewidth=3.0,
        marker="o",
        markersize=8.0,
        zorder=z_orders[index],
    )
ax.set_title(
    title,
    fontsize=fontsize_title,
    pad=fontsize_title * 0.75,
    color=color_title,
)
ax.set_xlabel(
    x_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
ax.set_ylabel(
    y_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
for index, legend in enumerate(legends):
    x_loc: float = (len(x_data) - 1.0) + len(x_data) * 0.04
    ax.text(
        x_loc,
        ax.lines[index].get_data()[1][-1],
        legend,
        color=colors[index],
        va="center",
        fontsize=fontsize_legend,
        fontweight=font_weights[index],
        zorder=z_orders[index],
    )
ax.tick_params(axis="x", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.tick_params(axis="y", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.grid(True, which="both", color=color_grid)
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
ax.spines["left"].set_color(color_tick)
ax.spines["bottom"].set_color(color_tick)
fig.show()
fig.savefig(
    f"result/011.{fig_ext}",
    bbox_inches="tight",
    pad_inches=0.1,
)

# %% 012 タイトルの位置を下にする

fontsize_title: float = 32.0
fontsize_label: float = 24.0
fontsize_legend: float = 24.0
fontsize_tick: float = 18.0

color_face: str = "#fafafa"
color_title: str = "#282828"
color_label: str = "#282828"
color_legend: str = "#282828"
color_grid: str = "#c0c0c0"
color_tick: str = "#424242"
colors: list[str] = [
    "#005aff",
    "#f6aa00",
    "#03af7a",
    "#ff4b00",
    "#9467bd",
    "#804000",
    "#ff8082",
    "#84919e",
    "#fff100",
    "#4dc4ff",
]
focus_indexes: list[int] = [1]
focus_color: str = colors[1]
not_focus_color: str = "#c3c3c3"

plt.rcParams["font.family"] = "Ricty diminished"

data_num: int = len(y_data)
colors: list[str] = [not_focus_color] * data_num
z_orders: list[int] = [1] * data_num
font_weights: list[str] = ["normal"] * data_num

if focus_indexes is not None and 0 < len(focus_indexes):
    for index, focus_index in enumerate(focus_indexes):
        if data_num <= focus_index:
            raise ValueError(f'"focus_index" {focus_index} is out of range.')
        colors[focus_index] = focus_color
        z_orders[focus_index] = 2
        font_weights[focus_index] = "bold"

fig = plt.figure(facecolor=color_face)
ax = fig.add_subplot(111)
ax.set_facecolor(color_face)
ax.set_prop_cycle(cycler("color", colors))
for index, y in enumerate(y_data):
    ax.plot(
        x_data,
        y,
        linewidth=3.0,
        marker="o",
        markersize=8.0,
        zorder=z_orders[index],
    )
ax.set_title(
    title,
    fontsize=fontsize_title,
    pad=fontsize_title * 0.75,
    color=color_title,
    y=-0.45,
)
ax.set_xlabel(
    x_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
ax.set_ylabel(
    y_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
for index, legend in enumerate(legends):
    x_loc: float = (len(x_data) - 1.0) + len(x_data) * 0.04
    ax.text(
        x_loc,
        ax.lines[index].get_data()[1][-1],
        legend,
        color=colors[index],
        va="center",
        fontsize=fontsize_legend,
        fontweight=font_weights[index],
        zorder=z_orders[index],
    )
ax.tick_params(axis="x", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.tick_params(axis="y", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.grid(True, which="both", color=color_grid)
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
ax.spines["left"].set_color(color_tick)
ax.spines["bottom"].set_color(color_tick)
fig.show()
fig.savefig(
    f"result/012.{fig_ext}",
    bbox_inches="tight",
    pad_inches=0.1,
)

# %% 013-a 凡例を埋め込まない

fontsize_title: float = 32.0
fontsize_label: float = 24.0
fontsize_legend: float = 24.0
fontsize_tick: float = 18.0

color_face: str = "#fafafa"
color_title: str = "#282828"
color_label: str = "#282828"
color_legend: str = "#282828"
color_grid: str = "#c0c0c0"
color_tick: str = "#424242"
colors: list[str] = [
    "#005aff",
    "#f6aa00",
    "#03af7a",
    "#ff4b00",
    "#9467bd",
    "#804000",
    "#ff8082",
    "#84919e",
    "#fff100",
    "#4dc4ff",
]
focus_indexes: list[int] = [1]
focus_color: str = colors[1]
not_focus_color: str = "#c3c3c3"

plt.rcParams["font.family"] = "Ricty diminished"

data_num: int = len(y_data)
colors: list[str] = [not_focus_color] * data_num
z_orders: list[int] = [1] * data_num
font_weights: list[str] = ["normal"] * data_num

if focus_indexes is not None and 0 < len(focus_indexes):
    for index, focus_index in enumerate(focus_indexes):
        if data_num <= focus_index:
            raise ValueError(f'"focus_index" {focus_index} is out of range.')
        colors[focus_index] = focus_color
        z_orders[focus_index] = 2
        font_weights[focus_index] = "bold"

fig = plt.figure(facecolor=color_face)
ax = fig.add_subplot(111)
ax.set_facecolor(color_face)
ax.set_prop_cycle(cycler("color", colors))
for index, y in enumerate(y_data):
    ax.plot(
        x_data,
        y,
        linewidth=3.0,
        marker="o",
        markersize=8.0,
        zorder=z_orders[index],
    )
ax.set_title(
    title,
    fontsize=fontsize_title,
    pad=fontsize_title * 0.75,
    color=color_title,
    y=-0.45,
)
ax.set_xlabel(
    x_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
ax.set_ylabel(
    y_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
ax.legend(
    legends,
    fancybox=False,
    bbox_to_anchor=(1.02, 1.0),
    loc="upper left",
    fontsize=fontsize_legend,
    facecolor=color_face,
    labelcolor=color_legend,
    edgecolor=color_tick,
    framealpha=1.0,
)
ax.tick_params(axis="x", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.tick_params(axis="y", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.grid(True, which="both", color=color_grid)
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
ax.spines["left"].set_color(color_tick)
ax.spines["bottom"].set_color(color_tick)
fig.show()
fig.savefig(
    f"result/013-a.{fig_ext}",
    bbox_inches="tight",
    pad_inches=0.1,
)

# %% 013-b 保存時に背景を透明にする

fontsize_title: float = 32.0
fontsize_label: float = 24.0
fontsize_legend: float = 24.0
fontsize_tick: float = 18.0

color_face: str = "#fafafa"
color_title: str = "#282828"
color_label: str = "#282828"
color_legend: str = "#282828"
color_grid: str = "#c0c0c0"
color_tick: str = "#424242"
colors: list[str] = [
    "#005aff",
    "#f6aa00",
    "#03af7a",
    "#ff4b00",
    "#9467bd",
    "#804000",
    "#ff8082",
    "#84919e",
    "#fff100",
    "#4dc4ff",
]
focus_indexes: list[int] = [1]
focus_color: str = colors[1]
not_focus_color: str = "#c3c3c3"

plt.rcParams["font.family"] = "Ricty diminished"

data_num: int = len(y_data)
colors: list[str] = [not_focus_color] * data_num
z_orders: list[int] = [1] * data_num
font_weights: list[str] = ["normal"] * data_num

if focus_indexes is not None and 0 < len(focus_indexes):
    for index, focus_index in enumerate(focus_indexes):
        if data_num <= focus_index:
            raise ValueError(f'"focus_index" {focus_index} is out of range.')
        colors[focus_index] = focus_color
        z_orders[focus_index] = 2
        font_weights[focus_index] = "bold"

fig = plt.figure(facecolor=color_face)
ax = fig.add_subplot(111)
ax.set_facecolor(color_face)
ax.set_prop_cycle(cycler("color", colors))
for index, y in enumerate(y_data):
    ax.plot(
        x_data,
        y,
        linewidth=3.0,
        marker="o",
        markersize=8.0,
        zorder=z_orders[index],
    )
ax.set_title(
    title,
    fontsize=fontsize_title,
    pad=fontsize_title * 0.75,
    color=color_title,
    y=-0.45,
)
ax.set_xlabel(
    x_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
ax.set_ylabel(
    y_label,
    fontsize=fontsize_label,
    labelpad=fontsize_label * 0.75,
    color=color_label,
)
for index, legend in enumerate(legends):
    x_loc: float = (len(x_data) - 1.0) + len(x_data) * 0.04
    ax.text(
        x_loc,
        ax.lines[index].get_data()[1][-1],
        legend,
        color=colors[index],
        va="center",
        fontsize=fontsize_legend,
        fontweight=font_weights[index],
        zorder=z_orders[index],
    )
ax.tick_params(axis="x", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.tick_params(axis="y", labelsize=fontsize_tick, pad=4.5, colors=color_tick)
ax.grid(True, which="both", color=color_grid)
ax.set_axisbelow(True)
ax.tick_params(which="both", direction="in")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)
ax.spines["left"].set_color(color_tick)
ax.spines["bottom"].set_color(color_tick)
fig.show()
fig.savefig(
    f"result/013-b.{fig_ext}",
    bbox_inches="tight",
    pad_inches=0.1,
    transparent=True,
)

# %%
