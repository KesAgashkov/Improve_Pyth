import yaml
from module import Site

with open("config.yaml") as f:
    data = yaml.safe_load(f)

site = Site(data["address"])

css = "div.submit.svelte-uwkxn9"

print(site.get_el_property("css", css, "width"))

xpath = '//*[@id="login"]/div[1]/label/input'

print(site.get_el_property("xpath", xpath, "color"))
