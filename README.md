# Preface #

This document describes the functionality provided by the xlr-rational-team-concert-plugin.

See the **[XL Release Documentation](https://docs.xebialabs.com/xl-release/index.html)** for background information on XL Release and release concepts.

# Overview #

The xlr-rational-team-concert-plugin is an XL Release plugin that allows you to:
  * programmatically update Rational Team Concert Workitems


## Tasks ##
+ Update Workitem Status
  * `rtcServer`: The CI created to connect to your Rational Team Concert Jazz Team Server (`CI`) 
  * `rtcProject`: The Rational Team Concert project to interact with (`string`)
  * `workItemID`: The ID of the work item to update (`string`)
  * `updateComment`: The comment associated with this update (`string`)

## Usage ##

This plugin interacts with a JazzTeamServer instance, therefore the first thing you need to do is create a Configuration Item in XL Release to connect to that instance.  This is done in the Configuration screen of XL Release.

Once done you can add a task (listed above) to your release template and complete the fields.

## Notes and Tips ##

For experimentation with Rational Team Concert IBM kindly provide a sandpit environment from this location - https://jazz.net/products/sandbox/  You can then use any instances you create with this plugin.
