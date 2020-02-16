from purescripto import LoadPureScript
__py__ = globals()
__ps__ = LoadPureScript(__file__, __name__)
__all__ = list(__ps__)
__py__.update(__ps__)
