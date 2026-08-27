from pyscript import document
from pyodide.ffi import create_proxy

panel = document.getElementById("panel")
hair_layer = document.getElementById("hair-layer")
outfit_layer = document.getElementById("outfit-layer")
hair_options = document.getElementById("hair-options")
outfit_options = document.getElementById("outfit-options")
HAIR_BLONDE = "assets/blonde_hair.png"
HAIR_BRUNETTE = "assets/brunette_hair.png"
HAIR_WAVY_BRUNETTE = "assets/wavy_brunette_hair.png"
HAIR_LONG_ESPRESSO_BANGS = "assets/long_espresso_bangs_hair.png"
HAIR_LONG_BLACK = "assets/long_black_hair.png"
OUTFIT_CASUAL = "assets/casual_outfit.png"
OUTFIT_DRESS = "assets/dress_outfit.png"
OUTFIT_CARDIGAN_DRESS = "assets/cardigan_dress_outfit.png"
OUTFIT_BLAZER_TROUSERS = "assets/blazer_trousers_outfit.png"

undo_stack = []
redo_stack = []


def get_current_state():
    return {"hair": hair_layer.getAttribute("src"), "outfit": outfit_layer.getAttribute("src")}

def apply_state(state):
    set_layer(hair_layer, state["hair"])
    set_layer(outfit_layer, state["outfit"])

def set_layer(layer, path):
    if path:
        layer.src = path
    else:
        layer.removeAttribute("src")

def save_state():
    undo_stack.append(get_current_state())
    redo_stack.clear()

def undo(event):
    if len(undo_stack) > 0:
        redo_stack.append(get_current_state())
        previous_state = undo_stack.pop()
        apply_state(previous_state)

def redo(event):
    if len(redo_stack) > 0:
        undo_stack.append(get_current_state())
        next_state = redo_stack.pop()
        apply_state(next_state)


def open_hair_panel(event):
    if hair_options.hasAttribute("hidden"):
        panel.removeAttribute("hidden")
        hair_options.removeAttribute("hidden")
        outfit_options.setAttribute("hidden", "true")
    else:
        panel.setAttribute("hidden", "true")
        hair_options.setAttribute("hidden", "true")

def open_outfit_panel(event):
    if outfit_options.hasAttribute("hidden"):
        panel.removeAttribute("hidden")
        outfit_options.removeAttribute("hidden")
        hair_options.setAttribute("hidden", "true")
    else:
        panel.setAttribute("hidden", "true")
        outfit_options.setAttribute("hidden", "true")

def close_panel(event):
    panel.setAttribute("hidden", "true")

def toggle_layer(layer, path):
    if layer.getAttribute("src") == path:
        layer.removeAttribute("src")
    else: 
        layer.src = path


def choose_hair_blonde(event):
    save_state()
    toggle_layer(hair_layer, HAIR_BLONDE)

def choose_hair_brunette(event):
    save_state()
    toggle_layer(hair_layer, HAIR_BRUNETTE)

def choose_hair_wavy_brunette(event):
    save_state()
    toggle_layer(hair_layer, HAIR_WAVY_BRUNETTE)

def choose_hair_long_espresso_bangs(event):
    save_state()
    toggle_layer(hair_layer, HAIR_LONG_ESPRESSO_BANGS)
    
def choose_hair_long_black(event):
    save_state()
    toggle_layer(hair_layer, HAIR_LONG_BLACK)
    
def choose_outfit_casual(event):
    save_state()
    toggle_layer(outfit_layer, OUTFIT_CASUAL)

def choose_outfit_dress(event):
    save_state()
    toggle_layer(outfit_layer, OUTFIT_DRESS)

def choose_outfit_cardigan_dress(event):
    save_state()
    toggle_layer(outfit_layer, OUTFIT_CARDIGAN_DRESS)

def choose_outfit_blazer_trousers(event):
    save_state()
    toggle_layer(outfit_layer, OUTFIT_BLAZER_TROUSERS)

document.getElementById("hair-menu-btn").addEventListener("click", create_proxy(open_hair_panel))
document.getElementById("outfit-menu-btn").addEventListener("click", create_proxy(open_outfit_panel))
document.getElementById("close-btn").addEventListener("click", create_proxy(close_panel))

document.getElementById("hair-blonde-btn").addEventListener("click", create_proxy(choose_hair_blonde))
document.getElementById("hair-brunette-btn").addEventListener("click", create_proxy(choose_hair_brunette))
document.getElementById("hair-wavy-brunette-btn").addEventListener("click", create_proxy(choose_hair_wavy_brunette))
document.getElementById("hair-long-espresso-bangs-btn").addEventListener("click", create_proxy(choose_hair_long_espresso_bangs))
document.getElementById("hair-long-black-btn").addEventListener("click", create_proxy(choose_hair_long_black))
document.getElementById("outfit-casual-btn").addEventListener("click", create_proxy(choose_outfit_casual))
document.getElementById("outfit-dress-btn").addEventListener("click", create_proxy(choose_outfit_dress))
document.getElementById("outfit-cardigan-dress-btn").addEventListener("click", create_proxy(choose_outfit_cardigan_dress))
document.getElementById("outfit-blazer-trousers-btn").addEventListener("click", create_proxy(choose_outfit_blazer_trousers))

document.getElementById("undo-btn").addEventListener("click", create_proxy(undo))
document.getElementById("redo-btn").addEventListener("click", create_proxy(redo))

# Track active page indices
current_hair_page = 1
total_hair_pages = 2

current_outfit_page = 1
total_outfit_pages = 2

# Hair Pagination Handlers
def show_hair_page(page_num):
    global current_hair_page
    current_hair_page = page_num
    for i in range(1, total_hair_pages + 1):
        page = document.getElementById(f"hair-page-{i}")
        if i == page_num:
            page.classList.remove("hidden")
        else:
            page.classList.add("hidden")

def next_hair_page(event):
    if current_hair_page < total_hair_pages:
        show_hair_page(current_hair_page + 1)

def prev_hair_page(event):
    if current_hair_page > 1:
        show_hair_page(current_hair_page - 1)

# Outfit Pagination Handlers
def show_outfit_page(page_num):
    global current_outfit_page
    current_outfit_page = page_num
    for i in range(1, total_outfit_pages + 1):
        page = document.getElementById(f"outfit-page-{i}")
        if i == page_num:
            page.classList.remove("hidden")
        else:
            page.classList.add("hidden")

def next_outfit_page(event):
    if current_outfit_page < total_outfit_pages:
        show_outfit_page(current_outfit_page + 1)

def prev_outfit_page(event):
    if current_outfit_page > 1:
        show_outfit_page(current_outfit_page - 1)

# Event Listeners for Pagination Controls
document.getElementById("hair-next-btn").addEventListener("click", create_proxy(next_hair_page))
document.getElementById("hair-prev-btn").addEventListener("click", create_proxy(prev_hair_page))
document.getElementById("outfit-next-btn").addEventListener("click", create_proxy(next_outfit_page))
document.getElementById("outfit-prev-btn").addEventListener("click", create_proxy(prev_outfit_page))

