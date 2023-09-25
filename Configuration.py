import math

import Log

class Configuration_2_1_0:
  """reference to `MMWAVE SDK User Guide`

  MMWAVE SDK User Guide

  Product Release 2.1.0

  Release Date: Oct 5, 2018

  Document Version: 1.0

  Manufacturer: Texas Instruments Incorporated

  http://www.ti.com

  Currently only supports `xWR1443`
  """
  __ProductRelease__ = '2.1.0'
  logger_parse:  Log.Logger | None = None
  platform = None
  commandParameters = {
    # The values in this command should not change between sensorStop and sensorStart.
    # Reboot the board to try config with different set of values in this command.
    # This is a mandatory command.
    "dfeDataOutputMode": {
    #   <modeType>
    #     1 - frame based chirps
    #     2 - continuous chirping
    #     3 - advanced frame config
      "modeType": None
    },
    # Channel config message to RadarSS. See mmwavelink doxgen for details.
    # The values in this command should not change between sensorStop and sensorStart.
    # Reboot the board to try config with different set of values in this command.
    # This is a mandatory command.
    "channelCfg": {
    #   <rxChannelEn>
    #     Receive antenna mask e.g for 4 antennas, it is 0x1111b: 15
      "rxChannelEn": None,
    #   <txChannelEn>
    #     Transmit antenna mask
      "txChannelEn": None,
    #   <cascading>
    #     SoC cascading, not applicable, set to 0
      "cascading": None
    },
    # ADC config message to RadarSS. See mmwavelink doxgen for details.
    # The values in this command should not change between sensorStop and sensorStart.
    # Reboot the board to try config with different set of values in this command.
    # This is a mandatory command.
    "adcCfg": {
    #   <numADCBits>
    #     Number of ADC bits (0 for 12-bits, 1 for 14-bits and 2 for 16-bits)
      "numADCBits": None,
    #   <adcOutputFmt>
    #     Output format :
    #       0 - real
    #       1 - complex 1x (image band filtered output)
    #       2 - complex 2x (image band visible)
      "adcOutputFmt": None
    },
    # adcBuf hardware config. The values in this command can be changed between sensorStop and sensorStart.
    # This is a mandatory command.
    "adcbufCfg": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <adcOutputFmt>
    #     ADCBUF out format
    #       0 - Complex,
    #       1 - Real
      "adcOutputFmt": None,
    #   <SampleSwap>
    #     ADCBUF IQ swap selection:
    #       0 - I in LSB, Q in MSB,
    #       1 - Q in LSB, I in MSB
      "SampleSwap": None,
    #   <ChanInterleave>
    #     ADCBUF channel interleave configuration:
    #       0 - interleaved(not supported on XWR16xx),
    #       1 - non-interleaved
      "ChanInterleave": None,
    #   <ChirpThreshold>
    #     Chirp Threshold configuration used for ADCBUF buffer to trigger ping/pong buffer switch.
    #     Valid values:
    #       0-8 for xWR16xx (conditions apply, see description in "Usage in mmW demo xwr16xx" column)
    #       only 1 for xWR14xx
      "ChirpThreshold": None,
    },
    # Profile config message to RadarSS and datapath.
    # See mmwavelink doxgen for details.
    # The values in this command can be changed between sensorStop and sensorStart.
    # This is a mandatory command.
    "profileCfg": {
    #   <profileId>
    #     profile Identifier
      "profileId": None,
    #   <startFreq>
    #     "Frequency Start" in GHz (float values allowed)
    #     Examples:
    #       77
    #       78.1
      "startFreq": None,
    #   <idleTime>
    #     "Idle Time" in u-sec (float values allowed)
    #     Examples:
    #       7
    #       7.15
      "idleTime": None,
    #   <adcStartTime>
    #     "ADC Valid Start Time" in usec (float values allowed)
    #     Examples:
    #       7
    #       7.34
      "adcStartTime": None,
    #   <rampEndTime>
    #     "Ramp End Time" in u-sec (float values allowed)
    #     Examples:
    #       58
    #       216.15
      "rampEndTime": None,
    #   <txOutPower>
    #     Tx output power back-off code for tx antennas
      "txOutPower": None,
    #   <txPhaseShifter>
    #     tx phase shifter for tx antennas
      "txPhaseShifter": None,
    #   <freqSlopeConst>
    #     "Frequency slope" for the chirp in MHz/usec (float values allowed)
    #     Examples:
    #       68
    #       16.83
      "freqSlopeConst": None,
    #   <txStartTime>
    #     "TX Start Time" in u-sec (float values allowed)
    #     Examples:
    #       1
    #       2.92
      "txStartTime": None,
    #   <numAdcSamples>
    #     number of ADC samples collected during "ADC Sampling Time" as shown in the chirp diagram above.
    #     Examples:
    #       256
    #       224
      "numAdcSamples": None,
    #   <digOutSampleRate>
    #     ADC sampling frequency in ksps.
    #     (<numAdcSamples> / <digOutSampleRate>: "ADC Sampling Time")
    #     Examples:
    #       5500
      "digOutSampleRate": None,
    #   <hpfCornerFreq1>
    #     HPF1 (High Pass Filter 1) corner frequency
    #       0: 175 KHz
    #       1: 235 KHz
    #       2: 350 KHz
    #       3: 700 KHz
      "hpfCornerFreq1": None,
    #   <hpfCornerFreq2>
    #     HPF2 (High Pass Filter 2) corner frequency
    #       0: 350 KHz
    #       1: 700 KHz
    #       2: 1.4 MHz
    #       3: 2.8 MHz
      "hpfCornerFreq2": None,
    #   <rxGain>
    #     OR'ed value of RX gain in dB and RF gain target (See mmwavelink doxgen for details)
      "rxGain": None,
    },
    # Chirp config message to RadarSS and datapath.
    # See mmwavelink doxgen for details.
    # The values in this command can be changed between sensorStop and sensorStart.
    # This is a mandatory command.
    "chirpCfg": {
    #   chirp start index
      "chirpStartIndex": None,
    #   chirp end index
      "chirpEndIndex": None,
    #   profile identifier
      "profileIdentifier": None,
    #   start frequency variation in Hz (float values allowed)
      "startFrequencyVariation": None,
    #   frequency slope variation in kHz/us (float values allowed)
      "frequencySlopeVariation": None,
    #   idle time variation in u-sec (float values allowed)
      "idleTimeVariation": None,
    #   ADC start time variation in usec (float values allowed)
      "adcStartTimeVariation": None,
    #   tx antenna enable mask (Tx2,Tx1) e.g (10)b: Tx2 enabled, Tx1 disabled.
      "txAntennaEnableMask": None,
    },
    # BPM MIMO configuration.
    # Every frame consists of alternating chirps with pattern TX1_Tx2 and TX1-TX2. 
    # This is alternate configuration to TDM-MIMO scheme and provides SNR improvement by running 2Tx simultaneously.
    # When using this scheme, user should enable both the azimuth TX in the chirpCfg. 
    # See profile_2d_bpm.cfg profile in the xwr16xx mmW demo profiles directory for example usage.
    # This config is supported only for xWR16xx.
    "bpmCfg": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <enabled>
    #     0 - Disabled
    #     1 - Enabled
      "enabled": None,
    #   <chirp0Idx>
    #     BPM enabled:
    #       If BPM is enabled in previous argument, this is the chirp index for the first BPM chirp.
    #       It will have phase 0 on both TX antennas (TX0+ , TX1+).
    #       Note that the chirpCfg command for this chirp index must have both TX antennas enabled.
    #     BPM disabled:
    #       If BPM is disabled, a BPM disable command (set phase to zero on both TX antennas) will be issued for the chirps in the range [chirp 0Idx..chirp1Idx]
      "chirp0Idx": None,
    #   <chirp1Idx>
    #     BPM enabled:
    #       If BPM is enabled, this is the chirp index for the second BPM chirp.
    #       It will have phase 0 on TX0 and phase 180 on TX1 (TX0+ , TX1-). 
    #       Note that the chirpCfg command for this chirp index must have both TX antennas enabled.
    #     BPM disabled:
    #       If BPM is disabled, a BPM disable command (set phase to zero on both TX antennas) will be issued for the chirps in the range [chirp 0Idx..chirp1Idx].
      "chirp1Idx": None,
    },
    # Low Power mode config message to RadarSS.
    # See mmwavelink doxgen for details.
    # The values in this command should not change between sensorStop and sensorStart.
    # Reboot the board to try config with different set of values in this command.
    # This is a mandatory command.
    "lowPower": {
    #   <don’t_care>
      "dontCare": None,
    #   ADC Mode
    #     0x00 : Regular ADC mode
    #     0x01 : Low power ADC mode
      "adcMode": None,
    },
    # frame config message to RadarSS and datapath.
    # See mmwavelink doxgen for details.
    # dfeOutputMode should be set to 1 to use this command.
    # The values in this command can be changed between sensorStop and sensorStart.
    # This is a mandatory command when dfeOutputMode is set to 1.
    "frameCfg": {
    #   chirp start index (0-511)
      "chirpStartIndex": None,
    #   chirp end index (chirp start index-511)
      "chirpEndIndex": None,
    #   number of loops (1 to 255)
      "numberOfLoops": None,
    #   number of frames (valid range is 0 to 65535, 0 means infinite)
      "numberOfFrames": None,
    #   frame periodicity in ms (float values allowed)
      "framePeriodicity": None,
    #   trigger select
    #     1: Software trigger.
    #     2: Hardware trigger.
      "triggerSelect": None,
    #   Frame trigger delay in ms (float values allowed)
      "frameTriggerDelay": None,
    },
    # Advanced config message to RadarSS and datapath. 
    # See mmwavelink doxgen for details.
    # The dfeOutputMode should be set to 3 to use this command. 
    # See profile_advanced_subframe.cfg profile in the xwr16xx mmW demo profiles directory for example usage.
    # The values in this command can be changed between sensorStop and sensorStart.
    # This is a mandatory command when dfeOutputMode is set to 3.
    "advFrameCfg": {
    #   <numOfSubFrames>
    #     Number of sub frames enabled in this frame.
      "numOfSubFrames": None,
    #   <forceProfile>
    #     Force profile
      "forceProfile": None,
    #   <numFrames>
    #     Number of frames to transmit (1 frame: all enabled sub frames)
      "numFrames": None,
    #   <triggerSelect>
    #     trigger select
    #       1: Software trigger.
    #       2: Hardware trigger.
      "triggerSelect": None,
    #   <frameTrigDelay>
    #     Frame trigger delay in ms (float values allowed)
      "frameTrigDelay": None,
    },
    # Subframe config message to RadarSS and datapath. 
    # See mmwavelink doxgen for details.
    # The dfeOutputMode should be set to 3 to use this command. 
    # See profile_advanced_subframe.cfg profile in the xwr16xx mmW demo profiles directory for example usage The values in this command can be changed between sensorStop and sensorStart.
    # This is a mandatory command when dfeOutputMode is set to 3.
    "subFrameCfg": {
    # <subFrameNum>
    #   subframe Number for which this command is being given
      "subFrameNum": None,
    # <forceProfileIdx>
    #   Force profile index
      "forceProfileIdx": None,
    # <chirpStartIdx>
    #   Start Index of Chirp
      "chirpStartIdx": None,
    # <numOfChirps>
    #   Num of unique Chirps per burst including start index
      "numOfChirps": None,
    # <numLoops>
    #   No. of times to loop through the unique chirps
      "numLoops": None,
    # <burstPeriodicity>
    #   Burst periodicty in msec (float values allowed) and meets the criteria
    #   burstPeriodicity >= (numLoops)* (numOfChirps) + InterBurstBlankTime
      "burstPeriodicity": None,
    # <chirpStartIdxOffset>
    #   Chirp Start address increament for next burst
      "chirpStartIdxOffset": None,
    # <numOfBurst>
    #   Num of bursts in the subframe
      "numOfBurst": None,
    # <numOfBurstLoops>
    #   Number of times to loop over the set of above defined bursts, in the sub frame
      "numOfBurstLoops": None,
    # <subFramePeriodicity>
    #   subFrame periodicty in msec (float values allowed) and meets the criteria
    #   subFramePeriodicity >= Sum total time of all bursts + InterSubFrameBlankTime
      "subFramePeriodicity": None,
    },
    # Plot config message to datapath.
    # The values in this command can be changed between sensorStop and sensorStart.
    # This is a mandatory command.
    "guiMonitor": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <detected objects>
    #     1 - enable export of detected objects
    #     0 - disable
      "detectedObjects": None,
    #   <log magnitude range>
    #     1 - enable export of log magnitude range profile at zero Doppler
    #     0 - disable
      "logMagnitudeRange": None,
    #   <noise profile>
    #     1 - enable export of log magnitude noise profile
    #     0 - disable
      "noiseProfile": None,
    #   <rangeAzimuthHeatMap>
    #     range-azimuth heat map related information
    #       1 - enable export of zero Doppler radar cube matrix, all range bins, all antennas to calculate and display azimuth heat map.
    #       0 - disable (the GUI computes the FFT of this to show heat map)
      "rangeAzimuthHeatMap": None,
    #   <rangeDopplerHeatMap>
    #     range-doppler heat map
    #       1 - enable export of the whole detection matrix. Note that the frame period should be adjusted according to UART transfer time.
    #       0 - disable
      "rangeDopplerHeatMap": None,
    #   <statsInfo>
    #     statistics (CPU load, margins, etc)
    #       1 - enable export of stats data.
    #       0 - disable
      "statsInfo": None,
    },
    # CFAR config message to datapath.
    # The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "cfarCfg": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <procDirection>
    #     Processing direction:
    #     0 - CFAR detection in range direction
    #     1 - CFAR detection in Doppler direction
      "procDirection": None,
    #   <mode>
    #     CFAR averaging mode:
    #     0 - CFAR_CA (Cell Averaging)
    #     1 - CFAR_CAGO (Cell Averaging Greatest Of)
    #     2 - CFAR_CASO (Cell Averaging Smallest Of)
      "mode": None,
    #   <noiseWin>
    #     noise averaging window length:
    #     Length of the noise averaged cells in samples
      "noiseWin": None,
    #   <guardLen>
    #     guard length in samples
      "guardLen": None,
    #   <divShift>
    #     Cumulative noise sum divisor expressed as a shift.
    #     Sum of noise samples is divided by 2^<divShift>.
    #     Based on platform, <mode> and <noiseWin> , this value should be set as shown in next columns.
    #     The value to be used here should match the "CFAR averaging mode" and the "noise averaging window length" that is selected above.
    #     The actual value that is used for division (2^x) is a power of 2, even though the "noise averaging window length" samples may not have that restriction.
      "divShift": None,
    #   cyclic mode or Wrapped around mode.
    #     0- Disabled
    #     1- Enabled
      "cyclicModeOrWrappedAroundMode": None,
    #   Threshold scale.
    #     This is used in conjuntion with the noise sum divisor (say x).
    #     the CUT comparison for log input is:
    #     CUT > Threshold scale + (noise sum / 2^x)
      "ThresholdScale": None,
    },
    # Peak grouping config message to datapath.
    # With peak grouping scheme enabled, instead of reporting a cluster of detected neighboring points, only one point, the highest one, will be reported, this reducing the total number of detected points per frame. 
    # Only the points between start and end range index are considered. 
    # Detected points falling outside this range are dropped and not shipped out as part of point cloud.
    # The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "peakGrouping": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <scheme>
    #     1 - MMW_PEAK_GROUPING_DET_MATRIX_BASED Peak grouping is based on peaks of the neighboring bins read from detection matrix. 
    #         CFAR detected peak is reported if it is greater than its neighbors, located in detection matrix.
    #     2 - MMW_PEAK_GROUPING_CFAR_PEAK_BASED Peak grouping is based on peaks of neighboring bins that are CFAR detected. 
    #         CFAR detected peak is reported if it is greater than its neighbors, located in the list of CFAR detected peaks.
    #     For more detailed look at mmw demo's doxygen documentation.
      "scheme": None,
    #   peak grouping in Range direction:
    #     0 - disabled
    #     1 - enabled
      "peakGroupingInRangeDirection": None,
    #   peak grouping in Doppler direction:
    #     0 - disabled
    #     1 - enabled
      "peakGroupingInDopplerDirection": None,
    #   Start Range Index 
    #     Minimum range index of detected object that should be sent out.
    #     Ex: Value of 1 means Skip 0th bin and start peak grouping from range bin#1
      "startRangeIndex": None,
    #   End Range Index 
    #     Maximum range index of detected object that should be sent out.
    #     Ex: Value of (Range FFT size -1) means skip last bin and stop peak grouping at (Range FFT size -1)
      "endRangeIndex": None,
    },
    # Multi Object Beamforming config message to datapath.
    # This feature allows radar to separate reflections from multiple objects originating from the same range/Doppler detection.
    # The procedure searches for the second peak after locating the highest peak in Azimuth FFT.
    # If the second peak is greater than the specified threshold, the second object with the same range/Doppler is appended to the list of detected objects.
    # The threshold is proportional to the height of the highest peak.
    # The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "multiObjBeamForming": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <Feature Enabled>
    #     0 - disabled
    #     1 - enabled
      "featureEnabled": None,
    #   <threshold>
    #     0 to 1 – threshold scale for the second peak detection in azimuth FFT output.
    #     Detection threshold is equal to <thresholdScale> multiplied by the first peak height.
    #     Note that FFT output is magnitude squared.
      "threshold": None,
    },
    # DC range calibration config message to datapath.
    # Antenna coupling signature dominates the range bins close to the radar.
    # These are the bins in the range FFT output located around DC.
    # When this feature is enabled, the signature is estimated during the first N chirps, and then it is subtracted during the subsequent chirps.
    # During the estimation period the specified bins (defined as [negativeBinIdx, positiveBinIdx]) around DC are accumulated and averaged.
    # It is assumed that no objects are present in the vicinity of the radar at that time.
    # This procedure is initiated by the following CLI command, and it can be initiated any time while radar is running.
    # Note that the maximum number of compensated bins is 32.
    # The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "calibDcRangeSig": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <enabled>
    #     Enable DC removal using first few chirps
    #       0 - disabled
    #       1 - enabled
      "enabled": None,
    #   <negativeBinIdx>
    #     negative Bin Index (to remove DC from farthest range bins)
    #     Maximum negative range FFT index to be included for compensation.
    #     Negative indices are indices wrapped around from far end of 1D FFT.
    #     Ex: Value of -5 means last 5 bins starting from the farthest bin
      "negativeBinIdx": None,
    #   <positiveBinIdx>
    #     positive Bin Index (to remove DC from closest range bins)
    #     Maximum positive range FFT index to be included for compensation
    #     Value of 8 means first 9 bins (including bin#0)
      "positiveBinIdx": None,
    #   <numAvg>
    #     number of chirps to average to collect DC signature (which will then be applied to all chirps beyond this).
    #     The value must be power of 2, and also in xWR14xx, it must be greater than the number of Doppler bins.
    #     Value of 256 means first 256 chirps (after command is issued and feature is enabled) will be used for collecting (averaging) DC signature in the bins specified above.
    #     From 257th chirp, the collected DC signature will be removed from every chirp.
      "numAvg": None,
    },
    # Velocity disambiguation config message to datapath.
    # A simple technique for velocity disambiguation is implemented.
    # It corrects target velocities up to (2*vmax).
    # Enabling this feature results in loss of multiObjBeamForming feature.
    # See mmW demo doxygen for xwr16xx for more details.
    # The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "extendedMaxVelocity": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <enabled>
    #     Enable velocity disambiguation technique
    #       0 - disabled
    #       1 - enabled
      "enabled": None,
    },
    # Static clutter removal config message to datapath.
    # Static clutter removal algorithm implemented by subtracting from the samples the mean value of the input samples to the 2D-FFT.
    # The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "clutterRemoval": {
    #   <enabled>
    #     Enable static clutter removal technique
    #       0 - disabled
    #       1 - enabled
      "enabled": None,
    },
    # Command for datapath to compensate for bias in the range estimation and receive channel gain and phase imperfections.
    # Refer to the procedure mentioned here The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "compRangeBiasAndRxChanPhase": {
    #   <rangeBias>
    #     Compensation for range estimation bias in meters supported supported
      "rangeBias": None,
    #   <Re(0,0)> <Im(0,0)> <Re(0,1)> <Im(0,1)> ... <Re(0,R-1)> <Im(0,R-1)> <Re(1,0)> <Im(1,0)> ... <Re(T-1,R-1)> <Im(T-1,R-1)>
    #     Set of Complex value representing compensation for virtual Rx channel phase bias in Q15 format.
    #     Pairs of I and Q should be provided for all Tx and Rx antennas in the device
      "setOfComplexValue": None,
    },
    # Command for datapath to enable the measurement of the range bias and receive channel gain and phase imperfections. 
    # Refer to the procedure mentioned here The values in this command can be changed between sensorStop and sensorStart and even when the sensor is running.
    # This is a mandatory command.
    "measureRangeBiasAndRxChanPhase": {
    #   <enabled>
    #     1 - enable measurement.
    #         This parameter should be enabled only using the profile_calibration.cfg profile in the mmW demo profiles directory
    #     0 - disable measurement.
    #         This should be the value to use for all other profiles.
      "enabled": None,
    #   <targetDistance>
    #     distance in meters where strong reflector is located to be used as test object for measurement. 
    #     This field is only used when measurement mode is enabled.
      "targetDistance": None,
    #   <searchWin>
    #     distance in meters of the search window around <targetDistance> where the peak will be searched
      "searchWin": None,
    },
    # OOB processing chain assumes that the object of interests are located in the far field so that the rays between the object and the multiple TX/RX antennas are parallel. 
    # However for very close by objects this assumption (of parallel lines) is not valid and can induce a significant phase error when processed using regular FFT techniques.
    # User can use this command to enable the near field correction algorithm.
    # See mmW demo doxygen for xwr16xx for more details.
    "nearFieldCfg": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <enabled>
    #     Enable near field correction
    #       0 - disabled
    #       1 - enabled
      "enabled": None,
    #   <startRangeIndex>
    #     This is the first range bin index at which the algorithm would start correcting
      "startRangeIndex": None,
    #   <endRangeIndex>
    #     This is the last range bin index beyond which the algorithm would stop correcting.
      "endRangeIndex": None,
    },
    # Rx Saturation Monitoring config message for Chirp quality to RadarSS and datapath.
    # See mmwavelink doxgen for details on rlRxSatMonConf_t.
    "CQRxSatMonitor": {
    # <profile>
    #   Valid profile Id for this monitoring configuraiton.
    #   This profile ID should have a matching profileCfg
      "profile": None,
    # <satMonSel>
    #   RX Saturation monitoring mode
      "satMonSel": None,
    # <priSliceDuration>
    #   Duration of each slice, 1LSB=0.16us, range: 4 - number of ADC samples
      "priSliceDuration": None,
    # <numSlices>
    #   primary + secondary slices , range 1-127.
    #   Maximum primary slice is 64.
      "numSlices": None,
    # <rxChanMask>
    #   RX channgel mask, 1 - Mask, 0 - unmask
      "rxChanMask": None,
    },
    # Signal and image band energy Monitoring config message for Chirp quality to RadarSS and datapath.
    # See mmwavelink doxgen for details on rlSigImgMonConf_t.
    # The enable/disable for this command is controlled via the "analogMonitor" CLI command
    "CQSigImgMonitor": {
    #   <profile>
    #     Valid profile Id for this monitoring configuraiton.
    #     This profile ID should have a matching profileCfg
      "profile": None,
    #   <numSlices>
    #     primary + secondary slices , range 1-127.
    #     Maximum primary slice is 64.
      "numSlices": None,
    #   <numSamplePerSlice>
    #     Possible range is 4 to "number of ADC samples" in the corresponding profileCfg.
    #     It must be an even number.
      "numSamplePerSlice": None,
    },
    # Controls the enable/disable of the various monitoring features supported in the demos.
    "analogMonitor": {
    #   <rxSaturation>
    #     CQRxSatMonitor enable/disable
    #       1:enable
    #       0: disable
      "rxSaturation": None,
    #   <sigImgBand>
    #     CQSigImgMonitor enable/disable
    #       1:enable
    #       0: disable
      "sigImgBand": None,
    },
    # Enables the streaming of various data streams over LVDS lanes (xWR16xx).
    "lvdsStreamCfg": {
    #   <subFrameIdx>
    #     subframe Index (exists only in xwr16xx mmW demo)
      "subFrameIdx": None,
    #   <enableHeader>
    #     0 - Disable HSI header for all active streams
    #     1 - Enable HSI header for all active streams
      "enableHeader": None,
    #   <dataFmt>
    #     Controls HW streaming.
    #     Specifies the HW streaming data format.
    #       0-HW STREAMING DISABLED
    #       1-ADC
    #       2-CP_ADC
    #       3-ADC_CP
    #       4-CP_ADC_CQ
      "dataFmt": None,
    #   <enableSW>
    #     0 - Disable user data (SW session)
    #     1 - Enable user data
      "enableSW": None,
    },
    # sensor Start command to RadarSS and datapath.
    # Starts the sensor. This function triggers the transmission of the frames as per the frame and chirp configuration.
    # By default, this function also sends the configuration to the mmWave Front End and the processing chain.
    # This is a mandatory command.
    "sensorStart": {
    #   Optionally, user can provide an argument 'doReconfig'
    #     1 - Do full reconfiguration of the device
    #     0 - Skip reconfiguration and just start the sensor using already provided configuration.
      "doReconfig": None,
    },
    # sensor Stop command to RadarSS and datapath.
    # Stops the sensor.
    # If the sensor is running, it will stop the mmWave Front End and the processing chain.
    # After the command is acknowledged, a new config can be provided and sensor can be restarted or sensor can be restarted without a new config (i.e. using old config).
    # See 'sensorStart' command.
    # This is mandatory before any reconfiguration is performed post sensorStart.
    "sensorStop": {},
    # This command should be issued after 'sensorStop' command to flush the old configuration and provide a new one.
    # This is mandatory before any reconfiguration is performed post sensorStart.
    "flushCfg": {},
  }

  configParameters: dict[str, None] = {
    "numDopplerBins": None, 
    "numRangeBins": None, 
    "rangeResolutionMeters": None, 
    "rangeIdxToMeters": None, 
    "dopplerResolutionMps": None, 
    "maxRange": None, 
    "maxVelocity": None, 
  }

  def __init__(self, platform: str):
    logger_parse = Log.Logger(fileName="Configuration_2_1_0-parse.log")
    if platform == "xWR1443":
      self.platform = platform

  def set(self, command: str, parameters: str, value):
    self.cfg[command][parameters] = value
  def get(self, command: str, parameters: str):
    return self.cfg[command][parameters]
  
  def parse_commandParameters_1443(self, command: str):
    try:
      units: list[str] = command.split(' ')
      if units[0] == "dfeDataOutputMode": 
        self.commandParameters["dfeDataOutputMode"]["modeType"] = int(units[1])
      if units[0] == "channelCfg": 
        self.commandParameters["channelCfg"]["rxChannelEn"] = int(units[1])
        self.commandParameters["channelCfg"]["txChannelEn"] = int(units[2])
        self.commandParameters["channelCfg"]["cascading"] = int(units[3])
      if units[0] == "adcCfg": 
        self.commandParameters["adcCfg"]["numADCBits"] = int(units[1])
        self.commandParameters["adcCfg"]["adcOutputFmt"] = int(units[2])
      if units[0] == "adcbufCfg": 
        # self.commandParameters["adcbufCfg"]["subFrameIdx"] = None
        self.commandParameters["adcbufCfg"]["adcOutputFmt"] = int(units[1])
        self.commandParameters["adcbufCfg"]["SampleSwap"] = int(units[2])
        self.commandParameters["adcbufCfg"]["ChanInterleave"] = int(units[3])
        self.commandParameters["adcbufCfg"]["ChirpThreshold"] = int(units[4])
      if units[0] == "profileCfg": 
        self.commandParameters["profileCfg"]["profileId"] = int(units[1])
        self.commandParameters["profileCfg"]["startFreq"] = float(units[2])
        self.commandParameters["profileCfg"]["idleTime"] = float(units[3])
        self.commandParameters["profileCfg"]["adcStartTime"] = float(units[4])
        self.commandParameters["profileCfg"]["rampEndTime"] = float(units[5])
        self.commandParameters["profileCfg"]["txOutPower"] = int(units[6])
        self.commandParameters["profileCfg"]["txPhaseShifter"] = int(units[7])
        self.commandParameters["profileCfg"]["freqSlopeConst"] = float(units[8])
        self.commandParameters["profileCfg"]["txStartTime"] = float(units[9])
        self.commandParameters["profileCfg"]["numAdcSamples"] = int(units[10])
        self.commandParameters["profileCfg"]["digOutSampleRate"] = int(units[11])
        self.commandParameters["profileCfg"]["hpfCornerFreq1"] = int(units[12])
        self.commandParameters["profileCfg"]["hpfCornerFreq2"] = int(units[13])
        self.commandParameters["profileCfg"]["rxGain"] = int(units[14])
      if units[0] == "chirpCfg": 
        self.commandParameters["chirpCfg"]["chirpStartIndex"] = int(units[1])
        self.commandParameters["chirpCfg"]["chirpEndIndex"] = int(units[2])
        self.commandParameters["chirpCfg"]["profileIdentifier"] = float(units[3])
        self.commandParameters["chirpCfg"]["startFrequencyVariation"] = int(units[4])
        self.commandParameters["chirpCfg"]["frequencySlopeVariation"] = float(units[5])
        self.commandParameters["chirpCfg"]["idleTimeVariation"] = float(units[5])
        self.commandParameters["chirpCfg"]["adcStartTimeVariation"] = float(units[6])
        self.commandParameters["chirpCfg"]["txAntennaEnableMask"] = int(units[7])
      # if units[0] == "bpmCfg": 
      #   self.commandParameters["bpmCfg"]["subFrameIdx"] = None
      #   self.commandParameters["bpmCfg"]["enabled"] = None
      #   self.commandParameters["bpmCfg"]["chirp0Idx"] = None
      #   self.commandParameters["bpmCfg"]["chirp1Idx"] = None
      if units[0] == "lowPower": 
        self.commandParameters["lowPower"]["dontCare"] = int(units[1])
        self.commandParameters["lowPower"]["adcMode"] = int(units[2])
      if units[0] == "frameCfg": 
        self.commandParameters["frameCfg"]["chirpStartIndex"] = int(units[1])
        self.commandParameters["frameCfg"]["chirpEndIndex"] = int(units[2])
        self.commandParameters["frameCfg"]["numberOfLoops"] = int(units[3])
        self.commandParameters["frameCfg"]["numberOfFrames"] = int(units[4])
        self.commandParameters["frameCfg"]["framePeriodicity"] = float(units[5])
        self.commandParameters["frameCfg"]["triggerSelect"] = int(units[6])
        self.commandParameters["frameCfg"]["frameTriggerDelay"] = float(units[7])
      if units[0] == "advFrameCfg": 
        self.commandParameters["advFrameCfg"]["numOfSubFrames"] = int(units[1])
        self.commandParameters["advFrameCfg"]["forceProfile"] = int(units[2])
        self.commandParameters["advFrameCfg"]["numFrames"] = int(units[3])
        self.commandParameters["advFrameCfg"]["triggerSelect"] = int(units[4])
        self.commandParameters["advFrameCfg"]["frameTrigDelay"] = float(units[5])
      if units[0] == "subFrameCfg": 
        self.commandParameters["subFrameCfg"]["subFrameNum"] = int(units[1])
        self.commandParameters["subFrameCfg"]["forceProfileIdx"] = int(units[2])
        self.commandParameters["subFrameCfg"]["chirpStartIdx"] = int(units[3])
        self.commandParameters["subFrameCfg"]["numOfChirps"] = int(units[4])
        self.commandParameters["subFrameCfg"]["numLoops"] = int(units[5])
        self.commandParameters["subFrameCfg"]["burstPeriodicity"] = float(units[6])
        self.commandParameters["subFrameCfg"]["chirpStartIdxOffset"] = int(units[7])
        self.commandParameters["subFrameCfg"]["numOfBurst"] = int(units[8])
        self.commandParameters["subFrameCfg"]["numOfBurstLoops"] = int(units[9])
        self.commandParameters["subFrameCfg"]["subFramePeriodicity"] = float(units[10])
      if units[0] == "guiMonitor": 
        # self.commandParameters["guiMonitor"]["subFrameIdx"] = None
        self.commandParameters["guiMonitor"]["detectedObjects"] = int(units[1])
        self.commandParameters["guiMonitor"]["logMagnitudeRange"] = int(units[2])
        self.commandParameters["guiMonitor"]["noiseProfile"] = int(units[3])
        self.commandParameters["guiMonitor"]["rangeAzimuthHeatMap"] = int(units[4])
        self.commandParameters["guiMonitor"]["rangeDopplerHeatMap"] = int(units[5])
        self.commandParameters["guiMonitor"]["statsInfo"] = int(units[6])
      if units[0] == "cfarCfg": 
        # self.commandParameters["cfarCfg"]["subFrameIdx"] = None
        self.commandParameters["cfarCfg"]["procDirection"] = int(units[1])
        self.commandParameters["cfarCfg"]["mode"] = int(units[2])
        self.commandParameters["cfarCfg"]["noiseWin"] = int(units[3])
        self.commandParameters["cfarCfg"]["guardLen"] = int(units[4])
        self.commandParameters["cfarCfg"]["divShift"] = int(units[5])
        self.commandParameters["cfarCfg"]["cyclicModeOrWrappedAroundMode"] = int(units[6])
        self.commandParameters["cfarCfg"]["ThresholdScale"] = int(units[7])
      if units[0] == "peakGrouping": 
        # self.commandParameters["peakGrouping"]["subFrameIdx"] = None
        self.commandParameters["peakGrouping"]["scheme"] = int(units[2])
        self.commandParameters["peakGrouping"]["peakGroupingInRangeDirection"] = int(units[3])
        self.commandParameters["peakGrouping"]["peakGroupingInDopplerDirection"] = int(units[4])
        self.commandParameters["peakGrouping"]["startRangeIndex"] = int(units[5])
        self.commandParameters["peakGrouping"]["endRangeIndex"] = int(units[6])
      if units[0] == "multiObjBeamForming": 
        # self.commandParameters["multiObjBeamForming"]["subFrameIdx"] = None
        self.commandParameters["multiObjBeamForming"]["featureEnabled"] = int(units[1])
        self.commandParameters["multiObjBeamForming"]["threshold"] = int(units[2])
      if units[0] == "calibDcRangeSig": 
        # self.commandParameters["calibDcRangeSig"]["subFrameIdx"] = None
        self.commandParameters["calibDcRangeSig"]["enabled"] = int(units[1])
        self.commandParameters["calibDcRangeSig"]["negativeBinIdx"] = int(units[2])
        self.commandParameters["calibDcRangeSig"]["positiveBinIdx"] = int(units[3])
        self.commandParameters["calibDcRangeSig"]["numAvg"] = int(units[4])
      if units[0] == "extendedMaxVelocity": 
        # self.commandParameters["extendedMaxVelocity"]["subFrameIdx"] = None
        self.commandParameters["extendedMaxVelocity"]["enabled"] = int(units[1])
      if units[0] == "clutterRemoval": 
        self.commandParameters["clutterRemoval"]["enabled"] = int(units[1])
      if units[0] == "compRangeBiasAndRxChanPhase": 
        self.commandParameters["compRangeBiasAndRxChanPhase"]["rangeBias"] = int(units[1])
        self.commandParameters["compRangeBiasAndRxChanPhase"]["setOfComplexValue"] = [int(value) for value in units[2:]]
      if units[0] == "measureRangeBiasAndRxChanPhase": 
        self.commandParameters["measureRangeBiasAndRxChanPhase"]["enabled"] = int(units[1])
        self.commandParameters["measureRangeBiasAndRxChanPhase"]["targetDistance"] = int(units[2])
        self.commandParameters["measureRangeBiasAndRxChanPhase"]["searchWin"] = int(units[3])
      if units[0] == "nearFieldCfg": 
        # self.commandParameters["nearFieldCfg"]["subFrameIdx"] = None
        self.commandParameters["nearFieldCfg"]["enabled"] = int(units[1])
        self.commandParameters["nearFieldCfg"]["startRangeIndex"] = int(units[2])
        self.commandParameters["nearFieldCfg"]["endRangeIndex"] = int(units[3])
      if units[0] == "CQRxSatMonitor": 
        self.commandParameters["CQRxSatMonitor"]["profile"] = int(units[1])
        self.commandParameters["CQRxSatMonitor"]["satMonSel"] = int(units[2])
        self.commandParameters["CQRxSatMonitor"]["priSliceDuration"] = int(units[3])
        self.commandParameters["CQRxSatMonitor"]["numSlices"] = int(units[4])
        self.commandParameters["CQRxSatMonitor"]["rxChanMask"] = int(units[5])
      if units[0] == "CQSigImgMonitor": 
        self.commandParameters["CQSigImgMonitor"]["profile"] = int(units[1])
        self.commandParameters["CQSigImgMonitor"]["numSlices"] = int(units[2])
        self.commandParameters["CQSigImgMonitor"]["numSamplePerSlice"] = int(units[3])
      if units[0] == "analogMonitor": 
        self.commandParameters["analogMonitor"]["rxSaturation"] = int(units[1])
        self.commandParameters["analogMonitor"]["sigImgBand"] = int(units[2])
      if units[0] == "lvdsStreamCfg": 
        # self.commandParameters["lvdsStreamCfg"]["subFrameIdx"] = None
        self.commandParameters["lvdsStreamCfg"]["enableHeader"] = int(units[1])
        self.commandParameters["lvdsStreamCfg"]["dataFmt"] = int(units[2])
        self.commandParameters["lvdsStreamCfg"]["enableSW"] = int(units[3])
      if units[0] == "sensorStart": 
        self.commandParameters["sensorStart"]["doReconfig"] = int(units[1])
        pass
      if units[0] == "sensorStop": 
        pass
      if units[0] == "flushCfg": 
        pass
    except: 
      self.logger_parse.log(message="Parse error from: " + str(command))

  def parse_configParameters_1443(self):

    def decode_mask(mask: int) -> int:
      value = 0
      while mask :
        mask >>= 1
        value += 1
      return value
    
    self.configParameters["numRxAnt"] = decode_mask(mask=int(self.commandParameters["channelCfg"]["rxChannelEn"]))
    self.configParameters["numTxAnt"] = decode_mask(mask=int(self.commandParameters["channelCfg"]["txChannelEn"]))
    self.configParameters["numVirtualAntennas"] = self.configParameters["numRxAnt"] * self.configParameters["numTxAnt"]

    startFreq = self.commandParameters["profileCfg"]["startFreq"]
    idleTime = self.commandParameters["profileCfg"]["idleTime"]
    rampEndTime = self.commandParameters["profileCfg"]["rampEndTime"]
    freqSlopeConst = self.commandParameters["profileCfg"]["freqSlopeConst"]
    numAdcSamples = self.commandParameters["profileCfg"]["numAdcSamples"]
    numAdcSamplesRoundTo2 = 1
    while numAdcSamples > numAdcSamplesRoundTo2: numAdcSamplesRoundTo2 = numAdcSamplesRoundTo2 << 1
    digOutSampleRate = self.commandParameters["profileCfg"]["digOutSampleRate"]

    chirpStartIdx = self.commandParameters["frameCfg"]["chirpStartIndex"]
    chirpEndIdx = self.commandParameters["frameCfg"]["chirpEndIndex"]
    numLoops = self.commandParameters["frameCfg"]["numberOfLoops"]
    numFrames = self.commandParameters["frameCfg"]["numberOfFrames"]
    self.configParameters["framePeriodicity"] = self.commandParameters["frameCfg"]["framePeriodicity"]
    numChirpsPerFrame = (chirpEndIdx - chirpStartIdx + 1) * numLoops

    self.configParameters["numDopplerBins"] = numChirpsPerFrame / self.configParameters["numTxAnt"]
    self.configParameters["numRangeBins"] = numAdcSamplesRoundTo2
    self.configParameters["rangeResolutionMeters"] = (3e8 * digOutSampleRate * 1e3) / (2 * freqSlopeConst * 1e12 * numAdcSamples)
    self.configParameters["rangeIdxToMeters"] = (3e8 * digOutSampleRate * 1e3) / (2 * freqSlopeConst * 1e12 * self.configParameters["numRangeBins"])
    self.configParameters["dopplerResolutionMps"] = 3e8 / (2 * startFreq * 1e9 * (idleTime + rampEndTime) * 1e-6 * self.configParameters["numDopplerBins"] * self.configParameters["numTxAnt"])
    self.configParameters["maxRange"] = (300 * 0.9 * digOutSampleRate)/(2 * freqSlopeConst * 1e3)
    self.configParameters["maxVelocity"] = 3e8 / (4 * startFreq * 1e9 * (idleTime + rampEndTime) * 1e-6 * self.configParameters["numTxAnt"])

    self.configParameters["thresholdScaleDb"] = (self.commandParameters["cfarCfg"]["ThresholdScale"] * 6 * 2**math.ceil(math.log2(self.configParameters["numVirtualAntennas"]))) // (512 * self.configParameters["numVirtualAntennas"])

  def calc_CfarRangeThreshold_dB_1443(self, threshold_dB):
    if threshold_dB<0 or threshold_dB>100: 
      return self.commandParameters["cfarCfg"]["ThresholdScale"]
    return (threshold_dB * 512 * self.configParameters["numVirtualAntennas"]) // (6 * 2**math.ceil(math.log2(self.configParameters["numVirtualAntennas"])))
  
  def command_CfarRangeThreshold_dB_1443(self, threshold_dB) -> str:
    self.commandParameters["cfarCfg"]["ThresholdScale"] = self.calc_CfarRangeThreshold_dB_1443(threshold_dB)
    return ' '.join(["cfarCfg", 
            str(self.commandParameters["cfarCfg"]["procDirection"]), 
            str(self.commandParameters["cfarCfg"]["mode"]), 
            str(self.commandParameters["cfarCfg"]["noiseWin"]), 
            str(self.commandParameters["cfarCfg"]["guardLen"]), 
            str(self.commandParameters["cfarCfg"]["divShift"]), 
            str(self.commandParameters["cfarCfg"]["cyclicModeOrWrappedAroundMode"]), 
            str(self.commandParameters["cfarCfg"]["ThresholdScale"])
            ])
  
  def command_RemoveStaticClutter(self, enabled: bool = True) -> str:
    self.commandParameters["clutterRemoval"]["enabled"] = int(enabled)
    return ' '.join(["clutterRemoval", str(self.commandParameters["clutterRemoval"]["enabled"])])
