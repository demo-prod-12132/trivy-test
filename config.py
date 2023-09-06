import tomli

CFG = None

with open("config.toml", mode="rb") as cfg:
    CFG = tomli.load(cfg)
