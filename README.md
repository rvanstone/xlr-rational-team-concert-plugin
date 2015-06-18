# Preface #

This document describes the functionality provided by the xlr-rational-team-concert-plugin.

See the **[XL Release Documentation](https://docs.xebialabs.com/xl-release/index.html)** for background information on XL Release and release concepts.

# Overview #

The xlr-rational-team-concert-plugin is an XL Release plugin that allows you to:
  * programmatically update Rational Team Concert Workitems

For XL Release version 4.5.x you'll need at least version 1.5 of the plugin.

## Tasks ##
+ Update Workitem Status
  * `rtcServer`: The CI created to connect to your Rational Team Concert Jazz Team Server (`CI`) 
  * `rtcProject`: The Rational Team Concert project to interact with (`string`)
  * `workItemID`: The ID of the work item to update (`string`)
  * `rtcComment`: The comment associated with this update (`string`)
