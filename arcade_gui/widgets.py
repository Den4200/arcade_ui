from abc import ABCMeta, abstractmethod


_widgets = dict()


class _InteractiveWidgetMeta(type):

    def __new__(cls, name, bases, attrs):
        if name != 'InteractiveWidget':

            if '__widget_name__' not in attrs:
                raise AttributeError(f'Class {name} is missing attribute __widget_name__')

            if attrs['__widget_name__'] in _widgets:
                raise AttributeError(
                    f'Different classes cannot have the same value '
                    f'for __widget_name__: {repr(attrs["__widget_name__"])}'
                )

            _widgets[attrs['__widget_name__']] = list()

        return super().__new__(cls, name, bases, attrs)


class InteractiveWidgetMeta(ABCMeta, _InteractiveWidgetMeta):
    pass


class InteractiveWidget(metaclass=InteractiveWidgetMeta):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__widget_name__'):
            raise AttributeError(f'Class {cls.__name__} is missing attribute __widget_name__')

        name = cls.__widget_name__
        self = super().__new__(cls)

        _widgets[name].append(self)

        return self

    @property
    def widget_name(self):
        return self.__widget_name__

    @abstractmethod
    def move_center_x(self, delta_x: float) -> None:
        pass

    @abstractmethod
    def move_center_y(self, delta_y: float) -> None:
        pass
