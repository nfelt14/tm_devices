"""The wfmoutpre commands module.

These commands are used in the following models:
MSO2, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - WFMOutpre:ASC_Fmt?
    - WFMOutpre:BIT_Nr <NR1>
    - WFMOutpre:BIT_Nr?
    - WFMOutpre:BN_Fmt {RI|RP|FP}
    - WFMOutpre:BN_Fmt?
    - WFMOutpre:BYT_Nr <NR1>
    - WFMOutpre:BYT_Nr?
    - WFMOutpre:BYT_Or {LSB|MSB}
    - WFMOutpre:BYT_Or?
    - WFMOutpre:CENTERFREQuency?
    - WFMOutpre:DOMain?
    - WFMOutpre:ENCdg {ASCii|BINary}
    - WFMOutpre:ENCdg?
    - WFMOutpre:NR_Pt?
    - WFMOutpre:PT_Fmt?
    - WFMOutpre:PT_ORder?
    - WFMOutpre:PT_Off?
    - WFMOutpre:RESample <NR1>
    - WFMOutpre:RESample?
    - WFMOutpre:SPAN?
    - WFMOutpre:WFId?
    - WFMOutpre:WFMTYPe?
    - WFMOutpre:XINcr?
    - WFMOutpre:XUNit?
    - WFMOutpre:XZEro?
    - WFMOutpre:YMUlt?
    - WFMOutpre:YOFf?
    - WFMOutpre:YUNit?
    - WFMOutpre:YZEro?
    - WFMOutpre?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class WfmoutpreYzero(SCPICmdRead):
    """The ``WFMOutpre:YZEro`` command.

    Description:
        - This query-only command returns the combined vertical position and offset for the source
          waveform specified by ``DATA:SOURCE``. This represents a departure from previous
          instruments where the ``:YZEro`` value represented the vertical position in vertical units
          and the ``:YOFf`` value represented the vertical offset in digitizing levels. For this
          instrument family, the value of ``:YOFf`` is always 0.0. An error is reported if the
          ``DATA:SOURCE`` waveform does not exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:YZEro?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:YZEro?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:YZEro?
        ```
    """


class WfmoutpreYunit(SCPICmdRead):
    """The ``WFMOutpre:YUNit`` command.

    Description:
        - This query-only command returns the vertical units for the waveform specified by the
          ``DATA:SOURCE`` command. An error is reported if the ``DATa:SOUrce`` waveform does not
          exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:YUNit?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:YUNit?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:YUNit?
        ```
    """


class WfmoutpreYoff(SCPICmdRead):
    """The ``WFMOutpre:YOFf`` command.

    Description:
        - This query-only command returns the vertical offset of the source specified by
          ``DATA:SOURCE``. For this instrument family, the value returned is always 0.0 as the
          offset is combined with the ``:YZEro`` value. An error is reported if the ``DATA:SOURCE``
          waveform does not exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:YOFf?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:YOFf?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:YOFf?
        ```
    """


class WfmoutpreYmult(SCPICmdRead):
    """The ``WFMOutpre:YMUlt`` command.

    Description:
        - This query-only command returns the vertical scale factor per digitizing level in units
          specified by ``WFMOutpre:YUNit`` for the waveform specified by the ``DATA:SOURCE``
          command. For those formats in which ``WFMOUTPRE:BYT_NR`` is important (all non-floating
          point formats), ``WFMOutpre:YMUlt?`` must take the location of the binary point implied by
          ``BYT_NR`` into consideration. An error is reported if the ``DATa:SOUrce`` waveform does
          not exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:YMUlt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:YMUlt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:YMUlt?
        ```
    """


class WfmoutpreXzero(SCPICmdRead):
    """The ``WFMOutpre:XZEro`` command.

    Description:
        - This query-only command returns the sub-sample time between the trigger sample (designated
          by ``PT_OFF``) and the occurrence of the actual trigger for the waveform specified by the
          ``DATA:SOURCE`` command. This value is in units of ``WFMOutpre:XUNit``. An error is
          reported if the ``DATa:SOUrce`` waveform does not exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:XZEro?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:XZEro?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:XZEro?
        ```
    """


class WfmoutpreXunit(SCPICmdRead):
    """The ``WFMOutpre:XUNit`` command.

    Description:
        - This query-only command returns the horizontal units for the waveform specified by the
          ``DATA:SOURCE`` command. An error is reported if the ``DATa:SOUrce`` waveform does not
          exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:XUNit?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:XUNit?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:XUNit?
        ```
    """


class WfmoutpreXincr(SCPICmdRead):
    """The ``WFMOutpre:XINcr`` command.

    Description:
        - This query-only command returns the horizontal point spacing in units of
          ``WFMOutpre:XUNit`` for the waveform specified by the ``DATA:SOURCE`` command. This value
          corresponds to the sampling interval. An error is reported if the ``DATa:SOUrce`` waveform
          does not exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:XINcr?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:XINcr?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:XINcr?
        ```
    """


class WfmoutpreWfmtype(SCPICmdRead):
    """The ``WFMOutpre:WFMTYPe`` command.

    Description:
        - This query returns the type of the outgoing waveform. The type of waveform that is being
          transferred in turn determines in which window it will display on the instrument screen:
          (the Waveform View window or Spectrum View window). Both the Analog and ``RF_TD``
          arguments specify the time domain window; the ``RF_RD`` argument specifies the frequency
          domain window.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:WFMTYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:WFMTYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:WFMTYPe?
        ```
    """


class WfmoutpreWfid(SCPICmdRead):
    """The ``WFMOutpre:WFId`` command.

    Description:
        - This query-only command returns a string describing several aspects of the acquisition
          parameters for the waveform specified by the ``DATA:SOURCE`` command. An error is reported
          if the ``DATa:SOUrce`` waveform does not exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:WFId?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:WFId?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:WFId?
        ```
    """


class WfmoutpreSpan(SCPICmdRead):
    """The ``WFMOutpre:SPAN`` command.

    Description:
        - This query returns the frequency span of the outgoing waveform. The span is the range of
          frequencies you can observe around the center frequency.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:SPAN?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:SPAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:SPAN?
        ```
    """


class WfmoutpreResample(SCPICmdWrite, SCPICmdRead):
    """The ``WFMOutpre:RESample`` command.

    Description:
        - This command sets or queries the resampling of outgoing waveform data. This command is
          equivalent to setting ``DATa:RESample``. Setting the ``WFMOutpre:RESample`` value causes
          the corresponding DATa value to be updated and vice versa.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:RESample?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:RESample?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMOutpre:RESample value`` command.

    SCPI Syntax:
        ```
        - WFMOutpre:RESample <NR1>
        - WFMOutpre:RESample?
        ```

    Info:
        - ``<NR1>`` is the resampling rate. The default value is 1, which means every sample is
          returned. A value of 2 returns every other sample, while a value of 3 returns every third
          sample, and so on.
    """


class WfmoutprePtOff(SCPICmdRead):
    """The ``WFMOutpre:PT_Off`` command.

    Description:
        - This query-only command returns the trigger point relative to ``DATA:START`` for the
          waveform specified by the ``DATA:SOURCE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:PT_Off?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:PT_Off?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:PT_Off?
        ```
    """


class WfmoutprePtOrder(SCPICmdRead):
    """The ``WFMOutpre:PT_ORder`` command.

    Description:
        - This query-only command specifies whether the source waveform is Fast Acquisition. A Fast
          Acquisition waveform is stored as a 500 (vertical) by 1000 (horizontal) point bitmap. Each
          point represents display intensity for that screen location. Only CURVe? query functions
          are allowed on Fast Acquisition waveforms. When the ``WFMOutpre:PT_ORder?`` query returns
          Row, this indicates that the source is a Fast Acquisition waveform (and that each of 1000
          possible horizontal columns being transmitted contains 500 vertical points. Note: 500
          might vary based on how many channels enabled from same FastAcq group.) and waveform
          points are transmitted in the following order: left to right; then top to bottom. When the
          ``WFMOutpre:PT_ORder?`` query returns Linear, this indicates that the source is not a Fast
          Acquisition waveform (and that each horizontal column being sent contains only one
          vertical point). Note that waveform points are transmitted in the following order: top to
          bottom, then left to right.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:PT_ORder?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:PT_ORder?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:PT_ORder?
        ```
    """


class WfmoutprePtFmt(SCPICmdRead):
    """The ``WFMOutpre:PT_Fmt`` command.

    Description:
        - This query-only command returns the point format for the waveform specified by the
          ``DATA:SOURCE`` command. The format specifies a set of equations describing how the scale
          factors in the preamble are used to give meaning to the CURVE data points. An error is
          reported if the ``DATa:SOUrce`` waveform does not exist.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:PT_Fmt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:PT_Fmt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:PT_Fmt?
        ```
    """


class WfmoutpreNrPt(SCPICmdRead):
    """The ``WFMOutpre:NR_Pt`` command.

    Description:
        - This query-only command returns the number of points for the ``DATA:SOURCE`` waveform that
          will be transmitted in response to a CURVE? query.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:NR_Pt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:NR_Pt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:NR_Pt?
        ```
    """


class WfmoutpreEncdg(SCPICmdWrite, SCPICmdRead):
    """The ``WFMOutpre:ENCdg`` command.

    Description:
        - This command sets or queries the type of encoding for outgoing waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:ENCdg?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:ENCdg?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMOutpre:ENCdg value`` command.

    SCPI Syntax:
        ```
        - WFMOutpre:ENCdg {ASCii|BINary}
        - WFMOutpre:ENCdg?
        ```

    Info:
        - ``ASCii`` specifies that the outgoing data is to be in ASCII format. Waveforms internally
          stored as integers will be sent as <NR1> numbers, while those stored as floating point
          will be sent as <NR3> numbers.
        - ``BINary`` specifies that outgoing data is to be in a binary format whose further
          specification is determined by ``WFMOUTPRE:BYT_NR``, ``WFMOUTPRE:BIT_NR``,
          ``WFMOUTPRE:BN_FMT`` and ``WFMOUTPRE:BYT_OR``.
    """


class WfmoutpreDomain(SCPICmdRead):
    """The ``WFMOutpre:DOMain`` command.

    Description:
        - This query returns the domain of the outgoing waveform, either TIMe or FREQuency. If the
          domain is TIMe, it indicates that the data is to be treated as integer information. If the
          domain is FREQuency, it indicates that the data is to be treated as floating point
          information.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:DOMain?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:DOMain?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:DOMain?
        ```
    """


class WfmoutpreCenterfrequency(SCPICmdRead):
    """The ``WFMOutpre:CENTERFREQuency`` command.

    Description:
        - This query returns the center frequency of the outgoing waveform. The center frequency is
          a precise frequency at the center of the display of the frequency domain graticule. In
          many applications, it is a carrier frequency.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:CENTERFREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:CENTERFREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:CENTERFREQuency?
        ```
    """


class WfmoutpreBytOr(SCPICmdWrite, SCPICmdRead):
    """The ``WFMOutpre:BYT_Or`` command.

    Description:
        - This command sets or queries which byte of binary waveform data is transmitted first,
          during a waveform data transfer, when data points require more than one byte. This
          specification only has meaning when ``WFMOUTPRE:ENCDG`` is set to BIN.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:BYT_Or?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:BYT_Or?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMOutpre:BYT_Or value`` command.

    SCPI Syntax:
        ```
        - WFMOutpre:BYT_Or {LSB|MSB}
        - WFMOutpre:BYT_Or?
        ```

    Info:
        - ``LSB`` specifies that the least significant byte will be transmitted first.
        - ``MSB`` specifies that the most significant byte will be transmitted first.
    """


class WfmoutpreBytNr(SCPICmdWrite, SCPICmdRead):
    """The ``WFMOutpre:BYT_Nr`` command.

    Description:
        - This command sets or queries the binary field data width (bytes per point) for the
          waveform specified by the ``DATA:SOURCE`` command. Note that values will be constrained
          according to the underlying waveform data. This specification is only meaningful when
          ``WFMOUTPRE:ENCDG`` is set to BIN, and ``WFMOUTPRE:BN_FMT`` is set to either RI or RP.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:BYT_Nr?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:BYT_Nr?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMOutpre:BYT_Nr value`` command.

    SCPI Syntax:
        ```
        - WFMOutpre:BYT_Nr <NR1>
        - WFMOutpre:BYT_Nr?
        ```

    Info:
        - ``<NR1>`` is the number of bytes per data point and can be 1, 2 or 8. A value of 1 or 2
          bytes per waveform point indicates channel data; 8 bytes per waveform point indicate pixel
          map (fast acquisition) data.
    """


class WfmoutpreBnFmt(SCPICmdWrite, SCPICmdRead):
    """The ``WFMOutpre:BN_Fmt`` command.

    Description:
        - This command sets or queries the format of binary data for outgoing waveforms specified by
          the ``DATA:SOURCE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:BN_Fmt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:BN_Fmt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMOutpre:BN_Fmt value`` command.

    SCPI Syntax:
        ```
        - WFMOutpre:BN_Fmt {RI|RP|FP}
        - WFMOutpre:BN_Fmt?
        ```

    Info:
        - ``RI`` specifies signed integer data point representation.
        - ``RP`` specifies positive integer data point representation.
        - ``FP`` specifies floating point representation.
    """


class WfmoutpreBitNr(SCPICmdWrite, SCPICmdRead):
    """The ``WFMOutpre:BIT_Nr`` command.

    Description:
        - This command sets and queries the number of bits per waveform point that outgoing
          waveforms contain, as specified by the ``DATA:SOURCE`` command. Note that values will be
          constrained according to the underlying waveform data. This specification is only
          meaningful when ``WFMOUTPRE:ENCDG`` is set to BIN and ``WFMOUTPRE:BN_FMT`` is set to
          either RI or RP.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:BIT_Nr?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:BIT_Nr?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMOutpre:BIT_Nr value`` command.

    SCPI Syntax:
        ```
        - WFMOutpre:BIT_Nr <NR1>
        - WFMOutpre:BIT_Nr?
        ```

    Info:
        - ``<NR1>`` number of bits per data point can be 8 or 16.
    """


class WfmoutpreAscFmt(SCPICmdRead):
    """The ``WFMOutpre:ASC_Fmt`` command.

    Description:
        - This query returns the format for ASCII data transferred from the instrument. No command
          form is provided as the format is determined by the data source type. Some waveforms are
          normalized vector data where the data points are 8-byte doubles in floating point format
          whereas other formats are 1-byte or 2-byte integers.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre:ASC_Fmt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre:ASC_Fmt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre:ASC_Fmt?
        ```
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Wfmoutpre(SCPICmdRead):
    """The ``WFMOutpre`` command.

    Description:
        - This query-only command queries the waveform formatting data for the waveform specified by
          the ``DATA:SOURCE`` command. The preamble components are considered to be of two types;
          formatting and interpretation. The formatting components are: ENCdg, ``BN_Fmt``,
          ``BYT_Or``, ``BYT_Nr``, ``BIT_Nr``. The interpretation components are derived from the
          ``DATa:SOUrce`` specified waveform.

    Usage:
        - Using the ``.query()`` method will send the ``WFMOutpre?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMOutpre?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMOutpre?
        ```

    Properties:
        - ``.asc_fmt``: The ``WFMOutpre:ASC_Fmt`` command.
        - ``.bit_nr``: The ``WFMOutpre:BIT_Nr`` command.
        - ``.bn_fmt``: The ``WFMOutpre:BN_Fmt`` command.
        - ``.byt_nr``: The ``WFMOutpre:BYT_Nr`` command.
        - ``.byt_or``: The ``WFMOutpre:BYT_Or`` command.
        - ``.centerfrequency``: The ``WFMOutpre:CENTERFREQuency`` command.
        - ``.domain``: The ``WFMOutpre:DOMain`` command.
        - ``.encdg``: The ``WFMOutpre:ENCdg`` command.
        - ``.nr_pt``: The ``WFMOutpre:NR_Pt`` command.
        - ``.pt_fmt``: The ``WFMOutpre:PT_Fmt`` command.
        - ``.pt_order``: The ``WFMOutpre:PT_ORder`` command.
        - ``.pt_off``: The ``WFMOutpre:PT_Off`` command.
        - ``.resample``: The ``WFMOutpre:RESample`` command.
        - ``.span``: The ``WFMOutpre:SPAN`` command.
        - ``.wfid``: The ``WFMOutpre:WFId`` command.
        - ``.wfmtype``: The ``WFMOutpre:WFMTYPe`` command.
        - ``.xincr``: The ``WFMOutpre:XINcr`` command.
        - ``.xunit``: The ``WFMOutpre:XUNit`` command.
        - ``.xzero``: The ``WFMOutpre:XZEro`` command.
        - ``.ymult``: The ``WFMOutpre:YMUlt`` command.
        - ``.yoff``: The ``WFMOutpre:YOFf`` command.
        - ``.yunit``: The ``WFMOutpre:YUNit`` command.
        - ``.yzero``: The ``WFMOutpre:YZEro`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "WFMOutpre") -> None:
        super().__init__(device, cmd_syntax)
        self._asc_fmt = WfmoutpreAscFmt(device, f"{self._cmd_syntax}:ASC_Fmt")
        self._bit_nr = WfmoutpreBitNr(device, f"{self._cmd_syntax}:BIT_Nr")
        self._bn_fmt = WfmoutpreBnFmt(device, f"{self._cmd_syntax}:BN_Fmt")
        self._byt_nr = WfmoutpreBytNr(device, f"{self._cmd_syntax}:BYT_Nr")
        self._byt_or = WfmoutpreBytOr(device, f"{self._cmd_syntax}:BYT_Or")
        self._centerfrequency = WfmoutpreCenterfrequency(
            device, f"{self._cmd_syntax}:CENTERFREQuency"
        )
        self._domain = WfmoutpreDomain(device, f"{self._cmd_syntax}:DOMain")
        self._encdg = WfmoutpreEncdg(device, f"{self._cmd_syntax}:ENCdg")
        self._nr_pt = WfmoutpreNrPt(device, f"{self._cmd_syntax}:NR_Pt")
        self._pt_fmt = WfmoutprePtFmt(device, f"{self._cmd_syntax}:PT_Fmt")
        self._pt_order = WfmoutprePtOrder(device, f"{self._cmd_syntax}:PT_ORder")
        self._pt_off = WfmoutprePtOff(device, f"{self._cmd_syntax}:PT_Off")
        self._resample = WfmoutpreResample(device, f"{self._cmd_syntax}:RESample")
        self._span = WfmoutpreSpan(device, f"{self._cmd_syntax}:SPAN")
        self._wfid = WfmoutpreWfid(device, f"{self._cmd_syntax}:WFId")
        self._wfmtype = WfmoutpreWfmtype(device, f"{self._cmd_syntax}:WFMTYPe")
        self._xincr = WfmoutpreXincr(device, f"{self._cmd_syntax}:XINcr")
        self._xunit = WfmoutpreXunit(device, f"{self._cmd_syntax}:XUNit")
        self._xzero = WfmoutpreXzero(device, f"{self._cmd_syntax}:XZEro")
        self._ymult = WfmoutpreYmult(device, f"{self._cmd_syntax}:YMUlt")
        self._yoff = WfmoutpreYoff(device, f"{self._cmd_syntax}:YOFf")
        self._yunit = WfmoutpreYunit(device, f"{self._cmd_syntax}:YUNit")
        self._yzero = WfmoutpreYzero(device, f"{self._cmd_syntax}:YZEro")

    @property
    def asc_fmt(self) -> WfmoutpreAscFmt:
        """Return the ``WFMOutpre:ASC_Fmt`` command.

        Description:
            - This query returns the format for ASCII data transferred from the instrument. No
              command form is provided as the format is determined by the data source type. Some
              waveforms are normalized vector data where the data points are 8-byte doubles in
              floating point format whereas other formats are 1-byte or 2-byte integers.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:ASC_Fmt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:ASC_Fmt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:ASC_Fmt?
            ```
        """
        return self._asc_fmt

    @property
    def bit_nr(self) -> WfmoutpreBitNr:
        """Return the ``WFMOutpre:BIT_Nr`` command.

        Description:
            - This command sets and queries the number of bits per waveform point that outgoing
              waveforms contain, as specified by the ``DATA:SOURCE`` command. Note that values will
              be constrained according to the underlying waveform data. This specification is only
              meaningful when ``WFMOUTPRE:ENCDG`` is set to BIN and ``WFMOUTPRE:BN_FMT`` is set to
              either RI or RP.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:BIT_Nr?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:BIT_Nr?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMOutpre:BIT_Nr value`` command.

        SCPI Syntax:
            ```
            - WFMOutpre:BIT_Nr <NR1>
            - WFMOutpre:BIT_Nr?
            ```

        Info:
            - ``<NR1>`` number of bits per data point can be 8 or 16.
        """
        return self._bit_nr

    @property
    def bn_fmt(self) -> WfmoutpreBnFmt:
        """Return the ``WFMOutpre:BN_Fmt`` command.

        Description:
            - This command sets or queries the format of binary data for outgoing waveforms
              specified by the ``DATA:SOURCE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:BN_Fmt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:BN_Fmt?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMOutpre:BN_Fmt value`` command.

        SCPI Syntax:
            ```
            - WFMOutpre:BN_Fmt {RI|RP|FP}
            - WFMOutpre:BN_Fmt?
            ```

        Info:
            - ``RI`` specifies signed integer data point representation.
            - ``RP`` specifies positive integer data point representation.
            - ``FP`` specifies floating point representation.
        """
        return self._bn_fmt

    @property
    def byt_nr(self) -> WfmoutpreBytNr:
        """Return the ``WFMOutpre:BYT_Nr`` command.

        Description:
            - This command sets or queries the binary field data width (bytes per point) for the
              waveform specified by the ``DATA:SOURCE`` command. Note that values will be
              constrained according to the underlying waveform data. This specification is only
              meaningful when ``WFMOUTPRE:ENCDG`` is set to BIN, and ``WFMOUTPRE:BN_FMT`` is set to
              either RI or RP.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:BYT_Nr?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:BYT_Nr?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMOutpre:BYT_Nr value`` command.

        SCPI Syntax:
            ```
            - WFMOutpre:BYT_Nr <NR1>
            - WFMOutpre:BYT_Nr?
            ```

        Info:
            - ``<NR1>`` is the number of bytes per data point and can be 1, 2 or 8. A value of 1 or
              2 bytes per waveform point indicates channel data; 8 bytes per waveform point indicate
              pixel map (fast acquisition) data.
        """
        return self._byt_nr

    @property
    def byt_or(self) -> WfmoutpreBytOr:
        """Return the ``WFMOutpre:BYT_Or`` command.

        Description:
            - This command sets or queries which byte of binary waveform data is transmitted first,
              during a waveform data transfer, when data points require more than one byte. This
              specification only has meaning when ``WFMOUTPRE:ENCDG`` is set to BIN.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:BYT_Or?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:BYT_Or?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMOutpre:BYT_Or value`` command.

        SCPI Syntax:
            ```
            - WFMOutpre:BYT_Or {LSB|MSB}
            - WFMOutpre:BYT_Or?
            ```

        Info:
            - ``LSB`` specifies that the least significant byte will be transmitted first.
            - ``MSB`` specifies that the most significant byte will be transmitted first.
        """
        return self._byt_or

    @property
    def centerfrequency(self) -> WfmoutpreCenterfrequency:
        """Return the ``WFMOutpre:CENTERFREQuency`` command.

        Description:
            - This query returns the center frequency of the outgoing waveform. The center frequency
              is a precise frequency at the center of the display of the frequency domain graticule.
              In many applications, it is a carrier frequency.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:CENTERFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:CENTERFREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:CENTERFREQuency?
            ```
        """
        return self._centerfrequency

    @property
    def domain(self) -> WfmoutpreDomain:
        """Return the ``WFMOutpre:DOMain`` command.

        Description:
            - This query returns the domain of the outgoing waveform, either TIMe or FREQuency. If
              the domain is TIMe, it indicates that the data is to be treated as integer
              information. If the domain is FREQuency, it indicates that the data is to be treated
              as floating point information.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:DOMain?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:DOMain?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:DOMain?
            ```
        """
        return self._domain

    @property
    def encdg(self) -> WfmoutpreEncdg:
        """Return the ``WFMOutpre:ENCdg`` command.

        Description:
            - This command sets or queries the type of encoding for outgoing waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:ENCdg?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:ENCdg?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMOutpre:ENCdg value`` command.

        SCPI Syntax:
            ```
            - WFMOutpre:ENCdg {ASCii|BINary}
            - WFMOutpre:ENCdg?
            ```

        Info:
            - ``ASCii`` specifies that the outgoing data is to be in ASCII format. Waveforms
              internally stored as integers will be sent as <NR1> numbers, while those stored as
              floating point will be sent as <NR3> numbers.
            - ``BINary`` specifies that outgoing data is to be in a binary format whose further
              specification is determined by ``WFMOUTPRE:BYT_NR``, ``WFMOUTPRE:BIT_NR``,
              ``WFMOUTPRE:BN_FMT`` and ``WFMOUTPRE:BYT_OR``.
        """
        return self._encdg

    @property
    def nr_pt(self) -> WfmoutpreNrPt:
        """Return the ``WFMOutpre:NR_Pt`` command.

        Description:
            - This query-only command returns the number of points for the ``DATA:SOURCE`` waveform
              that will be transmitted in response to a CURVE? query.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:NR_Pt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:NR_Pt?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:NR_Pt?
            ```
        """
        return self._nr_pt

    @property
    def pt_fmt(self) -> WfmoutprePtFmt:
        """Return the ``WFMOutpre:PT_Fmt`` command.

        Description:
            - This query-only command returns the point format for the waveform specified by the
              ``DATA:SOURCE`` command. The format specifies a set of equations describing how the
              scale factors in the preamble are used to give meaning to the CURVE data points. An
              error is reported if the ``DATa:SOUrce`` waveform does not exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:PT_Fmt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:PT_Fmt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:PT_Fmt?
            ```
        """
        return self._pt_fmt

    @property
    def pt_order(self) -> WfmoutprePtOrder:
        """Return the ``WFMOutpre:PT_ORder`` command.

        Description:
            - This query-only command specifies whether the source waveform is Fast Acquisition. A
              Fast Acquisition waveform is stored as a 500 (vertical) by 1000 (horizontal) point
              bitmap. Each point represents display intensity for that screen location. Only CURVe?
              query functions are allowed on Fast Acquisition waveforms. When the
              ``WFMOutpre:PT_ORder?`` query returns Row, this indicates that the source is a Fast
              Acquisition waveform (and that each of 1000 possible horizontal columns being
              transmitted contains 500 vertical points. Note: 500 might vary based on how many
              channels enabled from same FastAcq group.) and waveform points are transmitted in the
              following order: left to right; then top to bottom. When the ``WFMOutpre:PT_ORder?``
              query returns Linear, this indicates that the source is not a Fast Acquisition
              waveform (and that each horizontal column being sent contains only one vertical
              point). Note that waveform points are transmitted in the following order: top to
              bottom, then left to right.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:PT_ORder?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:PT_ORder?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:PT_ORder?
            ```
        """
        return self._pt_order

    @property
    def pt_off(self) -> WfmoutprePtOff:
        """Return the ``WFMOutpre:PT_Off`` command.

        Description:
            - This query-only command returns the trigger point relative to ``DATA:START`` for the
              waveform specified by the ``DATA:SOURCE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:PT_Off?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:PT_Off?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:PT_Off?
            ```
        """
        return self._pt_off

    @property
    def resample(self) -> WfmoutpreResample:
        """Return the ``WFMOutpre:RESample`` command.

        Description:
            - This command sets or queries the resampling of outgoing waveform data. This command is
              equivalent to setting ``DATa:RESample``. Setting the ``WFMOutpre:RESample`` value
              causes the corresponding DATa value to be updated and vice versa.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:RESample?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:RESample?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMOutpre:RESample value`` command.

        SCPI Syntax:
            ```
            - WFMOutpre:RESample <NR1>
            - WFMOutpre:RESample?
            ```

        Info:
            - ``<NR1>`` is the resampling rate. The default value is 1, which means every sample is
              returned. A value of 2 returns every other sample, while a value of 3 returns every
              third sample, and so on.
        """
        return self._resample

    @property
    def span(self) -> WfmoutpreSpan:
        """Return the ``WFMOutpre:SPAN`` command.

        Description:
            - This query returns the frequency span of the outgoing waveform. The span is the range
              of frequencies you can observe around the center frequency.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:SPAN?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:SPAN?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:SPAN?
            ```
        """
        return self._span

    @property
    def wfid(self) -> WfmoutpreWfid:
        """Return the ``WFMOutpre:WFId`` command.

        Description:
            - This query-only command returns a string describing several aspects of the acquisition
              parameters for the waveform specified by the ``DATA:SOURCE`` command. An error is
              reported if the ``DATa:SOUrce`` waveform does not exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:WFId?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:WFId?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:WFId?
            ```
        """
        return self._wfid

    @property
    def wfmtype(self) -> WfmoutpreWfmtype:
        """Return the ``WFMOutpre:WFMTYPe`` command.

        Description:
            - This query returns the type of the outgoing waveform. The type of waveform that is
              being transferred in turn determines in which window it will display on the instrument
              screen: (the Waveform View window or Spectrum View window). Both the Analog and
              ``RF_TD`` arguments specify the time domain window; the ``RF_RD`` argument specifies
              the frequency domain window.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:WFMTYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:WFMTYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:WFMTYPe?
            ```
        """
        return self._wfmtype

    @property
    def xincr(self) -> WfmoutpreXincr:
        """Return the ``WFMOutpre:XINcr`` command.

        Description:
            - This query-only command returns the horizontal point spacing in units of
              ``WFMOutpre:XUNit`` for the waveform specified by the ``DATA:SOURCE`` command. This
              value corresponds to the sampling interval. An error is reported if the
              ``DATa:SOUrce`` waveform does not exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:XINcr?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:XINcr?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:XINcr?
            ```
        """
        return self._xincr

    @property
    def xunit(self) -> WfmoutpreXunit:
        """Return the ``WFMOutpre:XUNit`` command.

        Description:
            - This query-only command returns the horizontal units for the waveform specified by the
              ``DATA:SOURCE`` command. An error is reported if the ``DATa:SOUrce`` waveform does not
              exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:XUNit?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:XUNit?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:XUNit?
            ```
        """
        return self._xunit

    @property
    def xzero(self) -> WfmoutpreXzero:
        """Return the ``WFMOutpre:XZEro`` command.

        Description:
            - This query-only command returns the sub-sample time between the trigger sample
              (designated by ``PT_OFF``) and the occurrence of the actual trigger for the waveform
              specified by the ``DATA:SOURCE`` command. This value is in units of
              ``WFMOutpre:XUNit``. An error is reported if the ``DATa:SOUrce`` waveform does not
              exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:XZEro?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:XZEro?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:XZEro?
            ```
        """
        return self._xzero

    @property
    def ymult(self) -> WfmoutpreYmult:
        """Return the ``WFMOutpre:YMUlt`` command.

        Description:
            - This query-only command returns the vertical scale factor per digitizing level in
              units specified by ``WFMOutpre:YUNit`` for the waveform specified by the
              ``DATA:SOURCE`` command. For those formats in which ``WFMOUTPRE:BYT_NR`` is important
              (all non-floating point formats), ``WFMOutpre:YMUlt?`` must take the location of the
              binary point implied by ``BYT_NR`` into consideration. An error is reported if the
              ``DATa:SOUrce`` waveform does not exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:YMUlt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:YMUlt?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:YMUlt?
            ```
        """
        return self._ymult

    @property
    def yoff(self) -> WfmoutpreYoff:
        """Return the ``WFMOutpre:YOFf`` command.

        Description:
            - This query-only command returns the vertical offset of the source specified by
              ``DATA:SOURCE``. For this instrument family, the value returned is always 0.0 as the
              offset is combined with the ``:YZEro`` value. An error is reported if the
              ``DATA:SOURCE`` waveform does not exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:YOFf?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:YOFf?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:YOFf?
            ```
        """
        return self._yoff

    @property
    def yunit(self) -> WfmoutpreYunit:
        """Return the ``WFMOutpre:YUNit`` command.

        Description:
            - This query-only command returns the vertical units for the waveform specified by the
              ``DATA:SOURCE`` command. An error is reported if the ``DATa:SOUrce`` waveform does not
              exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:YUNit?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:YUNit?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:YUNit?
            ```
        """
        return self._yunit

    @property
    def yzero(self) -> WfmoutpreYzero:
        """Return the ``WFMOutpre:YZEro`` command.

        Description:
            - This query-only command returns the combined vertical position and offset for the
              source waveform specified by ``DATA:SOURCE``. This represents a departure from
              previous instruments where the ``:YZEro`` value represented the vertical position in
              vertical units and the ``:YOFf`` value represented the vertical offset in digitizing
              levels. For this instrument family, the value of ``:YOFf`` is always 0.0. An error is
              reported if the ``DATA:SOURCE`` waveform does not exist.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre:YZEro?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre:YZEro?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre:YZEro?
            ```
        """
        return self._yzero
