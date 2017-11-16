from ixnetwork.IxnEmulationHost import IxnEmulationHost

class IxnIPv4PseudoNodeRoutesEmulation(IxnEmulationHost):
    """Generated NGPF IPv4PseudoNodeRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnIPv4PseudoNodeRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific IPv4PseudoNodeRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ipv4Metric: href
                ipv4RouteOrigin: href
                ipv4Redistribution: href
                ipv4RFlag: href
                ipv4NFlag: href
                ipv4PFlag: href
                ipv4EFlag: href
                ipv4VFlag: href
                ipv4LFlag: href
                algorithm: href
                configureSIDIndexLabel: href
                sIDIndexLabel: href
                active: href
                networkAddress: href
                rangeSize: href
                prefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIPv4PseudoNodeRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","isisL3PseudoRouter","IPv4PseudoNodeRoutes"], vport_name, emulation_host, filters)


class IxnIPv6PseudoNodeRoutesEmulation(IxnEmulationHost):
    """Generated NGPF IPv6PseudoNodeRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnIPv6PseudoNodeRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific IPv6PseudoNodeRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ipv6Metric: href
                ipv6RouteOrigin: href
                ipv6Redistribution: href
                ipv6RFlag: href
                ipv6NFlag: href
                ipv6PFlag: href
                ipv6EFlag: href
                ipv6VFlag: href
                ipv6LFlag: href
                algorithm: href
                configureSIDIndexLabel: href
                sIDIndexLabel: href
                ipv6Srh: href
                active: href
                networkAddress: href
                rangeSize: href
                prefix: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIPv6PseudoNodeRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","isisL3PseudoRouter","IPv6PseudoNodeRoutes"], vport_name, emulation_host, filters)


class IxnIPv6SegmentsListEmulation(IxnEmulationHost):
    """Generated NGPF IPv6SegmentsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIPv6SegmentsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific IPv6SegmentsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                sIDEnable: href
                sID: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIPv6SegmentsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","ipv6sr","IPv6SegmentsList"], vport_name, emulation_host, filters)


class IxnOFSwitchChannelEmulation(IxnEmulationHost):
    """Generated NGPF OFSwitchChannel emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOFSwitchChannelEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific OFSwitchChannel emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                switchName: string
                localIp: list
                remoteIp: href
                datapathId: href
                datapathIdHex: href
                auxConnectionsPerChannel: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOFSwitchChannelEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch","OFSwitchChannel"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOFSwitchChannelEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOFSwitchChannelEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOFSwitchChannelEmulation, self).call_operation('stop', expected_state, timeout)


class IxnActionEmulation(IxnEmulationHost):
    """Generated NGPF action emulation host """


    def __init__(self, ixnhttp):
        super(IxnActionEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific action emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnActionEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","packetOutActionProfile","actionList","action"], vport_name, emulation_host, filters)


class IxnActionListEmulation(IxnEmulationHost):
    """Generated NGPF actionList emulation host """


    def __init__(self, ixnhttp):
        super(IxnActionListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific actionList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                listCount: number
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnActionListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","packetOutActionProfile","actionList"], vport_name, emulation_host, filters)


class IxnActionsEmulation(IxnEmulationHost):
    """Generated NGPF actions emulation host """


    def __init__(self, ixnhttp):
        super(IxnActionsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific actions emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnActionsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","tables","flowSet","flowProfile","matchAction","instructions","instruction","actions"], vport_name, emulation_host, filters)


class IxnActionsProfileEmulation(IxnEmulationHost):
    """Generated NGPF actionsProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnActionsProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific actionsProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnActionsProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","groups","buckets","actionsProfile"], vport_name, emulation_host, filters)


class IxnAncpEmulation(IxnEmulationHost):
    """Generated NGPF ancp emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnAncpEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ancp emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                standard: href
                nasIp: href
                nasServicePort: href
                triggerAccessLoopEvents: href
                keepAliveTimeout: href
                keepAliveRetries: href
                partitionId: href
                dynamicTopologyDiscovery: href
                lineConfiguration: href
                remoteLoopback: href
                transactionalMulticast: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnAncpEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ancp"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnAncpEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendrstack(self, expected_state=None, timeout=None):
        """Send RSTACK from selected Access Node.
            For expected_state options see the class state variables
        """
        super(IxnAncpEmulation, self).call_operation('sendRstack', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnAncpEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnAncpEmulation, self).call_operation('stop', expected_state, timeout)


class IxnAsyncConfStatLearnedInfoEmulation(IxnEmulationHost):
    """Generated NGPF asyncConfStatLearnedInfo emulation host """


    def __init__(self, ixnhttp):
        super(IxnAsyncConfStatLearnedInfoEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific asyncConfStatLearnedInfo emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnAsyncConfStatLearnedInfoEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","asyncConfStatLearnedInfo"], vport_name, emulation_host, filters)


class IxnAuxiliaryConnectionListEmulation(IxnEmulationHost):
    """Generated NGPF auxiliaryConnectionList emulation host """


    def __init__(self, ixnhttp):
        super(IxnAuxiliaryConnectionListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific auxiliaryConnectionList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                channelName: string
                active: href
                auxId: href
                connectionType: href
                uDPSrcPortNum: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnAuxiliaryConnectionListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch","OFSwitchChannel","auxiliaryConnectionList"], vport_name, emulation_host, filters)


class IxnBackupLspEROSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF backupLspEROSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBackupLspEROSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific backupLspEROSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                type: href
                ip: href
                prefixLength: href
                asNumber: href
                looseFlag: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBackupLspEROSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2PIngressLsps","backupLspEROSubObjectsList"], vport_name, emulation_host, filters)


class IxnBandsEmulation(IxnEmulationHost):
    """Generated NGPF bands emulation host """


    def __init__(self, ixnhttp):
        super(IxnBandsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bands emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                multiplier: number
                meterIndex: list
                bandDescription: href
                rate: href
                burstSize: href
                bandType: href
                precedenceLevel: href
                experimenter: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBandsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","meters","bands"], vport_name, emulation_host, filters)


class IxnBaseVidListEmulation(IxnEmulationHost):
    """Generated NGPF baseVidList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBaseVidListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific baseVidList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                baseVid: href
                baseVlanPriority: href
                bvlanTpid: href
                ectAlgorithm: href
                bmacSameAsSystemId: href
                bmac: href
                useFlagBit: href
                isidCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBaseVidListEmulation, self).find(["topology","deviceGroup","isisSpbRouter","spbTopologyList","baseVidList"], vport_name, emulation_host, filters)


class IxnBfdRouterEmulation(IxnEmulationHost):
    """Generated NGPF bfdRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBfdRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bfdRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                localRouterId: list
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBfdRouterEmulation, self).find(["topology","deviceGroup","bfdRouter"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBfdRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBfdRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBfdRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBfdv4InterfaceEmulation(IxnEmulationHost):
    """Generated NGPF bfdv4Interface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBfdv4InterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bfdv4Interface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                sourceIp4: href
                localRouterId: list
                noOfSessions: number
                aggregateBfdSession: bool
                vni: list
                minRxInterval: href
                txInterval: href
                echoRxInterval: href
                echoTxInterval: href
                echoTimeOut: href
                configureEchoSourceIp: href
                enableDemandMode: href
                enableControlPlaneIndependent: href
                pollInterval: href
                timeoutMultiplier: href
                flapTxIntervals: href
                ipDiffServ: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBfdv4InterfaceEmulation, self).find(["topology","deviceGroup","ipv4Loopback","bfdv4Interface"], vport_name, emulation_host, filters)

    def clearlearnedinfo(self, expected_state=None, timeout=None):
        """Clear Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBfdv4InterfaceEmulation, self).call_operation('clearLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBfdv4InterfaceEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBfdv4InterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate Interface
            For expected_state options see the class state variables
        """
        super(IxnBfdv4InterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Interface
            For expected_state options see the class state variables
        """
        super(IxnBfdv4InterfaceEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBfdv4SessionEmulation(IxnEmulationHost):
    """Generated NGPF bfdv4Session emulation host """

    STATE_ADMINDOWN = 'adminDown'
    STATE_AWAITINGIP = 'awaitingIp'
    STATE_DOWN = 'down'
    STATE_INIT = 'init'
    STATE_MAXSTATE = 'maxState'
    STATE_SESSDELETED = 'sessDeleted'
    STATE_UNKNOWNSTATE = 'unknownState'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBfdv4SessionEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bfdv4Session emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                sourceIp4: href
                remoteIp4: href
                learnedRemoteIP: list
                ipTTL: href
                localRouterId: list
                vni: list
                sessionType: href
                enableAutoChooseSourceIp: href
                enableOVSDBCommunication: href
                remoteMac: href
                learnedRemoteMac: list
                myDiscriminator: href
                enableRemoteDiscriminatorLearned: href
                remoteDiscriminator: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBfdv4SessionEmulation, self).find(["topology","deviceGroup","ipv4Loopback","bfdv4Interface","bfdv4Session"], vport_name, emulation_host, filters)

    def start(self, expected_state=None, timeout=None):
        """Activate Session
            For expected_state options see the class state variables
        """
        super(IxnBfdv4SessionEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Session
            For expected_state options see the class state variables
        """
        super(IxnBfdv4SessionEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBfdv6InterfaceEmulation(IxnEmulationHost):
    """Generated NGPF bfdv6Interface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBfdv6InterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bfdv6Interface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                sourceIp6: href
                localRouterId: list
                noOfSessions: number
                aggregateBfdSession: bool
                vni: list
                minRxInterval: href
                txInterval: href
                echoRxInterval: href
                echoTxInterval: href
                echoTimeOut: href
                configureEchoSourceIp: href
                enableDemandMode: href
                enableControlPlaneIndependent: href
                pollInterval: href
                timeoutMultiplier: href
                flapTxIntervals: href
                ipDiffServ: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBfdv6InterfaceEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","bfdv6Interface"], vport_name, emulation_host, filters)

    def clearlearnedinfo(self, expected_state=None, timeout=None):
        """Clear Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBfdv6InterfaceEmulation, self).call_operation('clearLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBfdv6InterfaceEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBfdv6InterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate Interface
            For expected_state options see the class state variables
        """
        super(IxnBfdv6InterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Interface
            For expected_state options see the class state variables
        """
        super(IxnBfdv6InterfaceEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBfdv6SessionEmulation(IxnEmulationHost):
    """Generated NGPF bfdv6Session emulation host """

    STATE_ADMINDOWN = 'adminDown'
    STATE_AWAITINGIP = 'awaitingIp'
    STATE_DOWN = 'down'
    STATE_INIT = 'init'
    STATE_MAXSTATE = 'maxState'
    STATE_SESSDELETED = 'sessDeleted'
    STATE_UNKNOWNSTATE = 'unknownState'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBfdv6SessionEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bfdv6Session emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                sourceIp6: href
                remoteIp6: href
                localRouterId: list
                vni: list
                sessionType: href
                enableAutoChooseSourceIp: href
                enableOVSDBCommunication: href
                remoteMac: href
                learnedRemoteMac: list
                myDiscriminator: href
                enableRemoteDiscriminatorLearned: href
                remoteDiscriminator: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBfdv6SessionEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","bfdv6Interface","bfdv6Session"], vport_name, emulation_host, filters)

    def start(self, expected_state=None, timeout=None):
        """Activate Session
            For expected_state options see the class state variables
        """
        super(IxnBfdv6SessionEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Session
            For expected_state options see the class state variables
        """
        super(IxnBfdv6SessionEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpAigpListEmulation(IxnEmulationHost):
    """Generated NGPF bgpAigpList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpAigpListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpAigpList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                type: href
                value: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpAigpListEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpIPRouteProperty","bgpAigpList"], vport_name, emulation_host, filters)


class IxnBgpAsNumberListEmulation(IxnEmulationHost):
    """Generated NGPF bgpAsNumberList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpAsNumberListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpAsNumberList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableASNumber: href
                asNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpAsNumberListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpEthernetSegmentV6","bgpAsPathSegmentList","bgpAsNumberList"], vport_name, emulation_host, filters)


class IxnBgpAsPathSegmentListEmulation(IxnEmulationHost):
    """Generated NGPF bgpAsPathSegmentList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpAsPathSegmentListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpAsPathSegmentList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableASPathSegment: href
                segmentType: href
                numberOfAsNumberInSegment: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpAsPathSegmentListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpEthernetSegmentV6","bgpAsPathSegmentList"], vport_name, emulation_host, filters)


class IxnBgpClusterIdListEmulation(IxnEmulationHost):
    """Generated NGPF bgpClusterIdList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpClusterIdListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpClusterIdList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                clusterId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpClusterIdListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpEthernetSegmentV6","bgpClusterIdList"], vport_name, emulation_host, filters)


class IxnBgpCommunitiesListEmulation(IxnEmulationHost):
    """Generated NGPF bgpCommunitiesList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpCommunitiesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpCommunitiesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                type: href
                asNumber: href
                lastTwoOctets: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpCommunitiesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpEthernetSegmentV6","bgpCommunitiesList"], vport_name, emulation_host, filters)


class IxnBgpEthernetSegmentV4Emulation(IxnEmulationHost):
    """Generated NGPF bgpEthernetSegmentV4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpEthernetSegmentV4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpEthernetSegmentV4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                noOfbMacMappedIpsV4: number
                esiType: href
                esiValue: href
                bMacPrefix: href
                bMacPrefixLength: href
                useSameSequenceNumber: href
                includeMacMobilityExtendedCommunity: href
                supportMultihomedEsAutoDiscovery: href
                autoConfigureEsImport: href
                esImport: href
                dfElectionTimer: href
                supportFastConvergence: href
                enableSingleActive: href
                esiLabel: href
                advertiseAliasingAutomatically: href
                AdvertiseAliasingBeforeAdPerEsRoute: href
                AliasingRouteGranularity: href
                AdvertiseInclusiveMulticastRoute: href
                evisCount: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                useControlWord: bool
                enableStickyStaticFlag: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpEthernetSegmentV4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpEthernetSegmentV4"], vport_name, emulation_host, filters)


class IxnBgpEthernetSegmentV6Emulation(IxnEmulationHost):
    """Generated NGPF bgpEthernetSegmentV6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpEthernetSegmentV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpEthernetSegmentV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                noOfbMacMappedIpsV6: number
                esiType: href
                esiValue: href
                bMacPrefix: href
                bMacPrefixLength: href
                useSameSequenceNumber: href
                includeMacMobilityExtendedCommunity: href
                supportMultihomedEsAutoDiscovery: href
                autoConfigureEsImport: href
                esImport: href
                dfElectionTimer: href
                supportFastConvergence: href
                enableSingleActive: href
                esiLabel: href
                advertiseAliasingAutomatically: href
                AdvertiseAliasingBeforeAdPerEsRoute: href
                AliasingRouteGranularity: href
                AdvertiseInclusiveMulticastRoute: href
                evisCount: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                useControlWord: bool
                enableStickyStaticFlag: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpEthernetSegmentV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpEthernetSegmentV6"], vport_name, emulation_host, filters)


class IxnBgpExportRouteTargetListEmulation(IxnEmulationHost):
    """Generated NGPF bgpExportRouteTargetList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpExportRouteTargetListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpExportRouteTargetList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                targetType: href
                targetAsNumber: href
                targetIpAddress: href
                targetAs4Number: href
                targetAssignedNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpExportRouteTargetListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnEvi","bgpExportRouteTargetList"], vport_name, emulation_host, filters)


class IxnBgpExtendedCommunitiesListEmulation(IxnEmulationHost):
    """Generated NGPF bgpExtendedCommunitiesList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpExtendedCommunitiesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpExtendedCommunitiesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                type: href
                subType: href
                asNumber2Bytes: href
                assignedNumber4Bytes: href
                ip: href
                asNumber4Bytes: href
                assignedNumber2Bytes: href
                opaqueData: href
                colorCOBits: href
                colorReservedBits: href
                colorValue: href
                linkBandwidth: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpExtendedCommunitiesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpEthernetSegmentV6","bgpExtendedCommunitiesList"], vport_name, emulation_host, filters)


class IxnBgpFlowSpecRangesListEmulation(IxnEmulationHost):
    """Generated NGPF bgpFlowSpecRangesList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpFlowSpecRangesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpFlowSpecRangesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableDestPrefixV6: href
                destPrefixV6: href
                destPrefixLengthV6: href
                destPrefixOffset: href
                enableSourcePrefixV6: href
                sourcePrefixV6: href
                sourcePrefixLengthV6: href
                srcPrefixOffset: href
                nextHeader: href
                flowLabel: href
                fragmentMatchV6: href
                ip: href
                redirectnexthop: href
                enableReirectIPv6: href
                redirectIPv6: href
                flowSpecName: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                numberOfFlows: href
                portMatch: href
                destPortMatch: href
                sourcePortMatch: href
                icmpTypeMatch: href
                icmpCodeMatch: href
                tcpFlagsMatch: href
                ipPacketLenMatch: href
                dscpMatch: href
                enableTrafficRate: href
                trafficRate: href
                enableTrafficAction: href
                terminalAction: href
                trafficActionSample: href
                enableRedirect: href
                enableRedirect: href
                asNumber2Bytes: href
                asNumber4Bytes: href
                ip: href
                redirectnexthop: href
                assignedNumber2Bytes: href
                assignedNumber4Bytes: href
                redirectCBit: href
                enableTrafficMarketing: href
                enableTrafficMarking: href
                trafficDscp: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpFlowSpecRangesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpFlowSpecRangesList"], vport_name, emulation_host, filters)


class IxnBgpFlowSpecRangesListV4Emulation(IxnEmulationHost):
    """Generated NGPF bgpFlowSpecRangesListV4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpFlowSpecRangesListV4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpFlowSpecRangesListV4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableDestPrefixV4: href
                destPrefixV4: href
                destPrefixLengthV4: href
                enableSourcePrefixV4: href
                sourcePrefixV4: href
                sourcePrefixLengthV4: href
                ipProto: href
                fragmentMatch: href
                flowSpecName: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                numberOfFlows: href
                portMatch: href
                destPortMatch: href
                sourcePortMatch: href
                icmpTypeMatch: href
                icmpCodeMatch: href
                tcpFlagsMatch: href
                ipPacketLenMatch: href
                dscpMatch: href
                enableTrafficRate: href
                trafficRate: href
                enableTrafficAction: href
                terminalAction: href
                trafficActionSample: href
                enableRedirect: href
                enableRedirect: href
                asNumber2Bytes: href
                asNumber4Bytes: href
                ip: href
                redirectnexthop: href
                assignedNumber2Bytes: href
                assignedNumber4Bytes: href
                redirectCBit: href
                enableTrafficMarketing: href
                enableTrafficMarking: href
                trafficDscp: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpFlowSpecRangesListV4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpFlowSpecRangesListV4"], vport_name, emulation_host, filters)


class IxnBgpFlowSpecRangesListV6Emulation(IxnEmulationHost):
    """Generated NGPF bgpFlowSpecRangesListV6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpFlowSpecRangesListV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpFlowSpecRangesListV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableDestPrefixV6: href
                destPrefixV6: href
                destPrefixLengthV6: href
                destPrefixOffset: href
                enableSourcePrefixV6: href
                sourcePrefixV6: href
                sourcePrefixLengthV6: href
                srcPrefixOffset: href
                nextHeader: href
                flowLabel: href
                fragmentMatchV6: href
                ip: href
                redirectnexthop: href
                enableReirectIPv6: href
                redirectIPv6: href
                flowSpecName: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                numberOfFlows: href
                portMatch: href
                destPortMatch: href
                sourcePortMatch: href
                icmpTypeMatch: href
                icmpCodeMatch: href
                tcpFlagsMatch: href
                ipPacketLenMatch: href
                dscpMatch: href
                enableTrafficRate: href
                trafficRate: href
                enableTrafficAction: href
                terminalAction: href
                trafficActionSample: href
                enableRedirect: href
                enableRedirect: href
                asNumber2Bytes: href
                asNumber4Bytes: href
                ip: href
                redirectnexthop: href
                assignedNumber2Bytes: href
                assignedNumber4Bytes: href
                redirectCBit: href
                enableTrafficMarketing: href
                enableTrafficMarking: href
                trafficDscp: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpFlowSpecRangesListV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpFlowSpecRangesListV6"], vport_name, emulation_host, filters)


class IxnBgpIPRoutePropertyEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPRouteProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpIPRoutePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPRouteProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                useTraditionalNlri: href
                advertiseAsBGPLSPrefix: href
                routeOrigin: href
                advertiseAsBgp3107: bool
                labelStart: href
                labelEnd: href
                labelStep: href
                advertiseAsBgp3107Sr: bool
                segmentId: href
                incrementMode: href
                specialLabel: href
                enableSRGB: href
                enableAigp: href
                noOfTlvs: number
                enableAddPath: href
                addPathId: href
                packingFrom: href
                packingTo: href
                enableNextHop: href
                nextHopType: href
                nextHopIPType: href
                ipv4NextHop: href
                ipv6NextHop: href
                nextHopIncrementMode: href
                advertiseNexthopAsV4: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableWeight: href
                weight: href
                enableFlapping: href
                uptime: href
                downtime: href
                partialFlap: href
                flapFromRouteIndex: href
                flapToRouteIndex: href
                delay: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorIdMode: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExternalCommunities: number
                OverridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpIPRoutePropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpIPRouteProperty"], vport_name, emulation_host, filters)


class IxnBgpIPv4EvpnEviEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv4EvpnEvi emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv4EvpnEviEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv4EvpnEvi emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV4: number
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv4EvpnEviEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIPv4EvpnEvi"], vport_name, emulation_host, filters)

    def advertisealiasingperevi(self, expected_state=None, timeout=None):
        """Advertise Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnEviEmulation, self).call_operation('advertiseAliasingPerEvi', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnEviEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnEviEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnEviEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawaliasingperevi(self, expected_state=None, timeout=None):
        """Withdraw Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnEviEmulation, self).call_operation('withdrawAliasingPerEvi', expected_state, timeout)


class IxnBgpIPv4EvpnPbbEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv4EvpnPbb emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv4EvpnPbbEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv4EvpnPbb emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV4: number
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv4EvpnPbbEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIPv4EvpnPbb"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnPbbEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnPbbEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnPbbEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpIPv4EvpnVXLANEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv4EvpnVXLAN emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv4EvpnVXLANEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv4EvpnVXLAN emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV4: number
                multicastTunnelTypeVxlan: href
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv4EvpnVXLANEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIPv4EvpnVXLAN"], vport_name, emulation_host, filters)

    def advertisealiasingperevi(self, expected_state=None, timeout=None):
        """Advertise Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANEmulation, self).call_operation('advertiseAliasingPerEvi', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawaliasingperevi(self, expected_state=None, timeout=None):
        """Withdraw Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANEmulation, self).call_operation('withdrawAliasingPerEvi', expected_state, timeout)


class IxnBgpIPv4EvpnVXLANVpwsEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv4EvpnVXLANVpws emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv4EvpnVXLANVpwsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv4EvpnVXLANVpws emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV4: number
                multicastTunnelTypeVxlan: href
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv4EvpnVXLANVpwsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIPv4EvpnVXLANVpws"], vport_name, emulation_host, filters)

    def advertisealiasingperevi(self, expected_state=None, timeout=None):
        """Advertise Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANVpwsEmulation, self).call_operation('advertiseAliasingPerEvi', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANVpwsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANVpwsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANVpwsEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawaliasingperevi(self, expected_state=None, timeout=None):
        """Withdraw Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVXLANVpwsEmulation, self).call_operation('withdrawAliasingPerEvi', expected_state, timeout)


class IxnBgpIPv4EvpnVpwsEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv4EvpnVpws emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv4EvpnVpwsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv4EvpnVpws emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV4: number
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv4EvpnVpwsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIPv4EvpnVpws"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVpwsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVpwsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv4EvpnVpwsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpIPv6EvpnEviEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv6EvpnEvi emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv6EvpnEviEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv6EvpnEvi emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV6: number
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv6EvpnEviEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnEvi"], vport_name, emulation_host, filters)

    def advertisealiasingperevi(self, expected_state=None, timeout=None):
        """Advertise Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnEviEmulation, self).call_operation('advertiseAliasingPerEvi', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnEviEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnEviEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnEviEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawaliasingperevi(self, expected_state=None, timeout=None):
        """Withdraw Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnEviEmulation, self).call_operation('withdrawAliasingPerEvi', expected_state, timeout)


class IxnBgpIPv6EvpnPbbEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv6EvpnPbb emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv6EvpnPbbEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv6EvpnPbb emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV6: number
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv6EvpnPbbEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnPbb"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnPbbEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnPbbEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnPbbEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpIPv6EvpnVXLANEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv6EvpnVXLAN emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv6EvpnVXLANEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv6EvpnVXLAN emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV6: number
                multicastTunnelTypeVxlan: href
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv6EvpnVXLANEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnVXLAN"], vport_name, emulation_host, filters)

    def advertisealiasingperevi(self, expected_state=None, timeout=None):
        """Advertise Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANEmulation, self).call_operation('advertiseAliasingPerEvi', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawaliasingperevi(self, expected_state=None, timeout=None):
        """Withdraw Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANEmulation, self).call_operation('withdrawAliasingPerEvi', expected_state, timeout)


class IxnBgpIPv6EvpnVXLANVpwsEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv6EvpnVXLANVpws emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv6EvpnVXLANVpwsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv6EvpnVXLANVpws emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV6: number
                multicastTunnelTypeVxlan: href
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv6EvpnVXLANVpwsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnVXLANVpws"], vport_name, emulation_host, filters)

    def advertisealiasingperevi(self, expected_state=None, timeout=None):
        """Advertise Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANVpwsEmulation, self).call_operation('advertiseAliasingPerEvi', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANVpwsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANVpwsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANVpwsEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawaliasingperevi(self, expected_state=None, timeout=None):
        """Withdraw Aliasing Per EVI
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVXLANVpwsEmulation, self).call_operation('withdrawAliasingPerEvi', expected_state, timeout)


class IxnBgpIPv6EvpnVpwsEmulation(IxnEmulationHost):
    """Generated NGPF bgpIPv6EvpnVpws emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIPv6EvpnVpwsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIPv6EvpnVpws emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numBroadcastDomainV6: number
                esiType: href
                esiValue: list
                autoConfigureRdIpAddress: href
                rdIpAddress: href
                rdEvi: href
                enableL3vniTargetList: href
                advertiseL3vniSeparately: href
                bMacFirstLabel: href
                enableBMacSecondLabel: href
                bMacSecondLabel: href
                adRouteLabel: href
                multicastTunnelType: href
                useUpstreamDownstreamAssignedMplsLabel: href
                includePmsiTunnelAttribute: href
                autoConfigPMSITunnelId: href
                pmsiTunnelIDv4: href
                pmsiTunnelIDv6: href
                upstreamDownstreamAssignedMplsLabel: href
                useIpv4MappedIpv6Address: href
                numRtInExportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInImportRouteTargetList: number
                numRtInL3vniExportRouteTargetList: number
                l3vniImportRtListSameAsL3vniExportRtList: bool
                numRtInL3vniImportRouteTargetList: number
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIPv6EvpnVpwsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnVpws"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVpwsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVpwsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnBgpIPv6EvpnVpwsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpImportRouteTargetListEmulation(IxnEmulationHost):
    """Generated NGPF bgpImportRouteTargetList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpImportRouteTargetListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpImportRouteTargetList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                targetType: href
                targetAsNumber: href
                targetIpAddress: href
                targetAs4Number: href
                targetAssignedNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpImportRouteTargetListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnEvi","bgpImportRouteTargetList"], vport_name, emulation_host, filters)


class IxnBgpIpv4AdL2VpnEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv4AdL2Vpn emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv4AdL2VpnEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv4AdL2Vpn emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                typeVsiId: href
                localIpv4: list
                dutIpv4: list
                localRouterID: list
                typeVplsId: href
                ipAddressVplsId: href
                asNumberVplsId: href
                assignedNumberVplsId: href
                numberVsiId: href
                importVplsIdAsRd: href
                typeVplsRd: href
                ipAddressVplsRd: href
                asNumberVplsRd: href
                assignedNumberVplsRd: href
                importRDAsRT: href
                typeVplsRt: href
                ipAddressVplsRt: href
                asNumberVplsRt: href
                assignedNumberVplsRt: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv4AdL2VpnEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIpv4AdL2Vpn"], vport_name, emulation_host, filters)

    def readvertiseadvplsroute(self, expected_state=None, timeout=None):
        """Re-advertise Aged out BGP Routes in a Route Range
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4AdL2VpnEmulation, self).call_operation('readvertiseADVPLSRoute', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4AdL2VpnEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP AD VPLS
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4AdL2VpnEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP AD VPLS
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4AdL2VpnEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawadvplsroute(self, expected_state=None, timeout=None):
        """Age out percentage of BGP Routes in a Route Range
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4AdL2VpnEmulation, self).call_operation('withdrawADVPLSRoute', expected_state, timeout)


class IxnBgpIpv4L2SiteEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv4L2Site emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv4L2SiteEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv4L2Site emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                dutIp: list
                encapsulationType: href
                enableBfdVccv: href
                enableVccvPing: href
                localRouterID: list
                numL2Sites: href
                siteId: href
                vpnName: href
                typeTarget: href
                targetIpAddr: href
                targetAsNumber: href
                targetAssignedNumber: href
                typeDistinguish: href
                distinguishIpAddr: href
                distinguishAsNumber: href
                distinguishAssignedNumber: href
                mtuL2Site: href
                enControlWord: href
                enSeqDelivery: href
                enCluster: href
                numClusterPerL2Site: number
                numLabelBlocksPerL2Site: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv4L2SiteEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIpv4L2Site"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4L2SiteEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP VPLS L2Site
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4L2SiteEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP VPLS L2Site
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4L2SiteEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpIpv4MVrfEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv4MVrf emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv4MVrfEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv4MVrf emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                multicastTunnelType: href
                multicastDistinguisherType: href
                multicastDistinguisherIpAddress: href
                multicastDistinguisherAsNumber: href
                multicastDistinguisherAs4Number: href
                multicastDistinguisherAssignedNumber: href
                includePmsiTunnelAttribute: href
                useUpOrDownStreamAssigneLabel: href
                upOrDownStreamAssignedLabel: href
                rsvpP2mpId: href
                rsvpP2mpIdAsNumber: href
                rsvpTunnelId: href
                localIpv4: list
                dutIpv4: list
                localRouterID: list
                numRtInImportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInExportRouteTargetList: number
                sameAsExportRT: bool
                numRtInUmhExportRouteTargetList: number
                sameAsImportRT: bool
                numRtInUmhImportRouteTargetList: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv4MVrfEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIpv4MVrf"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4MVrfEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4MVrfEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4MVrfEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpIpv4PeerEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv4Peer emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv4PeerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv4Peer emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableBgpId: href
                enableBgpIdSameasRouterId: href
                bgpId: href
                localIpv4Ver2: list
                dutIp: href
                ethernetSegmentsCountV4: number
                numberFlowSpecRangeV4: number
                numberFlowSpecRangeV6: number
                numberSRTEPolicies: number
                irbIpv4Address: href
                portData: href
                localRouterID: list
                localAs2Bytes: href
                enable4ByteAs: href
                localAs4Bytes: href
                asSetMode: href
                enableBfdRegistration: href
                modeOfBfdOperations: href
                enableGracefulRestart: href
                enableLlgr: href
                restartTime: href
                staleTime: href
                actAsRestarted: href
                advertiseEndOfRib: href
                operationalModel: href
                ipVrfToIpVrfType: enum
                routersMacOrIrbMacAddress: href
                irbInterfaceLabel: href
                vplsEnableNextHop: href
                vplsNextHop: href
                holdTimer: href
                configureKeepaliveTimer: href
                keepaliveTimer: href
                updateInterval: href
                ttl: href
                authentication: href
                md5Key: href
                discardIxiaGeneratedRoutes: href
                sendIxiaSignatureWithRoutes: href
                tcpWindowSizeInBytes: href
                numBgpUpdatesGeneratedPerIteration: href
                type: href
                flap: href
                uptimeInSec: href
                downtimeInSec: href
                filterIpV4Unicast: href
                filterIpV4Multicast: href
                filterIpV4Mpls: href
                filterIpV4MplsVpn: href
                filterIpV6Unicast: href
                filterIpV6Multicast: href
                filterIpV6Mpls: href
                filterIpV6MplsVpn: href
                filterVpls: href
                filterIpV4MulticastVpn: href
                filterIpV6MulticastVpn: href
                filterEvpn: href
                filterLinkState: href
                filterIpv4MulticastBgpMplsVpn: href
                filterIpv6MulticastBgpMplsVpn: href
                filterIpv4UnicastFlowSpec: href
                filterIpv6UnicastFlowSpec: href
                filterSRTEPoliciesV4: href
                filterSRTEPoliciesV6: href
                capabilityIpV4Unicast: href
                capabilityIpV4Multicast: href
                capabilityIpV4MplsVpn: href
                capabilityIpV6Unicast: href
                capabilityIpV6Multicast: href
                capabilityIpV6MplsVpn: href
                capabilityIpV4Mdt: href
                capabilityVpls: href
                capabilityIpV4MulticastVpn: href
                capabilityIpV6MulticastVpn: href
                capabilityRouteRefresh: href
                capabilityRouteConstraint: href
                capabilityLinkStateNonVpn: href
                evpn: href
                ipv4MulticastBgpMplsVpn: href
                ipv6MulticastBgpMplsVpn: href
                capabilityipv4UnicastFlowSpec: href
                capabilityipv6UnicastFlowSpec: href
                capabilitySRTEPoliciesV4: href
                capabilitySRTEPoliciesV6: href
                capabilityIpv4UnicastAddPath: href
                capabilityIpv6UnicastAddPath: href
                ipv4UnicastAddPathMode: href
                ipv6UnicastAddPathMode: href
                ipv4MplsAddPathMode: href
                ipv6MplsAddPathMode: href
                customSidType: href
                ipv4MplsCapability: bool
                ipv6MplsCapability: bool
                capabilityIpv4MplsAddPath: bool
                capabilityIpv6MplsAddPath: bool
                sRGBRangeCount: number
                numBgpLsId: href
                numBgpLsInstanceIdentifier: href
                bgpLsNoOfCommunities: number
                enableBgpLsCommunity: href
                noOfExtendedCommunities: number
                bgpLsEnableExtendedCommunity: href
                bgpLsOverridePeerAsSetMode: href
                bgpLsAsSetMode: href
                bgpLsNoOfASPathSegments: number
                bgpLsEnableAsPathSegments: href
                bgpLsNoOfClusters: number
                bgpLsEnableCluster: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv4PeerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer"], vport_name, emulation_host, filters)

    def bgpipv4flowspeclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 FlowSpec Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('bgpIPv4FlowSpecLearnedInfo', expected_state, timeout)

    def bgpipv6flowspeclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 FlowSpec Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('bgpIPv6FlowSpecLearnedInfo', expected_state, timeout)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getadvplslearnedinfo(self, expected_state=None, timeout=None):
        """Get ADVPLS Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getADVPLSLearnedInfo', expected_state, timeout)

    def getalllearnedinfo(self, expected_state=None, timeout=None):
        """Get All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getAllLearnedInfo', expected_state, timeout)

    def getevpnlearnedinfo(self, expected_state=None, timeout=None):
        """Get EVPN Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getEVPNLearnedInfo', expected_state, timeout)

    def getipv4learnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getIPv4LearnedInfo', expected_state, timeout)

    def getipv4vpnlearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 Vpn Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getIPv4VpnLearnedInfo', expected_state, timeout)

    def getipv6learnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getIPv6LearnedInfo', expected_state, timeout)

    def getipv6vpnlearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 Vpn Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getIPv6VpnLearnedInfo', expected_state, timeout)

    def getlinkstatelearnedinfo(self, expected_state=None, timeout=None):
        """Get Link State Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getLinkStateLearnedInfo', expected_state, timeout)

    def getvplslearnedinfo(self, expected_state=None, timeout=None):
        """Get VPLS Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('getVPLSLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumekeepalive(self, expected_state=None, timeout=None):
        """Resume sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('resumeKeepAlive', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP Peer
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP Peer
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('stop', expected_state, timeout)

    def stopkeepalive(self, expected_state=None, timeout=None):
        """Stop sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv4PeerEmulation, self).call_operation('stopKeepAlive', expected_state, timeout)


class IxnBgpIpv6AdL2VpnEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv6AdL2Vpn emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv6AdL2VpnEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv6AdL2Vpn emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                typeVsiId: href
                localIpv6: list
                dutIpv6: list
                localRouterID: list
                typeVplsId: href
                ipAddressVplsId: href
                asNumberVplsId: href
                assignedNumberVplsId: href
                numberVsiId: href
                importVplsIdAsRd: href
                typeVplsRd: href
                ipAddressVplsRd: href
                asNumberVplsRd: href
                assignedNumberVplsRd: href
                importRDAsRT: href
                typeVplsRt: href
                ipAddressVplsRt: href
                asNumberVplsRt: href
                assignedNumberVplsRt: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv6AdL2VpnEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIpv6AdL2Vpn"], vport_name, emulation_host, filters)

    def readvertiseadvplsroute(self, expected_state=None, timeout=None):
        """Re-advertise Aged out BGP Routes in a Route Range
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6AdL2VpnEmulation, self).call_operation('readvertiseADVPLSRoute', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6AdL2VpnEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP AD VPLS
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6AdL2VpnEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP AD VPLS
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6AdL2VpnEmulation, self).call_operation('stop', expected_state, timeout)

    def withdrawadvplsroute(self, expected_state=None, timeout=None):
        """Age out percentage of BGP Routes in a Route Range
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6AdL2VpnEmulation, self).call_operation('withdrawADVPLSRoute', expected_state, timeout)


class IxnBgpIpv6L2SiteEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv6L2Site emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv6L2SiteEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv6L2Site emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                dutIp: list
                localRouterID: list
                numL2Sites: href
                siteId: href
                vpnName: href
                typeTarget: href
                targetIpAddr: href
                targetAsNumber: href
                targetAssignedNumber: href
                typeDistinguish: href
                distinguishIpAddr: href
                distinguishAsNumber: href
                distinguishAssignedNumber: href
                mtuL2Site: href
                enControlWord: href
                enSeqDelivery: href
                enCluster: href
                numClusterPerL2Site: number
                numLabelBlocksPerL2Site: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv6L2SiteEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIpv6L2Site"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6L2SiteEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP VPLS L2Site
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6L2SiteEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP VPLS L2Site
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6L2SiteEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpIpv6MVrfEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv6MVrf emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv6MVrfEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv6MVrf emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                multicastTunnelType: href
                multicastDistinguisherType: href
                multicastDistinguisherIpAddress: href
                multicastDistinguisherAsNumber: href
                multicastDistinguisherAs4Number: href
                multicastDistinguisherAssignedNumber: href
                includePmsiTunnelAttribute: href
                useUpOrDownStreamAssigneLabel: href
                upOrDownStreamAssignedLabel: href
                rsvpP2mpId: href
                rsvpP2mpIdAsNumber: href
                rsvpTunnelId: href
                rootAddress: list
                numberOfTLVs: number
                localIpv6: list
                dutIpv6: list
                localRouterID: list
                numRtInImportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInExportRouteTargetList: number
                sameAsExportRT: bool
                numRtInUmhExportRouteTargetList: number
                sameAsImportRT: bool
                numRtInUmhImportRouteTargetList: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv6MVrfEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIpv6MVrf"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6MVrfEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6MVrfEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6MVrfEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpIpv6PeerEmulation(IxnEmulationHost):
    """Generated NGPF bgpIpv6Peer emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpIpv6PeerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpIpv6Peer emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableBgpId: href
                enableBgpIdSameAsRouterId: href
                bgpId: href
                localIpv6Ver2: list
                dutIp: href
                ethernetSegmentsCountV6: number
                numberFlowSpecRangeV4: number
                numberFlowSpecRangeV6: number
                numberSRTEPolicies: number
                irbIpv6Address: href
                portData: href
                localRouterID: list
                localAs2Bytes: href
                enable4ByteAs: href
                localAs4Bytes: href
                asSetMode: href
                enableBfdRegistration: href
                modeOfBfdOperations: href
                enableGracefulRestart: href
                enableLlgr: href
                restartTime: href
                staleTime: href
                actAsRestarted: href
                advertiseEndOfRib: href
                operationalModel: href
                ipVrfToIpVrfType: enum
                routersMacOrIrbMacAddress: href
                irbInterfaceLabel: href
                vplsEnableNextHop: href
                vplsNextHop: href
                holdTimer: href
                configureKeepaliveTimer: href
                keepaliveTimer: href
                updateInterval: href
                ttl: href
                authentication: href
                md5Key: href
                discardIxiaGeneratedRoutes: href
                sendIxiaSignatureWithRoutes: href
                tcpWindowSizeInBytes: href
                numBgpUpdatesGeneratedPerIteration: href
                type: href
                flap: href
                uptimeInSec: href
                downtimeInSec: href
                filterIpV4Unicast: href
                filterIpV4Multicast: href
                filterIpV4Mpls: href
                filterIpV4MplsVpn: href
                filterIpV6Unicast: href
                filterIpV6Multicast: href
                filterIpV6Mpls: href
                filterIpV6MplsVpn: href
                filterVpls: href
                filterIpV4MulticastVpn: href
                filterIpV6MulticastVpn: href
                filterEvpn: href
                filterLinkState: href
                filterIpv4MulticastBgpMplsVpn: href
                filterIpv6MulticastBgpMplsVpn: href
                filterIpv4UnicastFlowSpec: href
                filterIpv6UnicastFlowSpec: href
                filterSRTEPoliciesV4: href
                filterSRTEPoliciesV6: href
                capabilityIpV4Unicast: href
                capabilityIpV4Multicast: href
                capabilityIpV4MplsVpn: href
                capabilityIpV6Unicast: href
                capabilityIpV6Multicast: href
                capabilityIpV6MplsVpn: href
                capabilityIpV4Mdt: href
                capabilityVpls: href
                capabilityIpV4MulticastVpn: href
                capabilityIpV6MulticastVpn: href
                capabilityRouteRefresh: href
                capabilityRouteConstraint: href
                capabilityLinkStateNonVpn: href
                evpn: href
                ipv4MulticastBgpMplsVpn: href
                ipv6MulticastBgpMplsVpn: href
                capabilityipv4UnicastFlowSpec: href
                capabilityipv6UnicastFlowSpec: href
                capabilitySRTEPoliciesV4: href
                capabilitySRTEPoliciesV6: href
                capabilityIpv4UnicastAddPath: href
                capabilityIpv6UnicastAddPath: href
                ipv4UnicastAddPathMode: href
                ipv6UnicastAddPathMode: href
                ipv4MplsAddPathMode: href
                ipv6MplsAddPathMode: href
                customSidType: href
                ipv4MplsCapability: bool
                ipv6MplsCapability: bool
                capabilityIpv4MplsAddPath: bool
                capabilityIpv6MplsAddPath: bool
                sRGBRangeCount: number
                numBgpLsId: href
                numBgpLsInstanceIdentifier: href
                bgpLsNoOfCommunities: number
                enableBgpLsCommunity: href
                noOfExtendedCommunities: number
                bgpLsEnableExtendedCommunity: href
                bgpLsOverridePeerAsSetMode: href
                bgpLsAsSetMode: href
                bgpLsNoOfASPathSegments: number
                bgpLsEnableAsPathSegments: href
                bgpLsNoOfClusters: number
                bgpLsEnableCluster: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpIpv6PeerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer"], vport_name, emulation_host, filters)

    def bgpipv4flowspeclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 FlowSpec Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('bgpIPv4FlowSpecLearnedInfo', expected_state, timeout)

    def bgpipv6flowspeclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 FlowSpec Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('bgpIPv6FlowSpecLearnedInfo', expected_state, timeout)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getadvplslearnedinfo(self, expected_state=None, timeout=None):
        """Get ADVPLS Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getADVPLSLearnedInfo', expected_state, timeout)

    def getalllearnedinfo(self, expected_state=None, timeout=None):
        """Get All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getAllLearnedInfo', expected_state, timeout)

    def getevpnlearnedinfo(self, expected_state=None, timeout=None):
        """Get EVPN Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getEVPNLearnedInfo', expected_state, timeout)

    def getipv4learnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getIPv4LearnedInfo', expected_state, timeout)

    def getipv4vpnlearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 Vpn Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getIPv4VpnLearnedInfo', expected_state, timeout)

    def getipv6learnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getIPv6LearnedInfo', expected_state, timeout)

    def getipv6vpnlearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 Vpn Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getIPv6VpnLearnedInfo', expected_state, timeout)

    def getlinkstatelearnedinfo(self, expected_state=None, timeout=None):
        """Get Link State Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getLinkStateLearnedInfo', expected_state, timeout)

    def getvplslearnedinfo(self, expected_state=None, timeout=None):
        """Get VPLS Learned Info
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('getVPLSLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumekeepalive(self, expected_state=None, timeout=None):
        """Resume sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('resumeKeepAlive', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP Peer
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP Peer
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('stop', expected_state, timeout)

    def stopkeepalive(self, expected_state=None, timeout=None):
        """Stop sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnBgpIpv6PeerEmulation, self).call_operation('stopKeepAlive', expected_state, timeout)


class IxnBgpL3VNIExportRouteTargetListEmulation(IxnEmulationHost):
    """Generated NGPF bgpL3VNIExportRouteTargetList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpL3VNIExportRouteTargetListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpL3VNIExportRouteTargetList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                targetType: href
                targetAsNumber: href
                targetIpAddress: href
                targetAs4Number: href
                targetAssignedNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpL3VNIExportRouteTargetListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnEvi","bgpL3VNIExportRouteTargetList"], vport_name, emulation_host, filters)


class IxnBgpL3VNIImportRouteTargetListEmulation(IxnEmulationHost):
    """Generated NGPF bgpL3VNIImportRouteTargetList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpL3VNIImportRouteTargetListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpL3VNIImportRouteTargetList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                targetType: href
                targetAsNumber: href
                targetIpAddress: href
                targetAs4Number: href
                targetAssignedNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpL3VNIImportRouteTargetListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnEvi","bgpL3VNIImportRouteTargetList"], vport_name, emulation_host, filters)


class IxnBgpL3VpnRoutePropertyEmulation(IxnEmulationHost):
    """Generated NGPF bgpL3VpnRouteProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpL3VpnRoutePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpL3VpnRouteProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                useAsIpv4UmhRoutes: bool
                enableIpv4Receiver: bool
                enableIpv4Sender: bool
                useTraditionalNlri: href
                distinguisherType: href
                distinguisherIpAddress: href
                distinguisherAsNumber: href
                distinguisherAssignedNumber: href
                labelSpaceId: href
                labelStart: href
                labelEnd: href
                labelStep: href
                labelMode: href
                includeVrfRouteImportExtComm: href
                includeSourceAsExtComm: href
                packingFrom: href
                packingTo: href
                enableNextHop: href
                nextHopType: href
                nextHopIPType: href
                ipv4NextHop: href
                ipv6NextHop: href
                nextHopIncrementMode: href
                advertiseNexthopAsV4: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableWeight: href
                weight: href
                enableFlapping: href
                uptime: href
                downtime: href
                partialFlap: href
                flapFromRouteIndex: href
                flapToRouteIndex: href
                delay: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorIdMode: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExternalCommunities: number
                OverridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpL3VpnRoutePropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpL3VpnRouteProperty"], vport_name, emulation_host, filters)


class IxnBgpLsAsPathSegmentListEmulation(IxnEmulationHost):
    """Generated NGPF bgpLsAsPathSegmentList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpLsAsPathSegmentListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpLsAsPathSegmentList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableASPathSegment: href
                segmentType: href
                numberOfAsNumberInSegment: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpLsAsPathSegmentListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpLsAsPathSegmentList"], vport_name, emulation_host, filters)


class IxnBgpLsClusterIdListEmulation(IxnEmulationHost):
    """Generated NGPF bgpLsClusterIdList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpLsClusterIdListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpLsClusterIdList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                clusterId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpLsClusterIdListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpLsClusterIdList"], vport_name, emulation_host, filters)


class IxnBgpLsCommunitiesListEmulation(IxnEmulationHost):
    """Generated NGPF bgpLsCommunitiesList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpLsCommunitiesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpLsCommunitiesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                type: href
                asNumber: href
                lastTwoOctets: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpLsCommunitiesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpLsCommunitiesList"], vport_name, emulation_host, filters)


class IxnBgpLsExtendedCommunitiesListEmulation(IxnEmulationHost):
    """Generated NGPF bgpLsExtendedCommunitiesList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpLsExtendedCommunitiesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpLsExtendedCommunitiesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                type: href
                subType: href
                asNumber2Bytes: href
                assignedNumber4Bytes: href
                ip: href
                asNumber4Bytes: href
                assignedNumber2Bytes: href
                opaqueData: href
                colorCOBits: href
                colorReservedBits: href
                colorValue: href
                linkBandwidth: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpLsExtendedCommunitiesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpLsExtendedCommunitiesList"], vport_name, emulation_host, filters)


class IxnBgpMVpnReceiverSitesIpv4Emulation(IxnEmulationHost):
    """Generated NGPF bgpMVpnReceiverSitesIpv4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpMVpnReceiverSitesIpv4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpMVpnReceiverSitesIpv4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startGroupAddressIpv4: href
                startSourceOrCrpAddressIpv4: href
                startSourceAddressIpv4: href
                cMulticastRouteType: href
                supportLeafADRoutesSending: href
                downstreamLabel: href
                sendTriggeredMulticastRoute: href
                sourceGroupMapping: href
                groupMaskWidth: href
                groupAddressCount: href
                sourceMaskWidth: href
                sourceAddressCount: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpMVpnReceiverSitesIpv4Emulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpMVpnReceiverSitesIpv4"], vport_name, emulation_host, filters)


class IxnBgpMVpnReceiverSitesIpv6Emulation(IxnEmulationHost):
    """Generated NGPF bgpMVpnReceiverSitesIpv6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpMVpnReceiverSitesIpv6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpMVpnReceiverSitesIpv6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startGroupAddressIpv6: href
                startSourceOrCrpAddressIpv6: href
                startSourceAddressIpv6: href
                cMulticastRouteType: href
                supportLeafADRoutesSending: href
                downstreamLabel: href
                sendTriggeredMulticastRoute: href
                sourceGroupMapping: href
                groupMaskWidth: href
                groupAddressCount: href
                sourceMaskWidth: href
                sourceAddressCount: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpMVpnReceiverSitesIpv6Emulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpMVpnReceiverSitesIpv6"], vport_name, emulation_host, filters)


class IxnBgpMVpnSenderSitesIpv4Emulation(IxnEmulationHost):
    """Generated NGPF bgpMVpnSenderSitesIpv4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpMVpnSenderSitesIpv4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpMVpnSenderSitesIpv4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startGroupAddressIpv4: href
                startSourceAddressIpv4: href
                sendTriggeredSourceActiveADRoute: href
                sourceGroupMapping: href
                groupMaskWidth: href
                groupAddressCount: href
                sourceMaskWidth: href
                sourceAddressCount: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpMVpnSenderSitesIpv4Emulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpMVpnSenderSitesIpv4"], vport_name, emulation_host, filters)


class IxnBgpMVpnSenderSitesIpv6Emulation(IxnEmulationHost):
    """Generated NGPF bgpMVpnSenderSitesIpv6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpMVpnSenderSitesIpv6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpMVpnSenderSitesIpv6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startGroupAddressIpv6: href
                startSourceAddressIpv6: href
                includeIpv6ExplicitNullLabel: href
                sendTriggeredSourceActiveADRoute: href
                sourceGroupMapping: href
                groupMaskWidth: href
                groupAddressCount: href
                sourceMaskWidth: href
                sourceAddressCount: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpMVpnSenderSitesIpv6Emulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpMVpnSenderSitesIpv6"], vport_name, emulation_host, filters)


class IxnBgpSRGBRangeSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF bgpSRGBRangeSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRGBRangeSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRGBRangeSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startSID: href
                sIDCount: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRGBRangeSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpSRGBRangeSubObjectsList"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesListV4Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesListV4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesListV4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesListV4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfTunnelsV4: number
                srtepolicyName: href
                policyType: href
                distinguisher: href
                policyColor: href
                endPointV4: href
                endPointV6: href
                numberOfActiveTunnels: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                enableAddPath: href
                addPathId: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesListV4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpSRTEPoliciesListV4"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesListV6Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesListV6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesListV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesListV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfTunnelsV6: number
                srtepolicyName: href
                policyType: href
                distinguisher: href
                policyColor: href
                endPointV4: href
                endPointV6: href
                numberOfActiveTunnels: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                enableAddPath: href
                addPathId: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesListV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpSRTEPoliciesListV6"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesSegmentListV4Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesSegmentListV4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesSegmentListV4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesSegmentListV4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfSegmentsV4: number
                srtepolicyName: list
                segmentListNumber: href
                active: href
                enWeight: href
                weight: href
                numberOfActiveSegments: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesSegmentListV4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpSRTEPoliciesListV4","bgpSRTEPoliciesTunnelEncapsulationListV4","bgpSRTEPoliciesSegmentListV4"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesSegmentListV6Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesSegmentListV6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesSegmentListV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesSegmentListV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfSegmentsV6: number
                srtepolicyName: list
                segmentListNumber: href
                active: href
                enWeight: href
                weight: href
                numberOfActiveSegments: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesSegmentListV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpSRTEPoliciesListV6","bgpSRTEPoliciesTunnelEncapsulationListV6","bgpSRTEPoliciesSegmentListV6"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesSegmentsCollectionV4Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesSegmentsCollectionV4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesSegmentsCollectionV4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesSegmentsCollectionV4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srtepolicyName: list
                segmentListNumber: list
                active: href
                segmentType: href
                label: href
                trafficClass: href
                trafficClass: href
                timeToLive: href
                ipv6SID: href
                ipv4NodeAddress: href
                ipv6NodeAddress: href
                interfaceIndex: href
                ipv4LocalAddress: href
                ipv4RemoteAddress: href
                ipv6LocalAddress: href
                ipv6RemoteAddress: href
                optionalTLVType: href
                optionalLabel: href
                optionalTrafficClass: href
                optionalBottomOfStack: href
                optionalTimeToLive: href
                optionalIpv6SID: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesSegmentsCollectionV4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpSRTEPoliciesListV4","bgpSRTEPoliciesTunnelEncapsulationListV4","bgpSRTEPoliciesSegmentListV4","bgpSRTEPoliciesSegmentsCollectionV4"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesSegmentsCollectionV6Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesSegmentsCollectionV6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesSegmentsCollectionV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesSegmentsCollectionV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srtepolicyName: list
                segmentListNumber: list
                active: href
                segmentType: href
                label: href
                trafficClass: href
                trafficClass: href
                timeToLive: href
                ipv6SID: href
                ipv4NodeAddress: href
                ipv6NodeAddress: href
                interfaceIndex: href
                ipv4LocalAddress: href
                ipv4RemoteAddress: href
                ipv6LocalAddress: href
                ipv6RemoteAddress: href
                optionalTLVType: href
                optionalLabel: href
                optionalTrafficClass: href
                optionalBottomOfStack: href
                optionalTimeToLive: href
                optionalIpv6SID: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesSegmentsCollectionV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpSRTEPoliciesListV6","bgpSRTEPoliciesTunnelEncapsulationListV6","bgpSRTEPoliciesSegmentListV6","bgpSRTEPoliciesSegmentsCollectionV6"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesTunnelEncapsulationListV4Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesTunnelEncapsulationListV4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesTunnelEncapsulationListV4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesTunnelEncapsulationListV4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfSegmentListV4: number
                srtepolicyName: list
                active: href
                tunnelType: href
                numberOfActiveSegmentList: href
                enRemoteEndPointTLV: href
                as4Number: href
                addressFamily: href
                remoteEndpointIPv4: href
                remoteEndpointIPv6: href
                enColorTLV: href
                colorValue: href
                enPrefTLV: href
                prefValue: href
                enBindingTLV: href
                bindingSIDType: href
                SID4Octet: href
                useAsMPLSLabel: href
                IPv6SID: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesTunnelEncapsulationListV4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpSRTEPoliciesListV4","bgpSRTEPoliciesTunnelEncapsulationListV4"], vport_name, emulation_host, filters)


class IxnBgpSRTEPoliciesTunnelEncapsulationListV6Emulation(IxnEmulationHost):
    """Generated NGPF bgpSRTEPoliciesTunnelEncapsulationListV6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpSRTEPoliciesTunnelEncapsulationListV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpSRTEPoliciesTunnelEncapsulationListV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfSegmentListV6: number
                srtepolicyName: list
                active: href
                tunnelType: href
                numberOfActiveSegmentList: href
                enRemoteEndPointTLV: href
                as4Number: href
                addressFamily: href
                remoteEndpointIPv4: href
                remoteEndpointIPv6: href
                enColorTLV: href
                colorValue: href
                enPrefTLV: href
                prefValue: href
                enBindingTLV: href
                bindingSIDType: href
                SID4Octet: href
                useAsMPLSLabel: href
                IPv6SID: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpSRTEPoliciesTunnelEncapsulationListV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpSRTEPoliciesListV6","bgpSRTEPoliciesTunnelEncapsulationListV6"], vport_name, emulation_host, filters)


class IxnBgpUmhExportRouteTargetListEmulation(IxnEmulationHost):
    """Generated NGPF bgpUmhExportRouteTargetList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpUmhExportRouteTargetListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpUmhExportRouteTargetList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                targetType: href
                targetAsNumber: href
                targetIpAddress: href
                targetAs4Number: href
                targetAssignedNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpUmhExportRouteTargetListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpV6Vrf","bgpUmhExportRouteTargetList"], vport_name, emulation_host, filters)


class IxnBgpUmhImportRouteTargetListEmulation(IxnEmulationHost):
    """Generated NGPF bgpUmhImportRouteTargetList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpUmhImportRouteTargetListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpUmhImportRouteTargetList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                targetType: href
                targetAsNumber: href
                targetIpAddress: href
                targetAs4Number: href
                targetAssignedNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpUmhImportRouteTargetListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpV6Vrf","bgpUmhImportRouteTargetList"], vport_name, emulation_host, filters)


class IxnBgpV6IPRoutePropertyEmulation(IxnEmulationHost):
    """Generated NGPF bgpV6IPRouteProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpV6IPRoutePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpV6IPRouteProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                useTraditionalNlri: href
                advertiseAsBGPLSPrefix: href
                routeOrigin: href
                advertiseAsBgp3107: bool
                labelStart: href
                labelEnd: href
                labelStep: href
                advertiseAsBgp3107Sr: bool
                segmentId: href
                incrementMode: href
                specialLabel: href
                enableSRGB: href
                enableAigp: href
                noOfTlvs: number
                enableAddPath: href
                addPathId: href
                packingFrom: href
                packingTo: href
                enableNextHop: href
                nextHopType: href
                nextHopIPType: href
                ipv4NextHop: href
                ipv6NextHop: href
                nextHopIncrementMode: href
                advertiseNexthopAsV4: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableWeight: href
                weight: href
                enableFlapping: href
                uptime: href
                downtime: href
                partialFlap: href
                flapFromRouteIndex: href
                flapToRouteIndex: href
                delay: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorIdMode: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExternalCommunities: number
                OverridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpV6IPRoutePropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpV6IPRouteProperty"], vport_name, emulation_host, filters)


class IxnBgpV6L3VpnRoutePropertyEmulation(IxnEmulationHost):
    """Generated NGPF bgpV6L3VpnRouteProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpV6L3VpnRoutePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpV6L3VpnRouteProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                useAsIpv6UmhRoutes: bool
                enableIpv6Receiver: bool
                enableIpv6Sender: bool
                useTraditionalNlri: href
                distinguisherType: href
                distinguisherIpAddress: href
                distinguisherAsNumber: href
                distinguisherAssignedNumber: href
                labelSpaceId: href
                labelStart: href
                labelEnd: href
                labelStep: href
                labelMode: href
                includeVrfRouteImportExtComm: href
                includeSourceAsExtComm: href
                packingFrom: href
                packingTo: href
                enableNextHop: href
                nextHopType: href
                nextHopIPType: href
                ipv4NextHop: href
                ipv6NextHop: href
                nextHopIncrementMode: href
                advertiseNexthopAsV4: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableWeight: href
                weight: href
                enableFlapping: href
                uptime: href
                downtime: href
                partialFlap: href
                flapFromRouteIndex: href
                flapToRouteIndex: href
                delay: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorIdMode: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExternalCommunities: number
                OverridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpV6L3VpnRoutePropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","bgpV6L3VpnRouteProperty"], vport_name, emulation_host, filters)


class IxnBgpV6VrfEmulation(IxnEmulationHost):
    """Generated NGPF bgpV6Vrf emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpV6VrfEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpV6Vrf emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIpv6: list
                dutIpv6: list
                localRouterID: list
                numRtInImportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInExportRouteTargetList: number
                sameAsExportRT: bool
                numRtInUmhExportRouteTargetList: number
                sameAsImportRT: bool
                numRtInUmhImportRouteTargetList: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpV6VrfEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpV6Vrf"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpV6VrfEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpV6VrfEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpV6VrfEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpVrfEmulation(IxnEmulationHost):
    """Generated NGPF bgpVrf emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnBgpVrfEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpVrf emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIpv4: list
                dutIpv4: list
                localRouterID: list
                numRtInImportRouteTargetList: number
                importRtListSameAsExportRtList: bool
                numRtInExportRouteTargetList: number
                sameAsExportRT: bool
                numRtInUmhExportRouteTargetList: number
                sameAsImportRT: bool
                numRtInUmhImportRouteTargetList: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnBgpVrfEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpVrf"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnBgpVrfEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpVrfEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop BGP VRF
            For expected_state options see the class state variables
        """
        super(IxnBgpVrfEmulation, self).call_operation('stop', expected_state, timeout)


class IxnBgpv4BMacMappedIpListEmulation(IxnEmulationHost):
    """Generated NGPF bgpv4BMacMappedIpList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpv4BMacMappedIpListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpv4BMacMappedIpList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ipType: href
                ipAddress: href
                ipv6Address: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpv4BMacMappedIpListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpEthernetSegmentV4","bgpv4BMacMappedIpList"], vport_name, emulation_host, filters)


class IxnBgpv6BMacMappedIpListEmulation(IxnEmulationHost):
    """Generated NGPF bgpv6BMacMappedIpList emulation host """


    def __init__(self, ixnhttp):
        super(IxnBgpv6BMacMappedIpListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bgpv6BMacMappedIpList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ipType: href
                ipAddress: href
                ipv6Address: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBgpv6BMacMappedIpListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpEthernetSegmentV6","bgpv6BMacMappedIpList"], vport_name, emulation_host, filters)


class IxnBridgeDataEmulation(IxnEmulationHost):
    """Generated NGPF bridgeData emulation host """


    def __init__(self, ixnhttp):
        super(IxnBridgeDataEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bridgeData emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                systemId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBridgeDataEmulation, self).find(["topology","deviceGroup","bridgeData"], vport_name, emulation_host, filters)


class IxnBroadcastDomainV4Emulation(IxnEmulationHost):
    """Generated NGPF broadcastDomainV4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBroadcastDomainV4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific broadcastDomainV4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                remoteServiceId: href
                includeVpwsL2AttrExtComm: href
                primaryPE: href
                backupFlag: href
                requireCW: href
                l2Mtu: href
                fxcType: href
                vidNormalization: href
                groupAddress: href
                senderAddressPRootNodeAddress: href
                ethernetTagId: href
                adRouteLabel: href
                enableVlanAwareService: href
                usebVlan: bool
                bVlanId: href
                bVlanPriority: href
                bVlanTpid: href
                noOfMacPools: number
                rsvpP2mpId: href
                rsvpP2mpIdAsNumber: href
                rsvpTunnelId: href
                rootAddress: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBroadcastDomainV4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","bgpIpv4Peer","bgpIPv4EvpnVpws","broadcastDomainV4"], vport_name, emulation_host, filters)


class IxnBroadcastDomainV6Emulation(IxnEmulationHost):
    """Generated NGPF broadcastDomainV6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnBroadcastDomainV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific broadcastDomainV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                groupAddress: href
                senderAddressPRootNodeAddress: href
                ethernetTagId: href
                adRouteLabel: href
                enableVlanAwareService: href
                usebVlan: bool
                bVlanId: href
                bVlanPriority: href
                bVlanTpid: href
                noOfMacPools: number
                rsvpP2mpId: href
                rsvpP2mpIdAsNumber: href
                rsvpTunnelId: href
                rootAddress: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBroadcastDomainV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnEvi","broadcastDomainV6"], vport_name, emulation_host, filters)


class IxnBucketsEmulation(IxnEmulationHost):
    """Generated NGPF buckets emulation host """


    def __init__(self, ixnhttp):
        super(IxnBucketsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific buckets emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                multiplier: number
                bucketDescription: href
                weight: href
                watchPort: href
                watchGroup: href
                groupName: string
                groupIndex: list
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnBucketsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","groups","buckets"], vport_name, emulation_host, filters)


class IxnBytesTxEmulation(IxnEmulationHost):
    """Generated NGPF bytesTx emulation host """


    def __init__(self, ixnhttp):
        super(IxnBytesTxEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific bytesTx emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnBytesTxEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueStatLearnedInfo","bytesTx"], vport_name, emulation_host, filters)


class IxnCMacPropertiesEmulation(IxnEmulationHost):
    """Generated NGPF cMacProperties emulation host """


    def __init__(self, ixnhttp):
        super(IxnCMacPropertiesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific cMacProperties emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                peerAddress: href
                eviId: href
                mac: list
                useSameSequenceNumber: href
                advertiseIpv4Address: href
                ipv4AddressPrefixLength: href
                advertiseIpv6Address: href
                ipv6AddressPrefixLength: href
                activeTs: href
                enableStickyStaticFlag: href
                includeDefaultGatewayExtendedCommunity: href
                firstLabelStart: href
                enableSecondLabel: href
                secondLabelStart: href
                labelStep: href
                labelMode: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnCMacPropertiesEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","ospfRouteProperty","evpnIPv4PrefixRange","evpnIPv6PrefixRange","cMacProperties"], vport_name, emulation_host, filters)


class IxnClusterDataEmulation(IxnEmulationHost):
    """Generated NGPF clusterData emulation host """

    STATE_DELETEBINDINGERROR = 'deleteBindingError'
    STATE_DELETEBINDINGTIMEOUT = 'deleteBindingTimeout'
    STATE_DELETELSERROR = 'deleteLsError'
    STATE_DELETELSTIMEOUT = 'deleteLsTimeout'
    STATE_DIFFERENTLSNAME = 'differentLsName'
    STATE_DUPLICATEVLANLSPORT = 'duplicateVlanLsPort'
    STATE_INSERTBINDINGERROR = 'insertBindingError'
    STATE_INSERTBINDINGTIMEOUT = 'insertBindingTimeout'
    STATE_INSERTLSERROR = 'insertLsError'
    STATE_INSERTLSTIMEOUT = 'insertLsTimeout'
    STATE_NONE = 'none'
    STATE_VLANMAPPEDTODIFFERENTLSS = 'vlanMappedToDifferentLSs'

    def __init__(self, ixnhttp):
        super(IxnClusterDataEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific clusterData emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                bindingsCount: number
                attachAtStart: href
                logicalSwitchName: href
                vni: href
                physicalSwitchName: href
                physicalPortName: href
                vlan: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnClusterDataEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ovsdbcontroller","clusterData"], vport_name, emulation_host, filters)


class IxnClusterListEmulation(IxnEmulationHost):
    """Generated NGPF clusterList emulation host """


    def __init__(self, ixnhttp):
        super(IxnClusterListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific clusterList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                clusterId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnClusterListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIpv6L2Site","clusterList"], vport_name, emulation_host, filters)


class IxnConfigFlagsEmulation(IxnEmulationHost):
    """Generated NGPF configFlags emulation host """


    def __init__(self, ixnhttp):
        super(IxnConfigFlagsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific configFlags emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnConfigFlagsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","switchConfigLearnedInfo","configFlags"], vport_name, emulation_host, filters)


class IxnContainerEmulation(IxnEmulationHost):
    """Generated NGPF container emulation host """


    def __init__(self, ixnhttp):
        super(IxnContainerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific container emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnContainerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container"], vport_name, emulation_host, filters)


class IxnDatapathIdBaseEmulation(IxnEmulationHost):
    """Generated NGPF datapathIdBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnDatapathIdBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific datapathIdBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnDatapathIdBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","datapathIdBase"], vport_name, emulation_host, filters)


class IxnDatapathIdHexBaseEmulation(IxnEmulationHost):
    """Generated NGPF datapathIdHexBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnDatapathIdHexBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific datapathIdHexBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnDatapathIdHexBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","datapathIdHexBase"], vport_name, emulation_host, filters)


class IxnDceMCastIpv4GroupListEmulation(IxnEmulationHost):
    """Generated NGPF dceMCastIpv4GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceMCastIpv4GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceMCastIpv4GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceMCastIpv4GroupListEmulation, self).find(["topology","deviceGroup","isisFabricPathRouter","dceMCastIpv4GroupList"], vport_name, emulation_host, filters)


class IxnDceMCastIpv6GroupListEmulation(IxnEmulationHost):
    """Generated NGPF dceMCastIpv6GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceMCastIpv6GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceMCastIpv6GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceMCastIpv6GroupListEmulation, self).find(["topology","deviceGroup","isisFabricPathRouter","dceMCastIpv6GroupList"], vport_name, emulation_host, filters)


class IxnDceMCastMacGroupListEmulation(IxnEmulationHost):
    """Generated NGPF dceMCastMacGroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceMCastMacGroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceMCastMacGroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrCnt: href
                mcastAddrIncr: href
                startUcastAddr: href
                ucastSrcCnt: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceMCastMacGroupListEmulation, self).find(["topology","deviceGroup","isisFabricPathRouter","dceMCastMacGroupList"], vport_name, emulation_host, filters)


class IxnDceNodeTopologyListEmulation(IxnEmulationHost):
    """Generated NGPF dceNodeTopologyList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceNodeTopologyListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceNodeTopologyList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                noOfTreesToCompute: href
                enableFTAG: href
                startFTAGValue: href
                interestedVlanRangeCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceNodeTopologyListEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisDceSimulatedTopologyConfig","dceNodeTopologyList"], vport_name, emulation_host, filters)


class IxnDceSimulatedMCastIpv4GroupListEmulation(IxnEmulationHost):
    """Generated NGPF dceSimulatedMCastIpv4GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceSimulatedMCastIpv4GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceSimulatedMCastIpv4GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceSimulatedMCastIpv4GroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisDceSimRouter","dceSimulatedMCastIpv4GroupList"], vport_name, emulation_host, filters)


class IxnDceSimulatedMCastIpv6GroupListEmulation(IxnEmulationHost):
    """Generated NGPF dceSimulatedMCastIpv6GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceSimulatedMCastIpv6GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceSimulatedMCastIpv6GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceSimulatedMCastIpv6GroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisDceSimRouter","dceSimulatedMCastIpv6GroupList"], vport_name, emulation_host, filters)


class IxnDceSimulatedMCastMacGroupListEmulation(IxnEmulationHost):
    """Generated NGPF dceSimulatedMCastMacGroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceSimulatedMCastMacGroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceSimulatedMCastMacGroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrCnt: href
                mcastAddrIncr: href
                startUcastAddr: href
                ucastSrcCnt: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceSimulatedMCastMacGroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisDceSimRouter","dceSimulatedMCastMacGroupList"], vport_name, emulation_host, filters)


class IxnDceTopologyListEmulation(IxnEmulationHost):
    """Generated NGPF dceTopologyList emulation host """


    def __init__(self, ixnhttp):
        super(IxnDceTopologyListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dceTopologyList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                noOfTreesToCompute: href
                enableFTAG: href
                startFTAGValue: href
                nicknameCount: number
                interestedVlanRangeCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDceTopologyListEmulation, self).find(["topology","deviceGroup","isisFabricPathRouter","dceTopologyList"], vport_name, emulation_host, filters)


class IxnDeviceGroupEmulation(IxnEmulationHost):
    """Generated NGPF deviceGroup emulation host """


    def __init__(self, ixnhttp):
        super(IxnDeviceGroupEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific deviceGroup emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                multiplier: number
                enabled: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnDeviceGroupEmulation, self).find(["topology","deviceGroup"], vport_name, emulation_host, filters)


class IxnDhcp4RelayAgentTlvProfileEmulation(IxnEmulationHost):
    """Generated NGPF dhcp4RelayAgentTlvProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp4RelayAgentTlvProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp4RelayAgentTlvProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp4RelayAgentTlvProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","dhcpv4relayAgent","dhcp4RelayAgentTlvProfile"], vport_name, emulation_host, filters)


class IxnDhcp4ServerSessionsEmulation(IxnEmulationHost):
    """Generated NGPF dhcp4ServerSessions emulation host """

    STATE_EXCESSIVETLVS = 'excessiveTlvs'
    STATE_NONE = 'none'
    STATE_POOLTOOLARGE = 'poolTooLarge'

    def __init__(self, ixnhttp):
        super(IxnDhcp4ServerSessionsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp4ServerSessions emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                defaultLeaseTime: href
                ipAddress: href
                ipAddressIncrement: href
                poolSize: href
                ipPrefix: href
                ipGateway: href
                ipDns1: href
                ipDns2: href
                echoRelayInfo: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp4ServerSessionsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","dhcpv4server","dhcp4ServerSessions"], vport_name, emulation_host, filters)


class IxnDhcp6IanaEmulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6IanaEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6IanaEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana"], vport_name, emulation_host, filters)


class IxnDhcp6Iana1Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana1 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iana1Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana1 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iana1Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana1"], vport_name, emulation_host, filters)


class IxnDhcp6Iana2Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana2 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iana2Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana2 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iana2Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana2"], vport_name, emulation_host, filters)


class IxnDhcp6Iana3Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana3 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iana3Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana3 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iana3Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana3"], vport_name, emulation_host, filters)


class IxnDhcp6Iana4Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iana4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iana4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana4"], vport_name, emulation_host, filters)


class IxnDhcp6Iana5Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana5 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iana5Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana5 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iana5Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana5"], vport_name, emulation_host, filters)


class IxnDhcp6Iana6Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iana6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iana6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana6"], vport_name, emulation_host, filters)


class IxnDhcp6Iana7Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iana7 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iana7Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iana7 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iana7Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iana7"], vport_name, emulation_host, filters)


class IxnDhcp6IapdEmulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6IapdEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6IapdEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd"], vport_name, emulation_host, filters)


class IxnDhcp6Iapd1Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd1 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iapd1Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd1 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iapd1Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd1"], vport_name, emulation_host, filters)


class IxnDhcp6Iapd2Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd2 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iapd2Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd2 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iapd2Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd2"], vport_name, emulation_host, filters)


class IxnDhcp6Iapd3Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd3 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iapd3Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd3 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iapd3Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd3"], vport_name, emulation_host, filters)


class IxnDhcp6Iapd4Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd4 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iapd4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iapd4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd4"], vport_name, emulation_host, filters)


class IxnDhcp6Iapd5Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd5 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iapd5Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd5 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iapd5Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd5"], vport_name, emulation_host, filters)


class IxnDhcp6Iapd6Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd6 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iapd6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iapd6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd6"], vport_name, emulation_host, filters)


class IxnDhcp6Iapd7Emulation(IxnEmulationHost):
    """Generated NGPF dhcp6Iapd7 emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6Iapd7Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6Iapd7 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6Iapd7Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6Iapd7"], vport_name, emulation_host, filters)


class IxnDhcp6LearnedInfoEmulation(IxnEmulationHost):
    """Generated NGPF dhcp6LearnedInfo emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6LearnedInfoEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6LearnedInfo emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                tabbedDiscoveredAddresses: list
                tabbedDiscoveredPrefix: list
                tabbedDiscoveredPrefixLength: list
                tabbedDiscoveredGateways: list
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6LearnedInfoEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client","dhcp6LearnedInfo"], vport_name, emulation_host, filters)


class IxnDhcp6RelayTlvProfileEmulation(IxnEmulationHost):
    """Generated NGPF dhcp6RelayTlvProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6RelayTlvProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6RelayTlvProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6RelayTlvProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","dhcpv6relayAgent","dhcp6RelayTlvProfile"], vport_name, emulation_host, filters)


class IxnDhcp6ServerSessionsEmulation(IxnEmulationHost):
    """Generated NGPF dhcp6ServerSessions emulation host """


    def __init__(self, ixnhttp):
        super(IxnDhcp6ServerSessionsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcp6ServerSessions emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                iaType: href
                ipAddress: href
                ipAddressIncrement: href
                poolSize: href
                ipPrefix: href
                enableAddressMatchDuid: href
                addressDuidMask: href
                addressDuidPattern: href
                addressesPerIA: href
                ipAddressPD: href
                ipPrefixIncrement: href
                poolPrefixSize: href
                prefixLength: href
                enablePrefixMatchDuid: href
                prefixDuidStart: href
                prefixDuidIncrement: href
                prefixesPerIA: href
                defaultLeaseTime: href
                leaseTimeIncrement: href
                useCustomTimes: href
                customRenewTime: href
                customRebindTime: href
                nak: href
                nakMask: href
                nakPattern: href
                ignore: href
                ignoreMask: href
                ignorePattern: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDhcp6ServerSessionsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","dhcpv6server","dhcp6ServerSessions"], vport_name, emulation_host, filters)


class IxnDhcpv4clientEmulation(IxnEmulationHost):
    """Generated NGPF dhcpv4client emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnDhcpv4clientEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcpv4client emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                discoveredAddresses: list
                discoveredPrefix: list
                discoveredGateways: list
                dhcp4GatewayAddress: href
                dhcp4GatewayMac: href
                renewTimer: href
                useRapidCommit: href
                dhcp4UseFirstServer: href
                dhcp4ServerAddress: href
                dhcp4Broadcast: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnDhcpv4clientEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv4client"], vport_name, emulation_host, filters)

    def rebind(self, expected_state=None, timeout=None):
        """Rebind selected DHCP items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4clientEmulation, self).call_operation('rebind', expected_state, timeout)

    def renew(self, expected_state=None, timeout=None):
        """Renew selected DHCP items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4clientEmulation, self).call_operation('renew', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4clientEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send ping for selected DHCP items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4clientEmulation, self).call_operation('sendPing', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4clientEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4clientEmulation, self).call_operation('stop', expected_state, timeout)


class IxnDhcpv4relayAgentEmulation(IxnEmulationHost):
    """Generated NGPF dhcpv4relayAgent emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnDhcpv4relayAgentEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcpv4relayAgent emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                dhcp4RelayAgentGlobalAndPortData: href
                dhcp4RelayAddress: href
                dhcp4ServerAddress: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnDhcpv4relayAgentEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","dhcpv4relayAgent"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4relayAgentEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4relayAgentEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4relayAgentEmulation, self).call_operation('stop', expected_state, timeout)


class IxnDhcpv4serverEmulation(IxnEmulationHost):
    """Generated NGPF dhcpv4server emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnDhcpv4serverEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcpv4server emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                useRapidCommit: href
                subnetAddrAssign: href
                subnet: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnDhcpv4serverEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","dhcpv4server"], vport_name, emulation_host, filters)

    def forcerenew(self, expected_state=None, timeout=None):
        """Send Force Renew for selected DHCPv4 Server items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4serverEmulation, self).call_operation('forceRenew', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4serverEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4serverEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv4serverEmulation, self).call_operation('stop', expected_state, timeout)


class IxnDhcpv6clientEmulation(IxnEmulationHost):
    """Generated NGPF dhcpv6client emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnDhcpv6clientEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcpv6client emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                discoveredAddresses: list
                discoveredPrefix: list
                discoveredPrefixLength: list
                discoveredGateways: list
                renewTimer: href
                useRapidCommit: href
                dhcp6DuidType: href
                dhcp6DuidEnterpriseId: href
                dhcp6DuidVendorId: href
                dhcp6IaType: href
                dhcp6UsePDGlobalAddress: href
                dhcp6IaId: href
                dhcp6IaIdInc: href
                dhcp6IaT1: href
                dhcp6IaT2: href
                enableStateless: bool
                dhcp6GatewayAddress: href
                dhcp6GatewayMac: href
                noOfAddresses: list
                noOfPrefixes: list
                dhcp6IANACount: href
                dhcp6IAPDCount: href
                maxNoPerClient: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnDhcpv6clientEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","dhcpv6client"], vport_name, emulation_host, filters)

    def rebind(self, expected_state=None, timeout=None):
        """Rebind selected DHCPv6 items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6clientEmulation, self).call_operation('rebind', expected_state, timeout)

    def renew(self, expected_state=None, timeout=None):
        """Renew selected DHCPv6 items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6clientEmulation, self).call_operation('renew', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6clientEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send ping for selected DHCPv6 items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6clientEmulation, self).call_operation('sendPing', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6clientEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6clientEmulation, self).call_operation('stop', expected_state, timeout)


class IxnDhcpv6relayAgentEmulation(IxnEmulationHost):
    """Generated NGPF dhcpv6relayAgent emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnDhcpv6relayAgentEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcpv6relayAgent emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                dhcp6RelayAgentGlobalAndPortData: href
                dhcp6RelayAddress: href
                dhcp6ServerAddress: href
                lightweightDhcp6RelayAgentGlobalAndPortData: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnDhcpv6relayAgentEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","dhcpv6relayAgent"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6relayAgentEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6relayAgentEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6relayAgentEmulation, self).call_operation('stop', expected_state, timeout)


class IxnDhcpv6serverEmulation(IxnEmulationHost):
    """Generated NGPF dhcpv6server emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnDhcpv6serverEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dhcpv6server emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                useRapidCommit: href
                subnetAddrAssign: href
                ipDns1: href
                ipDns2: href
                dnsDomain: href
                poolCount: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnDhcpv6serverEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","dhcpv6server"], vport_name, emulation_host, filters)

    def reconfigure(self, expected_state=None, timeout=None):
        """Send Reconfigure for selected DHCPv6 Server items.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6serverEmulation, self).call_operation('reconfigure', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6serverEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6serverEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnDhcpv6serverEmulation, self).call_operation('stop', expected_state, timeout)


class IxnDslPoolsEmulation(IxnEmulationHost):
    """Generated NGPF dslPools emulation host """

    STATE_DISABLED = 'disabled'
    STATE_IDLE = 'idle'
    STATE_NONE = 'none'
    STATE_SHOWTIME = 'showTime'
    STATE_SILENT = 'silent'
    STATE_TLVNA = 'tlvNa'

    def __init__(self, ixnhttp):
        super(IxnDslPoolsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific dslPools emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portUpSent: list
                portDownSent: list
                vlanAllocationModel: href
                innerVlanId: href
                outerVlanId: href
                circuitId: href
                enableRemoteId: href
                remoteId: href
                flappingMode: href
                lineUpInterval: href
                lineDownInterval: href
                actualNetDataRateUpstreamTolerance: href
                actualNetDataRateDownstreamTolerance: href
                actualBandwidthUpstream: list
                actualBandwidthDownstream: list
                enableDslType: href
                dslType: href
                enableActualNetDataRateUpstream: href
                actualNetDataRateUpstream: href
                enableActualNetDataRateDownstream: href
                actualNetDataRateDownstream: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnDslPoolsEmulation, self).find(["topology","deviceGroup","networkGroup","dslPools"], vport_name, emulation_host, filters)

    def sendportdown(self, expected_state=None, timeout=None):
        """Send Port Down event from selected Access Loop items.
            For expected_state options see the class state variables
        """
        super(IxnDslPoolsEmulation, self).call_operation('sendPortDown', expected_state, timeout)

    def sendportup(self, expected_state=None, timeout=None):
        """Send Port Up event from selected Access Loop items.
            For expected_state options see the class state variables
        """
        super(IxnDslPoolsEmulation, self).call_operation('sendPortUp', expected_state, timeout)


class IxnDurationNSecEmulation(IxnEmulationHost):
    """Generated NGPF durationNSec emulation host """


    def __init__(self, ixnhttp):
        super(IxnDurationNSecEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific durationNSec emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnDurationNSecEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueStatLearnedInfo","durationNSec"], vport_name, emulation_host, filters)


class IxnDurationSecEmulation(IxnEmulationHost):
    """Generated NGPF durationSec emulation host """


    def __init__(self, ixnhttp):
        super(IxnDurationSecEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific durationSec emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnDurationSecEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueStatLearnedInfo","durationSec"], vport_name, emulation_host, filters)


class IxnErrorCodeBaseEmulation(IxnEmulationHost):
    """Generated NGPF errorCodeBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnErrorCodeBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific errorCodeBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnErrorCodeBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","errorCodeBase"], vport_name, emulation_host, filters)


class IxnErrorTypeBaseEmulation(IxnEmulationHost):
    """Generated NGPF errorTypeBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnErrorTypeBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific errorTypeBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnErrorTypeBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","errorTypeBase"], vport_name, emulation_host, filters)


class IxnErrorsTxEmulation(IxnEmulationHost):
    """Generated NGPF errorsTx emulation host """


    def __init__(self, ixnhttp):
        super(IxnErrorsTxEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific errorsTx emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnErrorsTxEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueStatLearnedInfo","errorsTx"], vport_name, emulation_host, filters)


class IxnEthernetEmulation(IxnEmulationHost):
    """Generated NGPF ethernet emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnEthernetEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ethernet emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                mac: href
                mtu: href
                notifyMACMove: bool
                enableVlans: href
                vlanCount: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnEthernetEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnEthernetEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnEthernetEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnEthernetEmulation, self).call_operation('stop', expected_state, timeout)


class IxnEvpnIPv4PrefixRangeEmulation(IxnEmulationHost):
    """Generated NGPF evpnIPv4PrefixRange emulation host """


    def __init__(self, ixnhttp):
        super(IxnEvpnIPv4PrefixRangeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific evpnIPv4PrefixRange emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ipv4Address: list
                labelStart: href
                labelStep: href
                labelMode: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnEvpnIPv4PrefixRangeEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","ospfRouteProperty","evpnIPv4PrefixRange"], vport_name, emulation_host, filters)


class IxnEvpnIPv6PrefixRangeEmulation(IxnEmulationHost):
    """Generated NGPF evpnIPv6PrefixRange emulation host """


    def __init__(self, ixnhttp):
        super(IxnEvpnIPv6PrefixRangeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific evpnIPv6PrefixRange emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ipv6Address: list
                labelStart: href
                labelStep: href
                labelMode: href
                enableNextHop: href
                setNextHop: href
                setNextHopIpType: href
                ipv4NextHop: href
                ipv6NextHop: href
                enableOrigin: href
                origin: href
                enableLocalPreference: href
                localPreference: href
                enableMultiExitDiscriminator: href
                multiExitDiscriminator: href
                enableAtomicAggregate: href
                enableAggregatorId: href
                aggregatorId: href
                aggregatorAs: href
                enableOriginatorId: href
                originatorId: href
                enableCommunity: href
                noOfCommunities: number
                enableExtendedCommunity: href
                noOfExtendedCommunity: number
                overridePeerAsSetMode: href
                asSetMode: href
                enableAsPathSegments: href
                noOfASPathSegmentsPerRouteRange: number
                enableCluster: href
                noOfClusters: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnEvpnIPv6PrefixRangeEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","ospfRouteProperty","evpnIPv4PrefixRange","evpnIPv6PrefixRange"], vport_name, emulation_host, filters)


class IxnExpectedInitiatedLspListEmulation(IxnEmulationHost):
    """Generated NGPF expectedInitiatedLspList emulation host """


    def __init__(self, ixnhttp):
        super(IxnExpectedInitiatedLspListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific expectedInitiatedLspList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                symbolicPathName: href
                sourceIpv4Address: href
                sourceIpv6Address: href
                maxExpectedSegmentCount: number
                insertIpv6ExplicitNull: bool
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnExpectedInitiatedLspListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcc","expectedInitiatedLspList"], vport_name, emulation_host, filters)


class IxnExperimenterDataEmulation(IxnEmulationHost):
    """Generated NGPF experimenterData emulation host """


    def __init__(self, ixnhttp):
        super(IxnExperimenterDataEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific experimenterData emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnExperimenterDataEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","experimenterData"], vport_name, emulation_host, filters)


class IxnExperimenterDataLengthEmulation(IxnEmulationHost):
    """Generated NGPF experimenterDataLength emulation host """


    def __init__(self, ixnhttp):
        super(IxnExperimenterDataLengthEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific experimenterDataLength emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnExperimenterDataLengthEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","experimenterDataLength"], vport_name, emulation_host, filters)


class IxnExperimenterIDEmulation(IxnEmulationHost):
    """Generated NGPF experimenterID emulation host """


    def __init__(self, ixnhttp):
        super(IxnExperimenterIDEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific experimenterID emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnExperimenterIDEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","experimenterID"], vport_name, emulation_host, filters)


class IxnExternalLinkEmulation(IxnEmulationHost):
    """Generated NGPF externalLink emulation host """


    def __init__(self, ixnhttp):
        super(IxnExternalLinkEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific externalLink emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                fromNodeIndex: number
                toNetworkTopology: href
                toNodeIndex: number
        """
        return super(IxnExternalLinkEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","externalLink"], vport_name, emulation_host, filters)


class IxnExternalRoutesEmulation(IxnEmulationHost):
    """Generated NGPF externalRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnExternalRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific externalRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                eBit: href
                refLSType: href
                fBit: href
                forwardingAddress: href
                tBit: href
                externalRouteTag: href
                referencedLinkStateId: href
                metric: href
                unusedBit7: href
                unusedBit6: href
                unusedBit5: href
                unusedBit4: href
                pBit: href
                mCBit: href
                lABit: href
                nUBit: href
                linkStateId: href
                linkStateIdStep: href
                active: href
                networkAddress: href
                rangeSize: href
                prefix: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnExternalRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfv3PseudoRouter","externalRoutes"], vport_name, emulation_host, filters)


class IxnFieldEmulation(IxnEmulationHost):
    """Generated NGPF field emulation host """


    def __init__(self, ixnhttp):
        super(IxnFieldEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific field emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                encoding: enum
                size: number
                value: href
                singleValue: bool
                enum: string
                sizeType: enum
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnFieldEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","packetOutActionProfile","actionList","action","field"], vport_name, emulation_host, filters)


class IxnFlowAggrMatchProfileEmulation(IxnEmulationHost):
    """Generated NGPF flowAggrMatchProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnFlowAggrMatchProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific flowAggrMatchProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnFlowAggrMatchProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","flowAggrMatchProfile"], vport_name, emulation_host, filters)


class IxnFlowProfileEmulation(IxnEmulationHost):
    """Generated NGPF flowProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnFlowProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific flowProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnFlowProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","tables","flowSet","flowProfile"], vport_name, emulation_host, filters)


class IxnFlowRemovedMasterEmulation(IxnEmulationHost):
    """Generated NGPF flowRemovedMaster emulation host """


    def __init__(self, ixnhttp):
        super(IxnFlowRemovedMasterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific flowRemovedMaster emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnFlowRemovedMasterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","asyncConfStatLearnedInfo","flowRemovedMaster"], vport_name, emulation_host, filters)


class IxnFlowRemovedSlaveEmulation(IxnEmulationHost):
    """Generated NGPF flowRemovedSlave emulation host """


    def __init__(self, ixnhttp):
        super(IxnFlowRemovedSlaveEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific flowRemovedSlave emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnFlowRemovedSlaveEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","asyncConfStatLearnedInfo","flowRemovedSlave"], vport_name, emulation_host, filters)


class IxnFlowSetEmulation(IxnEmulationHost):
    """Generated NGPF flowSet emulation host """


    def __init__(self, ixnhttp):
        super(IxnFlowSetEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific flowSet emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                flowSetId: string
                numberOfFlows: number
                cookie: href
                cookieMask: href
                flowFlags: href
                idleTimeout: href
                hardTimeout: href
                flowMatchType: href
                priority: href
                flowAdvertise: bool
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnFlowSetEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","tables","flowSet"], vport_name, emulation_host, filters)


class IxnFlowStatMatchProfileEmulation(IxnEmulationHost):
    """Generated NGPF flowStatMatchProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnFlowStatMatchProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific flowStatMatchProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnFlowStatMatchProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","flowStatMatchProfile"], vport_name, emulation_host, filters)


class IxnGeneveEmulation(IxnEmulationHost):
    """Generated NGPF geneve emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnGeneveEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific geneve emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                vni: href
                ipv4Remote: href
                udpDestPort: href
                enableUdpCsum: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnGeneveEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","geneve"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnGeneveEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnGeneveEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnGeneveEmulation, self).call_operation('stop', expected_state, timeout)


class IxnGreoipv4Emulation(IxnEmulationHost):
    """Generated NGPF greoipv4 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnGreoipv4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific greoipv4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srcIp: href
                destIp: href
                enableChecksum: href
                enableKey: href
                inKey: href
                outKey: href
                enableSequenceNumber: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnGreoipv4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnGreoipv4Emulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnGreoipv4Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnGreoipv4Emulation, self).call_operation('stop', expected_state, timeout)


class IxnGreoipv6Emulation(IxnEmulationHost):
    """Generated NGPF greoipv6 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnGreoipv6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific greoipv6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srcIp: href
                destIp: href
                enableChecksum: href
                enableKey: href
                inKey: href
                outKey: href
                enableSequenceNumber: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnGreoipv6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnGreoipv6Emulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnGreoipv6Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnGreoipv6Emulation, self).call_operation('stop', expected_state, timeout)


class IxnGroupsEmulation(IxnEmulationHost):
    """Generated NGPF groups emulation host """


    def __init__(self, ixnhttp):
        super(IxnGroupsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific groups emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                multiplier: number
                ofChannel: href
                groupDescription: href
                numberOfBuckets: number
                groupId: href
                groupType: href
                groupAdvertise: href
                channelName: string
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnGroupsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","groups"], vport_name, emulation_host, filters)


class IxnIgmpHostEmulation(IxnEmulationHost):
    """Generated NGPF igmpHost emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIgmpHostEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific igmpHost emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                versionType: href
                noOfGrpRanges: number
                routerAlert: href
                gQResponseMode: href
                gSResponseMode: href
                uSResponseMode: href
                reportFreq: href
                imResponse: href
                jlMultiplier: number
                enableProxyReporting: href
                enableIptv: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIgmpHostEmulation, self).find(["topology","deviceGroup","ipv4Loopback","igmpHost"], vport_name, emulation_host, filters)

    def igmpstarthost(self, expected_state=None, timeout=None):
        """Start IGMP Host
            For expected_state options see the class state variables
        """
        super(IxnIgmpHostEmulation, self).call_operation('igmpStartHost', expected_state, timeout)

    def igmpstophost(self, expected_state=None, timeout=None):
        """Stop IGMP Host
            For expected_state options see the class state variables
        """
        super(IxnIgmpHostEmulation, self).call_operation('igmpStopHost', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIgmpHostEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIgmpHostEmulation, self).call_operation('start', expected_state, timeout)

    def startigmp(self, expected_state=None, timeout=None):
        """Start IGMP protocol in selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnIgmpHostEmulation, self).call_operation('startIGMP', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIgmpHostEmulation, self).call_operation('stop', expected_state, timeout)

    def stopigmp(self, expected_state=None, timeout=None):
        """Stop IGMP protocol in selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnIgmpHostEmulation, self).call_operation('stopIGMP', expected_state, timeout)


class IxnIgmpMcastIPv4GroupListEmulation(IxnEmulationHost):
    """Generated NGPF igmpMcastIPv4GroupList emulation host """

    STATE_IPTV = 'iptv'
    STATE_JOINED = 'joined'
    STATE_NOTJOINED = 'notJoined'
    STATE_NOTSTARTED = 'notStarted'

    def __init__(self, ixnhttp):
        super(IxnIgmpMcastIPv4GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific igmpMcastIPv4GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startMcastAddr: href
                mcastAddrIncr: href
                sourceMode: href
                noOfSrcRanges: number
                mcastAddrCnt: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIgmpMcastIPv4GroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","igmpHost","igmpMcastIPv4GroupList"], vport_name, emulation_host, filters)

    def igmpjoingroup(self, expected_state=None, timeout=None):
        """Join Group
            For expected_state options see the class state variables
        """
        super(IxnIgmpMcastIPv4GroupListEmulation, self).call_operation('igmpJoinGroup', expected_state, timeout)

    def igmpleavegroup(self, expected_state=None, timeout=None):
        """Leave Group
            For expected_state options see the class state variables
        """
        super(IxnIgmpMcastIPv4GroupListEmulation, self).call_operation('igmpLeaveGroup', expected_state, timeout)


class IxnIgmpQuerierEmulation(IxnEmulationHost):
    """Generated NGPF igmpQuerier emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIgmpQuerierEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific igmpQuerier emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                versionType: href
                startupQueryCount: href
                generalQueryInterval: href
                routerAlert: href
                robustnessVariable: href
                generalQueryResponseInterval: href
                specificQueryResponseInterval: href
                specificQueryTransmissionCount: href
                supportElection: href
                supportOlderVersionHost: href
                supportOlderVersionQuerier: href
                discardLearntInfo: href
                proxyQuerier: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIgmpQuerierEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","igmpQuerier"], vport_name, emulation_host, filters)

    def igmpgetlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('igmpGetLearnedInfo', expected_state, timeout)

    def igmpresumeperiodicgenquery(self, expected_state=None, timeout=None):
        """Resume Periodic General Query
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('igmpResumePeriodicGenQuery', expected_state, timeout)

    def igmpstartquerier(self, expected_state=None, timeout=None):
        """Start IGMP Querier
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('igmpStartQuerier', expected_state, timeout)

    def igmpstopperiodicgenquery(self, expected_state=None, timeout=None):
        """Stop Periodic General Query
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('igmpStopPeriodicGenQuery', expected_state, timeout)

    def igmpstopquerier(self, expected_state=None, timeout=None):
        """Stop IGMP Querier
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('igmpStopQuerier', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('start', expected_state, timeout)

    def startigmp(self, expected_state=None, timeout=None):
        """Start IGMP protocol in selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('startIGMP', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('stop', expected_state, timeout)

    def stopigmp(self, expected_state=None, timeout=None):
        """Stop IGMP protocol in selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnIgmpQuerierEmulation, self).call_operation('stopIGMP', expected_state, timeout)


class IxnIgmpUcastIPv4SourceListEmulation(IxnEmulationHost):
    """Generated NGPF igmpUcastIPv4SourceList emulation host """

    STATE_IPTV = 'iptv'
    STATE_JOINED = 'joined'
    STATE_NOTJOINED = 'notJoined'
    STATE_NOTSTARTED = 'notStarted'

    def __init__(self, ixnhttp):
        super(IxnIgmpUcastIPv4SourceListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific igmpUcastIPv4SourceList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startUcastAddr: href
                ucastAddrIncr: href
                ucastSrcAddrCnt: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIgmpUcastIPv4SourceListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","igmpHost","igmpMcastIPv4GroupList","igmpUcastIPv4SourceList"], vport_name, emulation_host, filters)

    def igmpjoinsource(self, expected_state=None, timeout=None):
        """Join Source
            For expected_state options see the class state variables
        """
        super(IxnIgmpUcastIPv4SourceListEmulation, self).call_operation('igmpJoinSource', expected_state, timeout)

    def igmpleavesource(self, expected_state=None, timeout=None):
        """Leave Source
            For expected_state options see the class state variables
        """
        super(IxnIgmpUcastIPv4SourceListEmulation, self).call_operation('igmpLeaveSource', expected_state, timeout)


class IxnInstructionEmulation(IxnEmulationHost):
    """Generated NGPF instruction emulation host """


    def __init__(self, ixnhttp):
        super(IxnInstructionEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific instruction emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnInstructionEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","tables","flowSet","flowProfile","matchAction","instructions","instruction"], vport_name, emulation_host, filters)


class IxnInstructionsEmulation(IxnEmulationHost):
    """Generated NGPF instructions emulation host """


    def __init__(self, ixnhttp):
        super(IxnInstructionsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific instructions emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnInstructionsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","tables","flowSet","flowProfile","matchAction","instructions"], vport_name, emulation_host, filters)


class IxnInterAreaPrefixEmulation(IxnEmulationHost):
    """Generated NGPF interAreaPrefix emulation host """


    def __init__(self, ixnhttp):
        super(IxnInterAreaPrefixEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific interAreaPrefix emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                unusedBit7: href
                unusedBit6: href
                unusedBit5: href
                unusedBit4: href
                pBit: href
                mCBit: href
                lABit: href
                nUBit: href
                linkStateId: href
                linkStateIdStep: href
                active: href
                networkAddress: href
                rangeSize: href
                prefix: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnInterAreaPrefixEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfv3PseudoRouter","interAreaPrefix"], vport_name, emulation_host, filters)


class IxnInterAreaRouterEmulation(IxnEmulationHost):
    """Generated NGPF interAreaRouter emulation host """


    def __init__(self, ixnhttp):
        super(IxnInterAreaRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific interAreaRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                metric: href
                linkStateId: href
                linkStateIdStep: href
                rangeSize: href
                reservedBit7: href
                reservedBit6: href
                dCBit: href
                rBit: href
                nBit: href
                mCBit: href
                eBit: href
                v6Bit: href
                destRouterId: href
                destRouterIdPrefix: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnInterAreaRouterEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfv3PseudoRouter","interAreaRouter"], vport_name, emulation_host, filters)


class IxnInterestedVlanListEmulation(IxnEmulationHost):
    """Generated NGPF interestedVlanList emulation host """


    def __init__(self, ixnhttp):
        super(IxnInterestedVlanListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific interestedVlanList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nickname: href
                includeInLSP: href
                includeInMGroupPDU: href
                startVlanId: href
                vlanIdIncr: href
                vlanCount: href
                m4BitEnabled: href
                m6BitEnabled: href
                noOfSpanningTreeRoots: href
                startSpanningTreeRootBridgeId: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnInterestedVlanListEmulation, self).find(["topology","deviceGroup","isisFabricPathRouter","dceTopologyList","interestedVlanList"], vport_name, emulation_host, filters)


class IxnIntraAreaPrefixEmulation(IxnEmulationHost):
    """Generated NGPF intraAreaPrefix emulation host """


    def __init__(self, ixnhttp):
        super(IxnIntraAreaPrefixEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific intraAreaPrefix emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                refLSType: href
                referencedLinkStateId: href
                referencedRouterId: href
                metric: href
                unusedBit7: href
                unusedBit6: href
                unusedBit5: href
                unusedBit4: href
                pBit: href
                mCBit: href
                lABit: href
                nUBit: href
                linkStateId: href
                linkStateIdStep: href
                active: href
                networkAddress: href
                rangeSize: href
                prefix: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIntraAreaPrefixEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfv3PseudoRouter","intraAreaPrefix"], vport_name, emulation_host, filters)


class IxnIptvEmulation(IxnEmulationHost):
    """Generated NGPF iptv emulation host """

    STATE_NOTSTARTED = 'notStarted'
    STATE_STARTED = 'started'

    def __init__(self, ixnhttp):
        super(IxnIptvEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific iptv emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                stbLeaveJoinDelay: href
                joinLatencyThreshold: href
                leaveLatencyThreshold: href
                logFailureTimestamps: href
                logAllTimestamps: href
                zapBehavior: href
                zapDirection: href
                zapIntervalType: href
                zapInterval: href
                numChannelChangesBeforeView: href
                viewDuration: href
                enableGeneralQueryResponse: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIptvEmulation, self).find(["topology","deviceGroup","ipv4Loopback","igmpHost","iptv"], vport_name, emulation_host, filters)

    def startiptv(self, expected_state=None, timeout=None):
        """Start IPTV
            For expected_state options see the class state variables
        """
        super(IxnIptvEmulation, self).call_operation('startIptv', expected_state, timeout)

    def stopiptv(self, expected_state=None, timeout=None):
        """Stop IPTV
            For expected_state options see the class state variables
        """
        super(IxnIptvEmulation, self).call_operation('stopIptv', expected_state, timeout)


class IxnIpv4Emulation(IxnEmulationHost):
    """Generated NGPF ipv4 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIpv4Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv4 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                address: href
                prefix: href
                gatewayIp: href
                resolveGateway: href
                resolvedGatewayMac: list
                manualGatewayMac: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIpv4Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIpv4Emulation, self).call_operation('restartDown', expected_state, timeout)

    def sendarp(self, expected_state=None, timeout=None):
        """Send ARP request to configured gateway IP to resolve Gateway MAC for selected items.
            For expected_state options see the class state variables
        """
        super(IxnIpv4Emulation, self).call_operation('sendArp', expected_state, timeout)

    def sendarpmanual(self, expected_state=None, timeout=None):
        """Send ARP request to specified IP for selected IPv4 items.
            For expected_state options see the class state variables
        """
        super(IxnIpv4Emulation, self).call_operation('sendArpManual', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send ping for selected IPv4 items.
            For expected_state options see the class state variables
        """
        super(IxnIpv4Emulation, self).call_operation('sendPing', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv4Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv4Emulation, self).call_operation('stop', expected_state, timeout)


class IxnIpv4LoopbackEmulation(IxnEmulationHost):
    """Generated NGPF ipv4Loopback emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIpv4LoopbackEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv4Loopback emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                address: href
                prefix: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIpv4LoopbackEmulation, self).find(["topology","deviceGroup","ipv4Loopback"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIpv4LoopbackEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send ping for selected IPv4 Loopback items.
            For expected_state options see the class state variables
        """
        super(IxnIpv4LoopbackEmulation, self).call_operation('sendPing', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv4LoopbackEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv4LoopbackEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIpv4PrefixPoolsEmulation(IxnEmulationHost):
    """Generated NGPF ipv4PrefixPools emulation host """


    def __init__(self, ixnhttp):
        super(IxnIpv4PrefixPoolsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv4PrefixPools emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                networkAddress: href
                prefixLength: href
                prefixAddrStep: href
                addrStepSupported: bool
                numberOfAddresses: number
                lastNetworkAddress: list
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIpv4PrefixPoolsEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv4PrefixPools"], vport_name, emulation_host, filters)


class IxnIpv6Emulation(IxnEmulationHost):
    """Generated NGPF ipv6 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIpv6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                address: href
                prefix: href
                gatewayIp: href
                resolveGateway: href
                resolvedGatewayMac: list
                manualGatewayMac: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIpv6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIpv6Emulation, self).call_operation('restartDown', expected_state, timeout)

    def sendns(self, expected_state=None, timeout=None):
        """Send Neighbor Solicitation request to configured gateway IP address to resolve Gateway MAC for selected items.
            For expected_state options see the class state variables
        """
        super(IxnIpv6Emulation, self).call_operation('sendNs', expected_state, timeout)

    def sendnsmanual(self, expected_state=None, timeout=None):
        """Send Neighbor Solicitation request to specified IP address for selected items.
            For expected_state options see the class state variables
        """
        super(IxnIpv6Emulation, self).call_operation('sendNsManual', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send ping for selected IPv6 items.
            For expected_state options see the class state variables
        """
        super(IxnIpv6Emulation, self).call_operation('sendPing', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6Emulation, self).call_operation('stop', expected_state, timeout)


class IxnIpv6AutoconfigurationEmulation(IxnEmulationHost):
    """Generated NGPF ipv6Autoconfiguration emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIpv6AutoconfigurationEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv6Autoconfiguration emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                address: list
                prefix: list
                gatewayIp: list
                resolvedGatewayMac: list
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIpv6AutoconfigurationEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIpv6AutoconfigurationEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendns(self, expected_state=None, timeout=None):
        """Send NS for selected IPv6 Autoconfig items.
            For expected_state options see the class state variables
        """
        super(IxnIpv6AutoconfigurationEmulation, self).call_operation('sendNs', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send ping for selected IPv6 Autoconfig items.
            For expected_state options see the class state variables
        """
        super(IxnIpv6AutoconfigurationEmulation, self).call_operation('sendPing', expected_state, timeout)

    def sendrs(self, expected_state=None, timeout=None):
        """Send RS for selected IPv6 Autoconfig items.
            For expected_state options see the class state variables
        """
        super(IxnIpv6AutoconfigurationEmulation, self).call_operation('sendRs', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6AutoconfigurationEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6AutoconfigurationEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIpv6LoopbackEmulation(IxnEmulationHost):
    """Generated NGPF ipv6Loopback emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIpv6LoopbackEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv6Loopback emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                address: href
                prefix: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIpv6LoopbackEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIpv6LoopbackEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send ping for selected IPv6 Loopback items.
            For expected_state options see the class state variables
        """
        super(IxnIpv6LoopbackEmulation, self).call_operation('sendPing', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6LoopbackEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6LoopbackEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIpv6PrefixPoolsEmulation(IxnEmulationHost):
    """Generated NGPF ipv6PrefixPools emulation host """


    def __init__(self, ixnhttp):
        super(IxnIpv6PrefixPoolsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv6PrefixPools emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                networkAddress: href
                prefixLength: href
                prefixAddrStep: href
                addrStepSupported: bool
                numberOfAddresses: number
                lastNetworkAddress: list
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIpv6PrefixPoolsEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools"], vport_name, emulation_host, filters)


class IxnIpv6srEmulation(IxnEmulationHost):
    """Generated NGPF ipv6sr emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIpv6srEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ipv6sr emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                tunnelDescription: href
                cleanupFlag: href
                protectedFlag: href
                oamFlag: href
                useAsIngress: href
                outerSrcAddr: href
                outerDestAddr: href
                segmentsLeft: href
                firstSegment: href
                numberSegments: number
                sIDEnable0: href
                sID0: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIpv6srEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","ipv6sr"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIpv6srEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6srEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIpv6srEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsidListEmulation(IxnEmulationHost):
    """Generated NGPF isidList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsidListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isidList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                baseVid: href
                itagEthernetType: href
                isid: href
                transmissionType: href
                tbit: href
                rbit: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsidListEmulation, self).find(["topology","deviceGroup","isisSpbRouter","spbTopologyList","baseVidList","isidList"], vport_name, emulation_host, filters)


class IxnIsisDcePseudoIfaceAttPoint1ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisDcePseudoIfaceAttPoint1Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisDcePseudoIfaceAttPoint1ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisDcePseudoIfaceAttPoint1Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisDcePseudoIfaceAttPoint1ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisDcePseudoIfaceAttPoint1Config"], vport_name, emulation_host, filters)


class IxnIsisDcePseudoIfaceAttPoint2ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisDcePseudoIfaceAttPoint2Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisDcePseudoIfaceAttPoint2ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisDcePseudoIfaceAttPoint2Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisDcePseudoIfaceAttPoint2ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisDcePseudoIfaceAttPoint2Config"], vport_name, emulation_host, filters)


class IxnIsisDcePseudoNodeEmulation(IxnEmulationHost):
    """Generated NGPF isisDcePseudoNode emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisDcePseudoNodeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisDcePseudoNode emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nickname: href
                broadcastRootPriority: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisDcePseudoNodeEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouterBridge","isisDcePseudoNode"], vport_name, emulation_host, filters)


class IxnIsisDceSimRouterEmulation(IxnEmulationHost):
    """Generated NGPF isisDceSimRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisDceSimRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisDceSimRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                systemId: href
                nickname: href
                broadcastRootPriority: href
                dceMCastMacGroupCount: number
                dceMCastIpv4GroupCount: number
                dceMCastIpv6GroupCount: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisDceSimRouterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisDceSimRouter"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisDceSimRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisDceSimRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisDceSimRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsisDceSimulatedTopologyConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisDceSimulatedTopologyConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisDceSimulatedTopologyConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisDceSimulatedTopologyConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                dceNodeTopologyCount: number
                enableHostName: href
                hostName: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisDceSimulatedTopologyConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisDceSimulatedTopologyConfig"], vport_name, emulation_host, filters)


class IxnIsisFabricPathEmulation(IxnEmulationHost):
    """Generated NGPF isisFabricPath emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisFabricPathEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisFabricPath emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceMetric: href
                networkType: href
                levelType: href
                enable3WayHandshake: href
                extendedLocalCircuitId: href
                level1HelloInterval: href
                level1DeadInterval: href
                localSystemID: list
                enableConfiguredHoldTime: href
                configuredHoldTime: href
                authType: href
                circuitTranmitPasswordOrMD5Key: href
                autoAdjustMTU: href
                autoAdjustArea: href
                autoAdjustSupportedProtocols: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisFabricPathEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisFabricPath"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def isisstartinterface(self, expected_state=None, timeout=None):
        """Start ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('isisStartInterface', expected_state, timeout)

    def isisstopinterface(self, expected_state=None, timeout=None):
        """Stop ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('isisStopInterface', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('resumeHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('stop', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathEmulation, self).call_operation('stopHello', expected_state, timeout)


class IxnIsisFabricPathRouterEmulation(IxnEmulationHost):
    """Generated NGPF isisFabricPathRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisFabricPathRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisFabricPathRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                capabilityRouterId: href
                enableWideMetric: href
                dceTopologyCount: number
                dceMCastMacGroupCount: number
                dceMCastIpv4GroupCount: number
                dceMCastIpv6GroupCount: number
                enableHelloPadding: href
                maxAreaAddresses: href
                areaAddresses: href
                portData: href
                discardLSPs: href
                localSystemID: list
                enableHostName: href
                hostName: href
                attached: href
                partitionRepair: href
                overloaded: href
                lSPRefreshRate: href
                lSPLifetime: href
                pSNPInterval: href
                cSNPInterval: href
                maxLSPSize: href
                lSPorMGroupPDUMinTransmissionInterval: href
                ignoreReceiveMD5: href
                areaAuthenticationType: href
                areaTransmitPasswordOrMD5Key: href
                maxLSPsOrMGroupPDUsPerBurst: href
                interLSPsOrMGroupPDUBurstGap: href
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisFabricPathRouterEmulation, self).find(["topology","deviceGroup","isisFabricPathRouter"], vport_name, emulation_host, filters)

    def isisstartrouter(self, expected_state=None, timeout=None):
        """Start ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathRouterEmulation, self).call_operation('isisStartRouter', expected_state, timeout)

    def isisstoprouter(self, expected_state=None, timeout=None):
        """Stop ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathRouterEmulation, self).call_operation('isisStopRouter', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisFabricPathRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsisL3Emulation(IxnEmulationHost):
    """Generated NGPF isisL3 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisL3Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceMetric: href
                ipv6MTMetric: href
                networkType: href
                enable3WayHandshake: href
                extendedLocalCircuitId: href
                levelType: href
                level1Priority: href
                level2Priority: href
                level1HelloInterval: href
                level1DeadInterval: href
                level2HelloInterval: href
                level2DeadInterval: href
                enableBfdRegistration: href
                enableAdjSID: href
                adjSID: href
                ipv6SidValue: href
                overrideFFlag: href
                fFlag: href
                bFlag: href
                vFlag: href
                lFlag: href
                sFlag: href
                pFlag: href
                weight: href
                enableLinkProtection: href
                extraTraffic: href
                unprotected: href
                shared: href
                dedicatedOneToOne: href
                dedicatedOnePlusOne: href
                enhanced: href
                reserved0x40: href
                reserved0x80: href
                suppressHello: href
                enableSRLG: href
                srlgCount: number
                localSystemID: list
                enableConfiguredHoldTime: href
                configuredHoldTime: href
                authType: href
                circuitTranmitPasswordOrMD5Key: href
                autoAdjustMTU: href
                autoAdjustArea: href
                autoAdjustSupportedProtocols: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisL3Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisL3"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def isisstartinterface(self, expected_state=None, timeout=None):
        """Start ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('isisStartInterface', expected_state, timeout)

    def isisstopinterface(self, expected_state=None, timeout=None):
        """Stop ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('isisStopInterface', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('restartDown', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('resumeHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('stop', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisL3Emulation, self).call_operation('stopHello', expected_state, timeout)


class IxnIsisL3PseudoIfaceAttPoint1ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisL3PseudoIfaceAttPoint1Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3PseudoIfaceAttPoint1ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3PseudoIfaceAttPoint1Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3PseudoIfaceAttPoint1ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisL3PseudoIfaceAttPoint1Config"], vport_name, emulation_host, filters)


class IxnIsisL3PseudoIfaceAttPoint2ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisL3PseudoIfaceAttPoint2Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3PseudoIfaceAttPoint2ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3PseudoIfaceAttPoint2Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3PseudoIfaceAttPoint2ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisL3PseudoIfaceAttPoint2Config"], vport_name, emulation_host, filters)


class IxnIsisL3PseudoInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF isisL3PseudoInterface emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3PseudoInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3PseudoInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                administratorGroup: href
                metricLevel: href
                maxBandwidth_Bps: href
                maxReservableBandwidth_Bps: href
                bandwidthPriority0_Bps: href
                bandwidthPriority1_Bps: href
                bandwidthPriority2_Bps: href
                bandwidthPriority3_Bps: href
                bandwidthPriority4_Bps: href
                bandwidthPriority5_Bps: href
                bandwidthPriority6_Bps: href
                bandwidthPriority7_Bps: href
                enableAdjSID: href
                adjSID: href
                ipv6SidValue: href
                bFlag: href
                overrideFFlag: href
                fFlag: href
                vFlag: href
                lFlag: href
                sFlag: href
                pFlag: href
                weight: href
                enableLinkProtection: href
                extraTraffic: href
                unprotected: href
                shared: href
                dedicatedOneToOne: href
                dedicatedOnePlusOne: href
                enhanced: href
                reserved0x40: href
                reserved0x80: href
                enableSRLG: href
                srlgCount: number
                linkType: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3PseudoInterfaceEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface"], vport_name, emulation_host, filters)


class IxnIsisL3PseudoRouterEmulation(IxnEmulationHost):
    """Generated NGPF isisL3PseudoRouter emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3PseudoRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3PseudoRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableMTIPv6: href
                ipv6MTMetric: href
                enableWideMetric: href
                enable: href
                tERouterId: href
                enableWMforTEinNetworkGroup: href
                enableSR: bool
                nodePrefix: href
                mask: href
                rtrcapId: href
                dBit: href
                sBit: href
                redistribution: href
                rFlag: href
                nFlag: href
                pFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                ipv4Flag: href
                ipv6Flag: href
                ipv6Srh: href
                ipv6NodePrefix: href
                prefixLength: href
                configureSIDIndexLabel: href
                sIDIndexLabel: href
                sRAlgorithmCount: number
                sRGBRangeCount: number
                advertiseSRLB: href
                srlbFlags: href
                srlbDescriptorCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3PseudoRouterEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","isisL3PseudoRouter"], vport_name, emulation_host, filters)


class IxnIsisL3RoutePropertyEmulation(IxnEmulationHost):
    """Generated NGPF isisL3RouteProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3RoutePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3RouteProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                localSystemID: list
                routeOrigin: href
                redistribution: href
                rFlag: href
                nFlag: href
                pFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                algorithm: href
                configureSIDIndexLabel: href
                sIDIndexLabel: href
                ipv6Srh: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3RoutePropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","isisL3RouteProperty"], vport_name, emulation_host, filters)


class IxnIsisL3RouterEmulation(IxnEmulationHost):
    """Generated NGPF isisL3Router emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisL3RouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3Router emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableMTIPv6: href
                enableWideMetric: href
                enableTE: href
                enableWMforTE: href
                tERouterId: href
                enableSR: bool
                noOfSRTunnels: number
                nodePrefix: href
                mask: href
                rtrcapId: href
                dBit: href
                sBit: href
                redistribution: href
                rFlag: href
                nFlag: href
                pFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                ipv4Flag: href
                ipv6Flag: href
                ipv6Srh: href
                ipv6NodePrefix: href
                prefixLength: href
                configureSIDIndexLabel: href
                sIDIndexLabel: href
                sRGBRangeCount: number
                sRAlgorithmCount: number
                enableMappingServer: href
                numberOfMappingIPV4Ranges: number
                numberOfMappingIPV6Ranges: number
                advertiseSRMSPreference: href
                srmsPreference: href
                advertiseSRLB: href
                srlbFlags: href
                srlbDescriptorCount: number
                enableHelloPadding: href
                maxAreaAddresses: href
                areaAddresses: href
                enableHitlessRestart: href
                hitlessRestartMode: href
                hitlessRestartVersion: href
                hitlessRestartTime: href
                domainAuthenticationType: href
                domainTransmitPasswordOrMD5Key: href
                portData: href
                discardLSPs: href
                localSystemID: list
                enableHostName: href
                hostName: href
                attached: href
                partitionRepair: href
                overloaded: href
                lSPRefreshRate: href
                lSPLifetime: href
                pSNPInterval: href
                cSNPInterval: href
                maxLSPSize: href
                lSPorMGroupPDUMinTransmissionInterval: href
                ignoreReceiveMD5: href
                areaAuthenticationType: href
                areaTransmitPasswordOrMD5Key: href
                maxLSPsOrMGroupPDUsPerBurst: href
                interLSPsOrMGroupPDUBurstGap: href
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisL3RouterEmulation, self).find(["topology","deviceGroup","isisL3Router"], vport_name, emulation_host, filters)

    def isisstartrouter(self, expected_state=None, timeout=None):
        """Start ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisL3RouterEmulation, self).call_operation('isisStartRouter', expected_state, timeout)

    def isisstoprouter(self, expected_state=None, timeout=None):
        """Stop ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisL3RouterEmulation, self).call_operation('isisStopRouter', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisL3RouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisL3RouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisL3RouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsisL3SimulatedTopologyConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisL3SimulatedTopologyConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3SimulatedTopologyConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3SimulatedTopologyConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                isisL3Ipv4NodeRouteCount: number
                isisL3Ipv6NodeRouteCount: number
                enableHostName: href
                hostName: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3SimulatedTopologyConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisL3SimulatedTopologyConfig"], vport_name, emulation_host, filters)


class IxnIsisL3ipv4NodeRouteListEmulation(IxnEmulationHost):
    """Generated NGPF isisL3ipv4NodeRouteList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3ipv4NodeRouteListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3ipv4NodeRouteList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                firstIpv4Route: href
                maskWidth: href
                noOfRoutes: href
                routeStep: href
                metric: href
                routeOrigin: href
                redistribution: href
                nodeStep: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3ipv4NodeRouteListEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisL3SimulatedTopologyConfig","isisL3ipv4NodeRouteList"], vport_name, emulation_host, filters)


class IxnIsisL3ipv6NodeRouteListEmulation(IxnEmulationHost):
    """Generated NGPF isisL3ipv6NodeRouteList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisL3ipv6NodeRouteListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisL3ipv6NodeRouteList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                firstIpv6Route: href
                maskWidth: href
                noOfRoutes: href
                routeStep: href
                metric: href
                routeOrigin: href
                redistribution: href
                nodeStep: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisL3ipv6NodeRouteListEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisL3SimulatedTopologyConfig","isisL3ipv6NodeRouteList"], vport_name, emulation_host, filters)


class IxnIsisMappingServerIPV4ListEmulation(IxnEmulationHost):
    """Generated NGPF isisMappingServerIPV4List emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisMappingServerIPV4ListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisMappingServerIPV4List emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                fECPrefix: href
                prefixLength: href
                range: href
                lastFECAddress: list
                startSIDLabel: href
                mFlag: href
                sFlag: href
                dFlag: href
                aFlag: href
                algorithm: href
                weight: href
                rFlag: href
                nFlag: href
                pFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisMappingServerIPV4ListEmulation, self).find(["topology","deviceGroup","isisL3Router","isisMappingServerIPV4List"], vport_name, emulation_host, filters)


class IxnIsisMappingServerIPV6ListEmulation(IxnEmulationHost):
    """Generated NGPF isisMappingServerIPV6List emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisMappingServerIPV6ListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisMappingServerIPV6List emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                fECPrefix: href
                prefixLength: href
                range: href
                lastFECAddress: list
                startSIDLabel: href
                mFlag: href
                sFlag: href
                dFlag: href
                aFlag: href
                algorithm: href
                weight: href
                rFlag: href
                nFlag: href
                pFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisMappingServerIPV6ListEmulation, self).find(["topology","deviceGroup","isisL3Router","isisMappingServerIPV6List"], vport_name, emulation_host, filters)


class IxnIsisPseudoInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF isisPseudoInterface emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisPseudoInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisPseudoInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                linkType: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisPseudoInterfaceEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisPseudoInterface"], vport_name, emulation_host, filters)


class IxnIsisSRAlgorithmListEmulation(IxnEmulationHost):
    """Generated NGPF isisSRAlgorithmList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSRAlgorithmListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSRAlgorithmList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                isisSrAlgorithm: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSRAlgorithmListEmulation, self).find(["topology","deviceGroup","isisL3Router","isisSRAlgorithmList"], vport_name, emulation_host, filters)


class IxnIsisSRGBRangeSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF isisSRGBRangeSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSRGBRangeSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSRGBRangeSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startSIDLabel: href
                sIDCount: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSRGBRangeSubObjectsListEmulation, self).find(["topology","deviceGroup","isisL3Router","isisSRGBRangeSubObjectsList"], vport_name, emulation_host, filters)


class IxnIsisSRLBDescriptorListEmulation(IxnEmulationHost):
    """Generated NGPF isisSRLBDescriptorList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSRLBDescriptorListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSRLBDescriptorList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startSIDLabel: href
                sIDCount: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSRLBDescriptorListEmulation, self).find(["topology","deviceGroup","isisL3Router","isisSRLBDescriptorList"], vport_name, emulation_host, filters)


class IxnIsisSRTunnelListEmulation(IxnEmulationHost):
    """Generated NGPF isisSRTunnelList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSRTunnelListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSRTunnelList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                tunnelDescription: href
                usingHeadEndNodePrefix: href
                sourceIpv4: href
                sourceIpv6: href
                numberOfSegments: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSRTunnelListEmulation, self).find(["topology","deviceGroup","isisL3Router","isisSRTunnelList"], vport_name, emulation_host, filters)


class IxnIsisSegmentListEmulation(IxnEmulationHost):
    """Generated NGPF isisSegmentList emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSegmentListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSegmentList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enable: href
                segmentType: href
                nodeSystemID: href
                neighbournodeSystemID: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSegmentListEmulation, self).find(["topology","deviceGroup","isisL3Router","isisSRTunnelList","isisSegmentList"], vport_name, emulation_host, filters)


class IxnIsisSpbBcbEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbBcb emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisSpbBcbEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbBcb emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceMetric: href
                levelType: href
                networkType: href
                enable3WayHandshake: href
                extendedLocalCircuitId: href
                helloInterval: href
                deadInterval: href
                localSystemID: list
                enableConfiguredHoldTime: href
                configuredHoldTime: href
                authType: href
                circuitTranmitPasswordOrMD5Key: href
                autoAdjustMTU: href
                autoAdjustArea: href
                autoAdjustSupportedProtocols: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisSpbBcbEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisSpbBcb"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def isisstartinterface(self, expected_state=None, timeout=None):
        """Start ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('isisStartInterface', expected_state, timeout)

    def isisstopinterface(self, expected_state=None, timeout=None):
        """Stop ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('isisStopInterface', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('resumeHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('stop', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBcbEmulation, self).call_operation('stopHello', expected_state, timeout)


class IxnIsisSpbBebEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbBeb emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisSpbBebEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbBeb emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceMetric: href
                levelType: href
                networkType: href
                enable3WayHandshake: href
                extendedLocalCircuitId: href
                helloInterval: href
                deadInterval: href
                localSystemID: list
                enableConfiguredHoldTime: href
                configuredHoldTime: href
                authType: href
                circuitTranmitPasswordOrMD5Key: href
                autoAdjustMTU: href
                autoAdjustArea: href
                autoAdjustSupportedProtocols: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisSpbBebEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisSpbBeb"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def isisstartinterface(self, expected_state=None, timeout=None):
        """Start ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('isisStartInterface', expected_state, timeout)

    def isisstopinterface(self, expected_state=None, timeout=None):
        """Stop ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('isisStopInterface', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('resumeHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('stop', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbBebEmulation, self).call_operation('stopHello', expected_state, timeout)


class IxnIsisSpbMacCloudConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbMacCloudConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSpbMacCloudConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbMacCloudConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                isid: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSpbMacCloudConfigEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","isisSpbMacCloudConfig"], vport_name, emulation_host, filters)


class IxnIsisSpbPseudoIfaceAttPoint1ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbPseudoIfaceAttPoint1Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSpbPseudoIfaceAttPoint1ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbPseudoIfaceAttPoint1Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSpbPseudoIfaceAttPoint1ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisSpbPseudoIfaceAttPoint1Config"], vport_name, emulation_host, filters)


class IxnIsisSpbPseudoIfaceAttPoint2ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbPseudoIfaceAttPoint2Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSpbPseudoIfaceAttPoint2ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbPseudoIfaceAttPoint2Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSpbPseudoIfaceAttPoint2ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisSpbPseudoIfaceAttPoint2Config"], vport_name, emulation_host, filters)


class IxnIsisSpbPseudoNodeEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbPseudoNode emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSpbPseudoNodeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbPseudoNode emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                bridgePriority: href
                spSourceId: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSpbPseudoNodeEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouterBridge","isisSpbPseudoNode"], vport_name, emulation_host, filters)


class IxnIsisSpbRouterEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisSpbRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableWideMetric: href
                spbTopologyCount: number
                ignoreMTPortCapability: href
                enableHelloPadding: href
                maxAreaAddresses: href
                areaAddresses: href
                enableHitlessRestart: href
                hitlessRestartMode: href
                hitlessRestartVersion: href
                hitlessRestartTime: href
                portData: href
                discardLSPs: href
                localSystemID: list
                enableHostName: href
                hostName: href
                attached: href
                partitionRepair: href
                overloaded: href
                lSPRefreshRate: href
                lSPLifetime: href
                pSNPInterval: href
                cSNPInterval: href
                maxLSPSize: href
                lSPorMGroupPDUMinTransmissionInterval: href
                ignoreReceiveMD5: href
                areaAuthenticationType: href
                areaTransmitPasswordOrMD5Key: href
                maxLSPsOrMGroupPDUsPerBurst: href
                interLSPsOrMGroupPDUBurstGap: href
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisSpbRouterEmulation, self).find(["topology","deviceGroup","isisSpbRouter"], vport_name, emulation_host, filters)

    def isisstartrouter(self, expected_state=None, timeout=None):
        """Start ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbRouterEmulation, self).call_operation('isisStartRouter', expected_state, timeout)

    def isisstoprouter(self, expected_state=None, timeout=None):
        """Stop ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbRouterEmulation, self).call_operation('isisStopRouter', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsisSpbSimRouterEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbSimRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisSpbSimRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbSimRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                systemId: href
                bridgePriority: href
                spSourceId: href
                spbTopologyCount: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisSpbSimRouterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisSpbSimRouter"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbSimRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbSimRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisSpbSimRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsisSpbSimulatedTopologyConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisSpbSimulatedTopologyConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisSpbSimulatedTopologyConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisSpbSimulatedTopologyConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceMetric: href
                spbNodeTopologyCount: number
                enableHostName: href
                hostName: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisSpbSimulatedTopologyConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisSpbSimulatedTopologyConfig"], vport_name, emulation_host, filters)


class IxnIsisTrafficEngineeringEmulation(IxnEmulationHost):
    """Generated NGPF isisTrafficEngineering emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisTrafficEngineeringEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrafficEngineering emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                administratorGroup: href
                metricLevel: href
                maxBandwidth: href
                maxReservableBandwidth: href
                bandwidthPriority0: href
                bandwidthPriority1: href
                bandwidthPriority2: href
                bandwidthPriority3: href
                bandwidthPriority4: href
                bandwidthPriority5: href
                bandwidthPriority6: href
                bandwidthPriority7: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisTrafficEngineeringEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisL3","isisTrafficEngineering"], vport_name, emulation_host, filters)


class IxnIsisTrillEmulation(IxnEmulationHost):
    """Generated NGPF isisTrill emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisTrillEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrill emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceMetric: href
                networkType: href
                levelType: href
                level1Priority: href
                enable3WayHandshake: href
                extendedLocalCircuitId: href
                level1HelloInterval: href
                level1DeadInterval: href
                localSystemID: list
                enableConfiguredHoldTime: href
                configuredHoldTime: href
                authType: href
                circuitTranmitPasswordOrMD5Key: href
                autoAdjustMTU: href
                autoAdjustArea: href
                autoAdjustSupportedProtocols: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisTrillEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisTrill"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def isisstartinterface(self, expected_state=None, timeout=None):
        """Start ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('isisStartInterface', expected_state, timeout)

    def isisstopinterface(self, expected_state=None, timeout=None):
        """Stop ISIS Interface
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('isisStopInterface', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('resumeHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('stop', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop sending ISIS Hellos
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillEmulation, self).call_operation('stopHello', expected_state, timeout)


class IxnIsisTrillPseudoIfaceAttPoint1ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisTrillPseudoIfaceAttPoint1Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisTrillPseudoIfaceAttPoint1ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrillPseudoIfaceAttPoint1Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisTrillPseudoIfaceAttPoint1ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisTrillPseudoIfaceAttPoint1Config"], vport_name, emulation_host, filters)


class IxnIsisTrillPseudoIfaceAttPoint2ConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisTrillPseudoIfaceAttPoint2Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisTrillPseudoIfaceAttPoint2ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrillPseudoIfaceAttPoint2Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                linkMetric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisTrillPseudoIfaceAttPoint2ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","isisL3PseudoInterface","isisTrillPseudoIfaceAttPoint2Config"], vport_name, emulation_host, filters)


class IxnIsisTrillPseudoNodeEmulation(IxnEmulationHost):
    """Generated NGPF isisTrillPseudoNode emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisTrillPseudoNodeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrillPseudoNode emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nickname: href
                broadcastRootPriority: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisTrillPseudoNodeEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouterBridge","isisTrillPseudoNode"], vport_name, emulation_host, filters)


class IxnIsisTrillRouterEmulation(IxnEmulationHost):
    """Generated NGPF isisTrillRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisTrillRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrillRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                capabilityRouterId: href
                enableWideMetric: href
                trillMCastMacGroupCount: number
                trillMCastIpv4GroupCount: number
                trillMCastIpv6GroupCount: number
                enableHelloPadding: href
                maxAreaAddresses: href
                areaAddresses: href
                enableMtuProbe: href
                noOfMtuProbes: href
                origLspBufSize: href
                portData: href
                discardLSPs: href
                localSystemID: list
                enableHostName: href
                hostName: href
                attached: href
                partitionRepair: href
                overloaded: href
                lSPRefreshRate: href
                lSPLifetime: href
                pSNPInterval: href
                cSNPInterval: href
                maxLSPSize: href
                lSPorMGroupPDUMinTransmissionInterval: href
                ignoreReceiveMD5: href
                areaAuthenticationType: href
                areaTransmitPasswordOrMD5Key: href
                maxLSPsOrMGroupPDUsPerBurst: href
                interLSPsOrMGroupPDUBurstGap: href
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisTrillRouterEmulation, self).find(["topology","deviceGroup","isisTrillRouter"], vport_name, emulation_host, filters)

    def isisstartrouter(self, expected_state=None, timeout=None):
        """Start ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillRouterEmulation, self).call_operation('isisStartRouter', expected_state, timeout)

    def isisstoprouter(self, expected_state=None, timeout=None):
        """Stop ISIS Router
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillRouterEmulation, self).call_operation('isisStopRouter', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsisTrillSimRouterEmulation(IxnEmulationHost):
    """Generated NGPF isisTrillSimRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnIsisTrillSimRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrillSimRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                systemId: href
                nickname: href
                broadcastRootPriority: href
                trillMCastMacGroupCount: number
                trillMCastIpv4GroupCount: number
                trillMCastIpv6GroupCount: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnIsisTrillSimRouterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisTrillSimRouter"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillSimRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillSimRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnIsisTrillSimRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnIsisTrillSimulatedTopologyConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisTrillSimulatedTopologyConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisTrillSimulatedTopologyConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrillSimulatedTopologyConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                trillNodeTopologyCount: number
                enableHostName: href
                hostName: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisTrillSimulatedTopologyConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisTrillSimulatedTopologyConfig"], vport_name, emulation_host, filters)


class IxnIsisTrillUCastMacConfigEmulation(IxnEmulationHost):
    """Generated NGPF isisTrillUCastMacConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnIsisTrillUCastMacConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific isisTrillUCastMacConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localSystemID: list
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIsisTrillUCastMacConfigEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","isisTrillUCastMacConfig"], vport_name, emulation_host, filters)


class IxnLabelBlockListEmulation(IxnEmulationHost):
    """Generated NGPF labelBlockList emulation host """


    def __init__(self, ixnhttp):
        super(IxnLabelBlockListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific labelBlockList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                advLblBlock: href
                offsetLabelBlock: href
                startLabel: href
                numLabels: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLabelBlockListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIpv6L2Site","labelBlockList"], vport_name, emulation_host, filters)


class IxnLacEmulation(IxnEmulationHost):
    """Generated NGPF lac emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLacEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific lac emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                lacGlobalAndPortData: href
                baseLnsIp: href
                enableRedial: href
                redialInterval: href
                maxRedialAttempts: href
                lacHostName: href
                lacSecret: href
                enableHelloRequest: href
                helloRequestInterval: href
                bearerCapability: href
                bearerType: href
                controlMsgsRetryCounter: href
                initRetransmitInterval: href
                maxRetransmitInterval: href
                receiveWindowSize: href
                framingCapability: href
                enableExcludeHdlc: bool
                enableControlChecksum: href
                enableDataChecksum: href
                udpSourcePort: href
                udpDestinationPort: href
                useLengthBitInPayload: href
                useOffsetBitInPayload: href
                offsetByte: href
                offsetLength: href
                useSequenceNoInPayload: href
                tunnelAuthentication: href
                useHiddenAVPs: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLacEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lac"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLacEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLacEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLacEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLacpEmulation(IxnEmulationHost):
    """Generated NGPF lacp emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLacpEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific lacp emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                administrativeKey: href
                actorSystemId: href
                actorSystemPriority: href
                actorKey: href
                actorPortNumber: href
                actorPortPriority: href
                sourceMac: list
                collectorsMaxdelay: href
                lacpduPeriodicTimeInterval: href
                lacpduTimeout: href
                lacpActivity: href
                supportRespondingToMarker: href
                markerResponseWaitTime: href
                periodicSendingOfMarkerRequest: href
                markerRequestMode: href
                interMarkerPDUDelay: href
                interMarkerPDUDelayRandomMin: href
                interMarkerPDUDelayRandomMax: href
                sendMarkerRequestOnLagChange: href
                aggregationFlagState: href
                synchronizationFlag: href
                distributingFlag: href
                collectingFlag: href
                portData: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLacpEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","lacp"], vport_name, emulation_host, filters)

    def lacpstartpdu(self, expected_state=None, timeout=None):
        """LACP Start PDU
            For expected_state options see the class state variables
        """
        super(IxnLacpEmulation, self).call_operation('lacpStartPDU', expected_state, timeout)

    def lacpstoppdu(self, expected_state=None, timeout=None):
        """LACP Stop PDU
            For expected_state options see the class state variables
        """
        super(IxnLacpEmulation, self).call_operation('lacpStopPDU', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLacpEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendmarker(self, expected_state=None, timeout=None):
        """Send Marker
            For expected_state options see the class state variables
        """
        super(IxnLacpEmulation, self).call_operation('sendMarker', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start LACP
            For expected_state options see the class state variables
        """
        super(IxnLacpEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LACP
            For expected_state options see the class state variables
        """
        super(IxnLacpEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLatencyBaseEmulation(IxnEmulationHost):
    """Generated NGPF latencyBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnLatencyBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific latencyBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnLatencyBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","latencyBase"], vport_name, emulation_host, filters)


class IxnLdpBasicRouterEmulation(IxnEmulationHost):
    """Generated NGPF ldpBasicRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpBasicRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpBasicRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rootRangesCountV4: number
                leafRangesCountV4: number
                portData: href
                localRouterID: list
                ldpVersion: enum
                enableGracefulRestart: href
                recoveryTime: href
                reconnectTime: href
                keepAliveInterval: href
                keepAliveHoldTime: href
                sessionPreference: href
                includeSac: href
                enableIpv4Advertisement: href
                enableIpv6Advertisement: href
                enableFec128Advertisement: href
                enableFec129Advertisement: href
                ignoreStateAdvertisementControlCapability: href
                enableP2MPCapability: href
                enableBfdMplsLearnedLsp: href
                enableLspPingLearnedLsp: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpBasicRouterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","ldpBasicRouterV6","ldpvplsbgpad","ldpBasicRouter"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getalllearnedinfo(self, expected_state=None, timeout=None):
        """Get All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('getAllLearnedInfo', expected_state, timeout)

    def getfec128learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 128 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('getFEC128LearnedInfo', expected_state, timeout)

    def getfec129learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 129 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('getFEC129LearnedInfo', expected_state, timeout)

    def getipv4feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('getIPv4FECLearnedInfo', expected_state, timeout)

    def getipv6feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('getIPv6FECLearnedInfo', expected_state, timeout)

    def getp2mpfeclearnedinfo(self, expected_state=None, timeout=None):
        """Get P2MP FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('getP2MPFECLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumekeepalive(self, expected_state=None, timeout=None):
        """Resume sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('resumeKeepAlive', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('stop', expected_state, timeout)

    def stopkeepalive(self, expected_state=None, timeout=None):
        """Stop sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterEmulation, self).call_operation('stopKeepAlive', expected_state, timeout)


class IxnLdpBasicRouterV6Emulation(IxnEmulationHost):
    """Generated NGPF ldpBasicRouterV6 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpBasicRouterV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpBasicRouterV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rootRangesCountV6: number
                leafRangesCountV6: number
                portData: href
                localRouterID: list
                ldpVersion: enum
                enableGracefulRestart: href
                recoveryTime: href
                reconnectTime: href
                keepAliveInterval: href
                keepAliveHoldTime: href
                sessionPreference: href
                includeSac: href
                enableIpv4Advertisement: href
                enableIpv6Advertisement: href
                enableFec128Advertisement: href
                enableFec129Advertisement: href
                ignoreStateAdvertisementControlCapability: href
                enableP2MPCapability: href
                enableBfdMplsLearnedLsp: href
                enableLspPingLearnedLsp: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpBasicRouterV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","ldpBasicRouterV6"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getalllearnedinfo(self, expected_state=None, timeout=None):
        """Get All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('getAllLearnedInfo', expected_state, timeout)

    def getfec128learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 128 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('getFEC128LearnedInfo', expected_state, timeout)

    def getfec129learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 129 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('getFEC129LearnedInfo', expected_state, timeout)

    def getipv4feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('getIPv4FECLearnedInfo', expected_state, timeout)

    def getipv6feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('getIPv6FECLearnedInfo', expected_state, timeout)

    def getp2mpfeclearnedinfo(self, expected_state=None, timeout=None):
        """Get P2MP FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('getP2MPFECLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('restartDown', expected_state, timeout)

    def resumekeepalive(self, expected_state=None, timeout=None):
        """Resume sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('resumeKeepAlive', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('stop', expected_state, timeout)

    def stopkeepalive(self, expected_state=None, timeout=None):
        """Stop sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpBasicRouterV6Emulation, self).call_operation('stopKeepAlive', expected_state, timeout)


class IxnLdpConnectedInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF ldpConnectedInterface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpConnectedInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpConnectedInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                basicHelloInterval: href
                basicHoldTime: href
                localRouterID: list
                labelSpaceID: href
                operationMode: href
                authentication: href
                mD5Key: href
                enableBfdRegistration: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpConnectedInterfaceEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ldpConnectedInterface"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpConnectedInterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumebasichello(self, expected_state=None, timeout=None):
        """Resume sending LDP Basic Hellos
            For expected_state options see the class state variables
        """
        super(IxnLdpConnectedInterfaceEmulation, self).call_operation('resumeBasicHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate LDP Interface
            For expected_state options see the class state variables
        """
        super(IxnLdpConnectedInterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LDP Interface
            For expected_state options see the class state variables
        """
        super(IxnLdpConnectedInterfaceEmulation, self).call_operation('stop', expected_state, timeout)

    def stopbasichello(self, expected_state=None, timeout=None):
        """Stop sending LDP Basic Hellos
            For expected_state options see the class state variables
        """
        super(IxnLdpConnectedInterfaceEmulation, self).call_operation('stopBasicHello', expected_state, timeout)


class IxnLdpFECPropertyEmulation(IxnEmulationHost):
    """Generated NGPF ldpFECProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnLdpFECPropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpFECProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localRouterID: list
                labelValue: href
                labelIncrementMode: href
                enablePacking: href
                enableReplyingLspPing: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLdpFECPropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv4PrefixPools","ldpFECProperty"], vport_name, emulation_host, filters)


class IxnLdpIpv6FECPropertyEmulation(IxnEmulationHost):
    """Generated NGPF ldpIpv6FECProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnLdpIpv6FECPropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpIpv6FECProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localRouterID: list
                labelValue: href
                labelIncrementMode: href
                enablePacking: href
                enableReplyingLspPing: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLdpIpv6FECPropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","ldpIpv6FECProperty"], vport_name, emulation_host, filters)


class IxnLdpLpbInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF ldpLpbInterface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpLpbInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpLpbInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpLpbInterfaceEmulation, self).find(["topology","deviceGroup","ldpLpbInterface"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpLpbInterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLdpLpbInterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLdpLpbInterfaceEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLdpPseudoRouterEmulation(IxnEmulationHost):
    """Generated NGPF ldpPseudoRouter emulation host """


    def __init__(self, ixnhttp):
        super(IxnLdpPseudoRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpPseudoRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                labelValue: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLdpPseudoRouterEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ldpPseudoRouter"], vport_name, emulation_host, filters)


class IxnLdpSimulatedTopologyConfigEmulation(IxnEmulationHost):
    """Generated NGPF ldpSimulatedTopologyConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnLdpSimulatedTopologyConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpSimulatedTopologyConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLdpSimulatedTopologyConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","ldpSimulatedTopologyConfig"], vport_name, emulation_host, filters)


class IxnLdpTLVListEmulation(IxnEmulationHost):
    """Generated NGPF ldpTLVList emulation host """


    def __init__(self, ixnhttp):
        super(IxnLdpTLVListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpTLVList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                type: href
                tlvLength: href
                value: href
                increment: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLdpTLVListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","rootRanges","ldpTLVList"], vport_name, emulation_host, filters)


class IxnLdpTargetedIpv6PeerEmulation(IxnEmulationHost):
    """Generated NGPF ldpTargetedIpv6Peer emulation host """


    def __init__(self, ixnhttp):
        super(IxnLdpTargetedIpv6PeerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpTargetedIpv6Peer emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                iPAddress: href
                localRouterID: list
                initiateTargetedHello: href
                authentication: href
                mD5Key: href
                targetedHelloInterval: href
                targetedHoldTime: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLdpTargetedIpv6PeerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldpTargetedIpv6Peer"], vport_name, emulation_host, filters)


class IxnLdpTargetedPeerEmulation(IxnEmulationHost):
    """Generated NGPF ldpTargetedPeer emulation host """


    def __init__(self, ixnhttp):
        super(IxnLdpTargetedPeerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpTargetedPeer emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                iPAddress: href
                localRouterID: list
                initiateTargetedHello: href
                authentication: href
                mD5Key: href
                targetedHelloInterval: href
                targetedHoldTime: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLdpTargetedPeerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldpTargetedPeer"], vport_name, emulation_host, filters)


class IxnLdpTargetedRouterEmulation(IxnEmulationHost):
    """Generated NGPF ldpTargetedRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpTargetedRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpTargetedRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rootRangesCountV4: number
                leafRangesCountV4: number
                labelSpaceID: href
                operationMode: href
                peerCount: number
                ipv6peerCount: number
                enableBfdRegistration: href
                bfdOpeMode: href
                portData: href
                localRouterID: list
                ldpVersion: enum
                enableGracefulRestart: href
                recoveryTime: href
                reconnectTime: href
                keepAliveInterval: href
                keepAliveHoldTime: href
                sessionPreference: href
                includeSac: href
                enableIpv4Advertisement: href
                enableIpv6Advertisement: href
                enableFec128Advertisement: href
                enableFec129Advertisement: href
                ignoreStateAdvertisementControlCapability: href
                enableP2MPCapability: href
                enableBfdMplsLearnedLsp: href
                enableLspPingLearnedLsp: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpTargetedRouterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getalllearnedinfo(self, expected_state=None, timeout=None):
        """Get All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('getAllLearnedInfo', expected_state, timeout)

    def getfec128learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 128 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('getFEC128LearnedInfo', expected_state, timeout)

    def getfec129learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 129 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('getFEC129LearnedInfo', expected_state, timeout)

    def getipv4feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('getIPv4FECLearnedInfo', expected_state, timeout)

    def getipv6feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('getIPv6FECLearnedInfo', expected_state, timeout)

    def getp2mpfeclearnedinfo(self, expected_state=None, timeout=None):
        """Get P2MP FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('getP2MPFECLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumekeepalive(self, expected_state=None, timeout=None):
        """Resume sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('resumeKeepAlive', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('stop', expected_state, timeout)

    def stopkeepalive(self, expected_state=None, timeout=None):
        """Stop sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterEmulation, self).call_operation('stopKeepAlive', expected_state, timeout)


class IxnLdpTargetedRouterV6Emulation(IxnEmulationHost):
    """Generated NGPF ldpTargetedRouterV6 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpTargetedRouterV6Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpTargetedRouterV6 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rootRangesCountV6: number
                leafRangesCountV6: number
                labelSpaceID: href
                operationMode: href
                peerCount: number
                ipv6peerCount: number
                enableBfdRegistration: href
                bfdOpeMode: href
                portData: href
                localRouterID: list
                ldpVersion: enum
                enableGracefulRestart: href
                recoveryTime: href
                reconnectTime: href
                keepAliveInterval: href
                keepAliveHoldTime: href
                sessionPreference: href
                includeSac: href
                enableIpv4Advertisement: href
                enableIpv6Advertisement: href
                enableFec128Advertisement: href
                enableFec129Advertisement: href
                ignoreStateAdvertisementControlCapability: href
                enableP2MPCapability: href
                enableBfdMplsLearnedLsp: href
                enableLspPingLearnedLsp: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpTargetedRouterV6Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getalllearnedinfo(self, expected_state=None, timeout=None):
        """Get All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('getAllLearnedInfo', expected_state, timeout)

    def getfec128learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 128 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('getFEC128LearnedInfo', expected_state, timeout)

    def getfec129learnedinfo(self, expected_state=None, timeout=None):
        """Get FEC 129 Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('getFEC129LearnedInfo', expected_state, timeout)

    def getipv4feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv4 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('getIPv4FECLearnedInfo', expected_state, timeout)

    def getipv6feclearnedinfo(self, expected_state=None, timeout=None):
        """Get IPv6 FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('getIPv6FECLearnedInfo', expected_state, timeout)

    def getp2mpfeclearnedinfo(self, expected_state=None, timeout=None):
        """Get P2MP FEC Learned Info
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('getP2MPFECLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('restartDown', expected_state, timeout)

    def resumekeepalive(self, expected_state=None, timeout=None):
        """Resume sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('resumeKeepAlive', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LDP Router
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('stop', expected_state, timeout)

    def stopkeepalive(self, expected_state=None, timeout=None):
        """Stop sending KeepAlive
            For expected_state options see the class state variables
        """
        super(IxnLdpTargetedRouterV6Emulation, self).call_operation('stopKeepAlive', expected_state, timeout)


class IxnLdpotherpwsEmulation(IxnEmulationHost):
    """Generated NGPF ldpotherpws emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpotherpwsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpotherpws emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ifaceType: href
                vCIDStart: href
                aTMPresent: href
                maxATMCells: href
                cEMPayLoadEnable: href
                cEMPayload: href
                cEMOptionPresent: href
                cEMOption: href
                includeTDMPayload: href
                tDMDataSize: href
                includeTDMBitrate: href
                tDMBitrate: href
                includeRTPHeader: href
                includeTDMOption: href
                timestampMode: href
                payloadType: href
                frequency: href
                includeSSRC: href
                sSRC: href
                cAS: href
                sP: href
                enableCCCVNegotiation: href
                pWACHCC: href
                routerAlertCC: href
                lSPPingCV: href
                bfdUdpCV: href
                bfdPwCV: href
                localRouterID: list
                autoPeerId: bool
                peerId: href
                ipv6PeerId: href
                descEnabled: href
                description: href
                cBitEnabled: href
                mtu: href
                label: href
                groupId: href
                enablePWStatus: href
                pwStatusSendNotification: href
                pWStatusCode: href
                downStart: href
                downInterval: href
                upInterval: href
                repeatCount: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpotherpwsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws"], vport_name, emulation_host, filters)

    def purgevcranges(self, expected_state=None, timeout=None):
        """Purge VC Ranges
            For expected_state options see the class state variables
        """
        super(IxnLdpotherpwsEmulation, self).call_operation('purgeVCRanges', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpotherpwsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate VC
            For expected_state options see the class state variables
        """
        super(IxnLdpotherpwsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate VC
            For expected_state options see the class state variables
        """
        super(IxnLdpotherpwsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLdppwvplsEmulation(IxnEmulationHost):
    """Generated NGPF ldppwvpls emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdppwvplsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldppwvpls emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceType: href
                vCIDStart: href
                enableCCCVNegotiation: href
                pWACHCC: href
                routerAlertCC: href
                lSPPingCV: href
                bfdUdpCV: href
                bfdPwCV: href
                localRouterID: list
                autoPeerId: bool
                peerId: href
                ipv6PeerId: href
                descEnabled: href
                description: href
                cBitEnabled: href
                mtu: href
                label: href
                groupId: href
                enablePWStatus: href
                pwStatusSendNotification: href
                pWStatusCode: href
                downStart: href
                downInterval: href
                upInterval: href
                repeatCount: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdppwvplsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls"], vport_name, emulation_host, filters)

    def purgevcranges(self, expected_state=None, timeout=None):
        """Purge VC Ranges
            For expected_state options see the class state variables
        """
        super(IxnLdppwvplsEmulation, self).call_operation('purgeVCRanges', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdppwvplsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate VC
            For expected_state options see the class state variables
        """
        super(IxnLdppwvplsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate VC
            For expected_state options see the class state variables
        """
        super(IxnLdppwvplsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLdpv6ConnectedInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF ldpv6ConnectedInterface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpv6ConnectedInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpv6ConnectedInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                basicHelloInterval: href
                basicHoldTime: href
                localRouterID: list
                labelSpaceID: href
                operationMode: href
                authentication: href
                mD5Key: href
                enableBfdRegistration: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpv6ConnectedInterfaceEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","ldpv6ConnectedInterface"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpv6ConnectedInterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumebasichello(self, expected_state=None, timeout=None):
        """Resume sending LDP Basic Hellos
            For expected_state options see the class state variables
        """
        super(IxnLdpv6ConnectedInterfaceEmulation, self).call_operation('resumeBasicHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate LDP Interface
            For expected_state options see the class state variables
        """
        super(IxnLdpv6ConnectedInterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LDP Interface
            For expected_state options see the class state variables
        """
        super(IxnLdpv6ConnectedInterfaceEmulation, self).call_operation('stop', expected_state, timeout)

    def stopbasichello(self, expected_state=None, timeout=None):
        """Stop sending LDP Basic Hellos
            For expected_state options see the class state variables
        """
        super(IxnLdpv6ConnectedInterfaceEmulation, self).call_operation('stopBasicHello', expected_state, timeout)


class IxnLdpv6LoopbackInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF ldpv6LoopbackInterface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpv6LoopbackInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpv6LoopbackInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpv6LoopbackInterfaceEmulation, self).find(["topology","deviceGroup","ldpv6LoopbackInterface"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpv6LoopbackInterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLdpv6LoopbackInterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLdpv6LoopbackInterfaceEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLdpvplsbgpadEmulation(IxnEmulationHost):
    """Generated NGPF ldpvplsbgpad emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLdpvplsbgpadEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ldpvplsbgpad emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                interfaceType: href
                provisioningModelType: href
                typeVplsId: href
                ipAddressVplsId: href
                asNumberVplsId: href
                assignedNumberVplsId: href
                sourceAIIType: href
                sourceAIIasIP: href
                sourceAIIasNumber: href
                targetAIIType: href
                targetAIIasIP: href
                targetAIIasNumber: href
                enableCCCVNegotiation: href
                pWACHCC: href
                routerAlertCC: href
                lSPPingCV: href
                bfdUdpCV: href
                bfdPwCV: href
                localRouterID: list
                autoPeerId: bool
                peerId: href
                ipv6PeerId: href
                descEnabled: href
                description: href
                cBitEnabled: href
                mtu: href
                label: href
                groupId: href
                enablePWStatus: href
                pwStatusSendNotification: href
                pWStatusCode: href
                downStart: href
                downInterval: href
                upInterval: href
                repeatCount: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLdpvplsbgpadEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","ldpBasicRouterV6","ldpvplsbgpad"], vport_name, emulation_host, filters)

    def purgevcranges(self, expected_state=None, timeout=None):
        """Purge VC Ranges
            For expected_state options see the class state variables
        """
        super(IxnLdpvplsbgpadEmulation, self).call_operation('purgeVCRanges', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLdpvplsbgpadEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate VC
            For expected_state options see the class state variables
        """
        super(IxnLdpvplsbgpadEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate VC
            For expected_state options see the class state variables
        """
        super(IxnLdpvplsbgpadEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLeafRangesEmulation(IxnEmulationHost):
    """Generated NGPF leafRanges emulation host """


    def __init__(self, ixnhttp):
        super(IxnLeafRangesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific leafRanges emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                lSPType: enum
                rootAddress: href
                rootAddressCount: href
                rootAddressStep: href
                lspCountPerRoot: href
                labelValueStart: href
                labelValueStep: href
                continuousIncrementOVAcrossRoot: href
                numberOfTLVs: number
                groupAddressV4: href
                groupAddressV6: href
                groupCountPerLsp: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLeafRangesEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","leafRanges"], vport_name, emulation_host, filters)


class IxnLevelEmulation(IxnEmulationHost):
    """Generated NGPF level emulation host """


    def __init__(self, ixnhttp):
        super(IxnLevelEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific level emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nodeCount: number
        """
        return super(IxnLevelEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyFatTree","level"], vport_name, emulation_host, filters)


class IxnLightweightDhcp6RelayTlvProfileEmulation(IxnEmulationHost):
    """Generated NGPF lightweightDhcp6RelayTlvProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnLightweightDhcp6RelayTlvProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific lightweightDhcp6RelayTlvProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLightweightDhcp6RelayTlvProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","dhcpv6relayAgent","lightweightDhcp6RelayTlvProfile"], vport_name, emulation_host, filters)


class IxnLightweightDhcpv6relayAgentEmulation(IxnEmulationHost):
    """Generated NGPF lightweightDhcpv6relayAgent emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLightweightDhcpv6relayAgentEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific lightweightDhcpv6relayAgent emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                lightweightDhcp6RelayAgentGlobalAndPortData: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLightweightDhcpv6relayAgentEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","lightweightDhcpv6relayAgent"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLightweightDhcpv6relayAgentEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLightweightDhcpv6relayAgentEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLightweightDhcpv6relayAgentEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLinkLsaRoutesEmulation(IxnEmulationHost):
    """Generated NGPF linkLsaRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnLinkLsaRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific linkLsaRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                routerPriority: href
                reservedBit7: href
                reservedBit6: href
                dCBit: href
                rBit: href
                nBit: href
                xBit: href
                eBit: href
                v6Bit: href
                linkLocalAddress: href
                metric: href
                unusedBit7: href
                unusedBit6: href
                unusedBit5: href
                unusedBit4: href
                pBit: href
                mCBit: href
                lABit: href
                nUBit: href
                linkStateId: href
                linkStateIdStep: href
                active: href
                networkAddress: href
                rangeSize: href
                prefix: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLinkLsaRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfv3PseudoRouter","linkLsaRoutes"], vport_name, emulation_host, filters)


class IxnLinkTableEmulation(IxnEmulationHost):
    """Generated NGPF linkTable emulation host """


    def __init__(self, ixnhttp):
        super(IxnLinkTableEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific linkTable emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                fromNodeIndex: list
                toNodeIndex: list
        """
        return super(IxnLinkTableEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyCustom","linkTable"], vport_name, emulation_host, filters)


class IxnLnsEmulation(IxnEmulationHost):
    """Generated NGPF lns emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnLnsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific lns emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                lnsGlobalAndPortData: href
                noCallTimeout: href
                credentialsCount: number
                lnsHostName: href
                enableHelloRequest: href
                helloRequestInterval: href
                bearerCapability: href
                bearerType: href
                controlMsgsRetryCounter: href
                initRetransmitInterval: href
                maxRetransmitInterval: href
                receiveWindowSize: href
                framingCapability: href
                enableExcludeHdlc: bool
                enableControlChecksum: href
                enableDataChecksum: href
                udpSourcePort: href
                udpDestinationPort: href
                useLengthBitInPayload: href
                useOffsetBitInPayload: href
                offsetByte: href
                offsetLength: href
                useSequenceNoInPayload: href
                tunnelAuthentication: href
                useHiddenAVPs: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnLnsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnLnsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLnsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnLnsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnLnsAuthCredentialsEmulation(IxnEmulationHost):
    """Generated NGPF lnsAuthCredentials emulation host """


    def __init__(self, ixnhttp):
        super(IxnLnsAuthCredentialsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific lnsAuthCredentials emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                lacHostName: href
                lacSecret: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnLnsAuthCredentialsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","lnsAuthCredentials"], vport_name, emulation_host, filters)


class IxnLocalIpBaseEmulation(IxnEmulationHost):
    """Generated NGPF localIpBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnLocalIpBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific localIpBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnLocalIpBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","localIpBase"], vport_name, emulation_host, filters)


class IxnMacPoolsEmulation(IxnEmulationHost):
    """Generated NGPF macPools emulation host """


    def __init__(self, ixnhttp):
        super(IxnMacPoolsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific macPools emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                mac: href
                prefixLength: href
                numberOfAddresses: number
                lastMacAddress: list
                enableVlans: href
                vlanCount: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMacPoolsEmulation, self).find(["topology","deviceGroup","networkGroup","macPools"], vport_name, emulation_host, filters)


class IxnManagerEmulation(IxnEmulationHost):
    """Generated NGPF manager emulation host """


    def __init__(self, ixnhttp):
        super(IxnManagerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific manager emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                managerActive: href
                managerIp: href
                tcpPort: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnManagerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ovsdbserver","manager"], vport_name, emulation_host, filters)


class IxnMatchActionEmulation(IxnEmulationHost):
    """Generated NGPF matchAction emulation host """


    def __init__(self, ixnhttp):
        super(IxnMatchActionEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific matchAction emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnMatchActionEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","tables","flowSet","flowProfile","matchAction"], vport_name, emulation_host, filters)


class IxnMatchCriteriaEmulation(IxnEmulationHost):
    """Generated NGPF matchCriteria emulation host """


    def __init__(self, ixnhttp):
        super(IxnMatchCriteriaEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific matchCriteria emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                description: string
                isRequired: bool
                isEditable: bool
                isEnabled: bool
                displayName: string
                count: number
        """
        return super(IxnMatchCriteriaEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","flowStatMatchProfile","matchCriteria"], vport_name, emulation_host, filters)


class IxnMetersEmulation(IxnEmulationHost):
    """Generated NGPF meters emulation host """


    def __init__(self, ixnhttp):
        super(IxnMetersEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific meters emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                multiplier: number
                meterDesc: href
                numberOfBands: number
                meterId: href
                flags: href
                advertise: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMetersEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","meters"], vport_name, emulation_host, filters)


class IxnMissSndLengthEmulation(IxnEmulationHost):
    """Generated NGPF missSndLength emulation host """


    def __init__(self, ixnhttp):
        super(IxnMissSndLengthEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific missSndLength emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnMissSndLengthEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","switchConfigLearnedInfo","missSndLength"], vport_name, emulation_host, filters)


class IxnMldHostEmulation(IxnEmulationHost):
    """Generated NGPF mldHost emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnMldHostEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific mldHost emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                versionType: href
                noOfGrpRanges: number
                routerAlert: href
                gQResponseMode: href
                gSResponseMode: href
                uSResponseMode: href
                reportFreq: href
                imResponse: href
                jlMultiplier: number
                enableProxyReporting: href
                enableIptv: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnMldHostEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","mldHost"], vport_name, emulation_host, filters)

    def mldstarthost(self, expected_state=None, timeout=None):
        """Start MLD Host
            For expected_state options see the class state variables
        """
        super(IxnMldHostEmulation, self).call_operation('mldStartHost', expected_state, timeout)

    def mldstophost(self, expected_state=None, timeout=None):
        """Stop MLD Host
            For expected_state options see the class state variables
        """
        super(IxnMldHostEmulation, self).call_operation('mldStopHost', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnMldHostEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMldHostEmulation, self).call_operation('start', expected_state, timeout)

    def startmld(self, expected_state=None, timeout=None):
        """Start MLD protocol on selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnMldHostEmulation, self).call_operation('startMLD', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMldHostEmulation, self).call_operation('stop', expected_state, timeout)

    def stopmld(self, expected_state=None, timeout=None):
        """Stop MLD protocol on selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnMldHostEmulation, self).call_operation('stopMLD', expected_state, timeout)


class IxnMldMcastIPv6GroupListEmulation(IxnEmulationHost):
    """Generated NGPF mldMcastIPv6GroupList emulation host """

    STATE_IPTV = 'iptv'
    STATE_JOINED = 'joined'
    STATE_NOTJOINED = 'notJoined'
    STATE_NOTSTARTED = 'notStarted'

    def __init__(self, ixnhttp):
        super(IxnMldMcastIPv6GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific mldMcastIPv6GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startMcastAddr: href
                mcastAddrIncr: href
                sourceMode: href
                noOfSrcRanges: number
                mcastAddrCnt: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMldMcastIPv6GroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","mldHost","mldMcastIPv6GroupList"], vport_name, emulation_host, filters)

    def mldjoingroup(self, expected_state=None, timeout=None):
        """Join Group
            For expected_state options see the class state variables
        """
        super(IxnMldMcastIPv6GroupListEmulation, self).call_operation('mldJoinGroup', expected_state, timeout)

    def mldleavegroup(self, expected_state=None, timeout=None):
        """Leave Group
            For expected_state options see the class state variables
        """
        super(IxnMldMcastIPv6GroupListEmulation, self).call_operation('mldLeaveGroup', expected_state, timeout)


class IxnMldQuerierEmulation(IxnEmulationHost):
    """Generated NGPF mldQuerier emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnMldQuerierEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific mldQuerier emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                versionType: href
                startupQueryCount: href
                generalQueryInterval: href
                routerAlert: href
                robustnessVariable: href
                generalQueryResponseInterval: href
                specificQueryResponseInterval: href
                specificQueryTransmissionCount: href
                supportElection: href
                supportOlderVersionHost: href
                supportOlderVersionQuerier: href
                discardLearntInfo: href
                proxyQuerier: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnMldQuerierEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","mldQuerier"], vport_name, emulation_host, filters)

    def mldgetlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('mldGetLearnedInfo', expected_state, timeout)

    def mldresumeperiodicgenquery(self, expected_state=None, timeout=None):
        """Resume Periodic General Query
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('mldResumePeriodicGenQuery', expected_state, timeout)

    def mldstartquerier(self, expected_state=None, timeout=None):
        """Start MLD Querier
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('mldStartQuerier', expected_state, timeout)

    def mldstopperiodicgenquery(self, expected_state=None, timeout=None):
        """Stop Periodic General Query
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('mldStopPeriodicGenQuery', expected_state, timeout)

    def mldstopquerier(self, expected_state=None, timeout=None):
        """Stop MLD Querier
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('mldStopQuerier', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('start', expected_state, timeout)

    def startmld(self, expected_state=None, timeout=None):
        """Start MLD protocol on selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('startMLD', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('stop', expected_state, timeout)

    def stopmld(self, expected_state=None, timeout=None):
        """Stop MLD protocol on selected interfaces
            For expected_state options see the class state variables
        """
        super(IxnMldQuerierEmulation, self).call_operation('stopMLD', expected_state, timeout)


class IxnMldUcastIPv6SourceListEmulation(IxnEmulationHost):
    """Generated NGPF mldUcastIPv6SourceList emulation host """

    STATE_IPTV = 'iptv'
    STATE_JOINED = 'joined'
    STATE_NOTJOINED = 'notJoined'
    STATE_NOTSTARTED = 'notStarted'

    def __init__(self, ixnhttp):
        super(IxnMldUcastIPv6SourceListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific mldUcastIPv6SourceList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startUcastAddr: href
                ucastAddrIncr: href
                ucastSrcAddrCnt: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMldUcastIPv6SourceListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","mldHost","mldMcastIPv6GroupList","mldUcastIPv6SourceList"], vport_name, emulation_host, filters)

    def mldjoinsource(self, expected_state=None, timeout=None):
        """Join Source
            For expected_state options see the class state variables
        """
        super(IxnMldUcastIPv6SourceListEmulation, self).call_operation('mldJoinSource', expected_state, timeout)

    def mldleavesource(self, expected_state=None, timeout=None):
        """Leave Source
            For expected_state options see the class state variables
        """
        super(IxnMldUcastIPv6SourceListEmulation, self).call_operation('mldLeaveSource', expected_state, timeout)


class IxnMplsEmulation(IxnEmulationHost):
    """Generated NGPF mpls emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnMplsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific mpls emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                upperLayer: enum
                txLabelValue: href
                rxLabelValue: href
                enablecw: bool
                overridecos: bool
                cos: href
                bos: href
                ttl: href
                destMac: href
                transportType: enum
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnMplsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","mpls"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnMplsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMplsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMplsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnMplsOamEmulation(IxnEmulationHost):
    """Generated NGPF mplsOam emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnMplsOamEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific mplsOam emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localRouterId: list
                controlChannel: href
                bfdCvType: href
                enablePeriodicPing: href
                replyMode: href
                enableFecValidation: href
                destinationAddressIpv4: href
                includePadTlv: href
                padTlvLength: href
                padTlvFirstOctet: href
                includeVendorEnterpriseNumbeTlv: href
                vendorEnterpriseNumber: href
                echoResponseTimeout: href
                echoRequestInterval: href
                enableDownstreamMappingTlv: href
                enableDSIflag: href
                enableDsNflag: href
                downstreamAddressType: href
                downstreamIpAddress: href
                downstreamInterfaceAddressUnnumbered: href
                downstreamInterfaceAddressNumbered: href
                minRxInterval: href
                txInterval: href
                timeoutMultiplier: href
                flapTxIntervals: href
                bfdDiscriminatorStart: href
                bfdDiscriminatorEnd: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnMplsOamEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","mplsOam"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnMplsOamEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate Interface
            For expected_state options see the class state variables
        """
        super(IxnMplsOamEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Interface
            For expected_state options see the class state variables
        """
        super(IxnMplsOamEmulation, self).call_operation('stop', expected_state, timeout)


class IxnMplsoamRouterEmulation(IxnEmulationHost):
    """Generated NGPF mplsoamRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnMplsoamRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific mplsoamRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localRouterId: list
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnMplsoamRouterEmulation, self).find(["topology","deviceGroup","mplsoamRouter"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnMplsoamRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMplsoamRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnMplsoamRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnMsrpListenerEmulation(IxnEmulationHost):
    """Generated NGPF msrpListener emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnMsrpListenerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific msrpListener emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                declareUnsolicitedVlan: bool
                startVlanId: href
                vlanCount: href
                advertiseAs: href
                subscribeAll: bool
                subscribedStreamCount: number
                listenerDomainCount: number
                portData: href
                protocolVersion: href
                joinTimer: href
                leaveTimer: href
                leaveAllTimer: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnMsrpListenerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","msrpListener"], vport_name, emulation_host, filters)

    def clearlistenerdatabasesinclient(self, expected_state=None, timeout=None):
        """Clears ALL databases learnt by this MSRP Listener.
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('clearListenerDatabasesInClient', expected_state, timeout)

    def getlistenerdatabases(self, expected_state=None, timeout=None):
        """Gets All databases learnt by this MSRP Listener
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('getListenerDatabases', expected_state, timeout)

    def getmsrplistenerdomaindatabase(self, expected_state=None, timeout=None):
        """Gets Listener Domain Database Information learnt by this Msrp Listener
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('getMsrpListenerDomainDatabase', expected_state, timeout)

    def getmsrplistenerstreamdatabase(self, expected_state=None, timeout=None):
        """Gets Listener Stream Database Information learnt by this Msrp Listener.
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('getMsrpListenerStreamDatabase', expected_state, timeout)

    def getmsrplistenervlandatabase(self, expected_state=None, timeout=None):
        """Gets Listener VLAN Database Information learnt by this Msrp Listener
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('getMsrpListenerVlanDatabase', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start MSRP Listener
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop MSRP Listener
            For expected_state options see the class state variables
        """
        super(IxnMsrpListenerEmulation, self).call_operation('stop', expected_state, timeout)


class IxnMsrpListenerDomainsEmulation(IxnEmulationHost):
    """Generated NGPF msrpListenerDomains emulation host """


    def __init__(self, ixnhttp):
        super(IxnMsrpListenerDomainsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific msrpListenerDomains emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srClassIdType: href
                srClassPriorityType: href
                srClassVid: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMsrpListenerDomainsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","msrpListener","msrpListenerDomains"], vport_name, emulation_host, filters)


class IxnMsrpTalkerEmulation(IxnEmulationHost):
    """Generated NGPF msrpTalker emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnMsrpTalkerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific msrpTalker emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                streamCount: number
                talkerDomainCount: number
                advertiseAs: href
                advertiseVlanMembership: bool
                portData: href
                protocolVersion: href
                joinTimer: href
                leaveTimer: href
                leaveAllTimer: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnMsrpTalkerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","msrpTalker"], vport_name, emulation_host, filters)

    def cleartalkerdatabasesinclient(self, expected_state=None, timeout=None):
        """Clears ALL databses learnt by this MSRP Talker.
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('clearTalkerDatabasesInClient', expected_state, timeout)

    def getmsrptalkerdomaindatabase(self, expected_state=None, timeout=None):
        """Gets Talker Domain Database Information learnt by this Msrp Talker
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('getMsrpTalkerDomainDatabase', expected_state, timeout)

    def getmsrptalkerstreamdatabase(self, expected_state=None, timeout=None):
        """Gets Talker Stream Database Information learnt by this Msrp Talker
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('getMsrpTalkerStreamDatabase', expected_state, timeout)

    def getmsrptalkervlandatabase(self, expected_state=None, timeout=None):
        """Gets Talker VLAN Database Information learnt by this Msrp Talker
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('getMsrpTalkerVlanDatabase', expected_state, timeout)

    def gettalkerdatabases(self, expected_state=None, timeout=None):
        """Gets All databses learnt by this MSRP Talker
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('getTalkerDatabases', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start MSRP Talker
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop MSRP Talker
            For expected_state options see the class state variables
        """
        super(IxnMsrpTalkerEmulation, self).call_operation('stop', expected_state, timeout)


class IxnMsrpTalkerDomainsEmulation(IxnEmulationHost):
    """Generated NGPF msrpTalkerDomains emulation host """


    def __init__(self, ixnhttp):
        super(IxnMsrpTalkerDomainsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific msrpTalkerDomains emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srClassIdType: href
                srClassPriorityType: href
                srClassVid: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMsrpTalkerDomainsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","msrpTalker","msrpTalkerDomains"], vport_name, emulation_host, filters)


class IxnNegotiatedVersionBaseEmulation(IxnEmulationHost):
    """Generated NGPF negotiatedVersionBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnNegotiatedVersionBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific negotiatedVersionBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnNegotiatedVersionBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","negotiatedVersionBase"], vport_name, emulation_host, filters)


class IxnNetTopologyCustomEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyCustom emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyCustomEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyCustom emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfNodes: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyCustomEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyCustom"], vport_name, emulation_host, filters)


class IxnNetTopologyFatTreeEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyFatTree emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyFatTreeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyFatTree emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                levelCount: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyFatTreeEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyFatTree"], vport_name, emulation_host, filters)


class IxnNetTopologyGridEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyGrid emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyGridEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyGrid emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rows: number
                columns: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyGridEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyGrid"], vport_name, emulation_host, filters)


class IxnNetTopologyHubNSpokeEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyHubNSpoke emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyHubNSpokeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyHubNSpoke emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfFirstLevelSpokes: number
                enableLevel2Spokes: bool
                numberOfSecondLevelSpokes: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyHubNSpokeEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyHubNSpoke"], vport_name, emulation_host, filters)


class IxnNetTopologyLinearEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyLinear emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyLinearEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyLinear emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nodes: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyLinearEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyLinear"], vport_name, emulation_host, filters)


class IxnNetTopologyMeshEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyMesh emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyMeshEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyMesh emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nodes: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyMeshEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyMesh"], vport_name, emulation_host, filters)


class IxnNetTopologyRingEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyRing emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyRingEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyRing emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nodes: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyRingEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyRing"], vport_name, emulation_host, filters)


class IxnNetTopologyTreeEmulation(IxnEmulationHost):
    """Generated NGPF netTopologyTree emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetTopologyTreeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific netTopologyTree emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nodes: number
                useTreeDepth: bool
                treeDepth: number
                maxChildPerNode: number
                linkMultiplier: number
                includeEntryPoint: bool
        """
        return super(IxnNetTopologyTreeEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","netTopologyTree"], vport_name, emulation_host, filters)


class IxnNetworkGroupEmulation(IxnEmulationHost):
    """Generated NGPF networkGroup emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetworkGroupEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific networkGroup emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                multiplier: number
                enabled: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnNetworkGroupEmulation, self).find(["topology","deviceGroup","networkGroup"], vport_name, emulation_host, filters)


class IxnNetworkRangeInfoEmulation(IxnEmulationHost):
    """Generated NGPF networkRangeInfo emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetworkRangeInfoEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific networkRangeInfo emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numColumns: href
                numRows: href
                networkRangeLinkType: href
                networkRangeRID: href
                networkRangeRIDIncrement: href
                networkRangeInterfaceIp: href
                networkRangeInterfaceIpMask: href
                networkRangeIp: href
                networkRangeIPByMask: href
                networkRangeIpMask: href
                networkRangeIpIncrementBy: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnNetworkRangeInfoEmulation, self).find(["topology","deviceGroup","networkGroup","networkRangeInfo"], vport_name, emulation_host, filters)


class IxnNetworkTopologyEmulation(IxnEmulationHost):
    """Generated NGPF networkTopology emulation host """


    def __init__(self, ixnhttp):
        super(IxnNetworkTopologyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific networkTopology emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nodesPerNetwork: number
                linksPerNetwork: number
                count: number
        """
        return super(IxnNetworkTopologyEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology"], vport_name, emulation_host, filters)


class IxnNicknameRecordListEmulation(IxnEmulationHost):
    """Generated NGPF nicknameRecordList emulation host """


    def __init__(self, ixnhttp):
        super(IxnNicknameRecordListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific nicknameRecordList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                nickname: href
                priority: href
                broadcastRootPriority: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnNicknameRecordListEmulation, self).find(["topology","deviceGroup","isisFabricPathRouter","dceTopologyList","nicknameRecordList"], vport_name, emulation_host, filters)


class IxnNssaRoutesEmulation(IxnEmulationHost):
    """Generated NGPF nssaRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnNssaRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific nssaRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                propagate: href
                includeForwardingAddress: href
                forwardingAddress: href
                linkStateId: href
                linkStateIdStep: href
                active: href
                networkAddress: href
                rangeSize: href
                prefix: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnNssaRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfv3PseudoRouter","nssaRoutes"], vport_name, emulation_host, filters)


class IxnOFSwitchLearnedInfoConfigEmulation(IxnEmulationHost):
    """Generated NGPF oFSwitchLearnedInfoConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnOFSwitchLearnedInfoConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific oFSwitchLearnedInfoConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                flowStatTableIdMode: enum
                flowStatTableIdValue: number
                flowStatOutPortMode: enum
                flowStatOutPortValue: number
                flowStatOutGroupMode: enum
                flowStatOutGroupValue: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOFSwitchLearnedInfoConfigEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch","oFSwitchLearnedInfoConfig"], vport_name, emulation_host, filters)


class IxnOfChannelLearnedInfoListEmulation(IxnEmulationHost):
    """Generated NGPF ofChannelLearnedInfoList emulation host """


    def __init__(self, ixnhttp):
        super(IxnOfChannelLearnedInfoListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ofChannelLearnedInfoList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                localIp: list
                remoteIp: list
                datapathId: list
                datapathIdHex: list
                oFVersion: list
                oFRole: list
                onDemandMessages: href
                basicLiLocalIp: list
                basicLiRemoteIp: list
                basicLiDatapathID: list
                groupFeatureResponseTimeOut: number
                groupDescResponseTimeOut: number
                groupStatResponseTimeOut: number
                groupStatMatchCapability: bool
                groupStatIDType: enum
                groupStatIDValue: number
                meterFeatureStatResponseTimeOut: number
                meterConfigResponseTimeOut: number
                meterConfigMeterID: enum
                meterConfigMeterIDManual: number
                meterStatResponseTimeOut: number
                meterStatMeterIDType: enum
                meterStatMeterID: number
                vendorStatResponseTimeOut: number
                vendorStatId: number
                vendorStatExpType: number
                vendorStatSendData: bool
                vendorStatMessage: href
                vendorMsgId: number
                vendorMsgExpType: number
                vendorMsgSendData: bool
                vendorMsgMessage: href
                descriptionStatResponseTimeOut: number
                queueConfigResponseTimeOut: number
                queueConfigPortNumberType: enum
                queueConfigPortNumberValue: number
                queueStatIDType: enum
                queueStatIDValue: number
                queueStatResponseTimeOut: number
                queueStatMatchCapability: bool
                queueStatPortNumberType: enum
                queueStatPortNumberValue: number
                switchConfigResTimeOut: number
                setSwitchConfig: bool
                switchConfigDropFragments: bool
                switchConfigReassembleFragments: bool
                switchConfigMissSendLength: number
                asyncConfigResTimeOut: number
                setAsyncConfig: bool
                asyncConfigPktInMaster: href
                asyncConfigPortStatusMaster: href
                asyncConfigFlowRemovedMaster: href
                asyncConfigPktInSlave: href
                asyncConfigPortStatusSlave: href
                asyncConfigFlowRemovedSlave: href
                portStatResponseTimeOut: number
                portStatMatchCapability: bool
                portStatPortNumberType: enum
                portStatPortNumberValue: number
                packetOutAuxiliaryID: number
                packetOutInPortType: enum
                packetOutInPort: number
                packetOutBufferIDType: enum
                packetOutBufferID: number
                packetOutSendData: bool
                packetOutData: href
                portFeaturesResponseTimeOut: number
                tableStatResTimeOut: number
                tableStatMatchCap: bool
                flowStatResTimeOut: number
                flowStatMatchCap: bool
                flowStatTableId: enum
                flowStatTableIdValue: number
                flowStatOutPort: enum
                flowStatOutPortValue: number
                flowStatOutGroup: enum
                flowStatOutGroupValue: number
                flowStatCookie: href
                flowStatCookieMask: href
                flowAggrStatResTimeOut: number
                flowAggrStatMatchCap: bool
                flowAggrStatTableId: enum
                flowAggrStatTableIdValue: number
                flowAggrStatOutPort: enum
                flowAggrStatOutPortValue: number
                flowAggrStatOutGroup: enum
                flowAggrStatOutGroupValue: number
                flowAggrStatCookie: href
                flowAggrStatCookieMask: href
                roleType: enum
                generationId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOfChannelLearnedInfoListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList"], vport_name, emulation_host, filters)


class IxnOfHostDataEmulation(IxnEmulationHost):
    """Generated NGPF ofHostData emulation host """


    def __init__(self, ixnhttp):
        super(IxnOfHostDataEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ofHostData emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                numberOfHostPorts: number
                numberOfHostsPerPort: number
                parentSwitchPortName: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOfHostDataEmulation, self).find(["topology","deviceGroup","ofHostData"], vport_name, emulation_host, filters)


class IxnOfLearnedInfoTriggerParamPortFeaturesListEmulation(IxnEmulationHost):
    """Generated NGPF ofLearnedInfoTriggerParamPortFeaturesList emulation host """


    def __init__(self, ixnhttp):
        super(IxnOfLearnedInfoTriggerParamPortFeaturesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ofLearnedInfoTriggerParamPortFeaturesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                responseTimeOut: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOfLearnedInfoTriggerParamPortFeaturesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofLearnedInfoTriggerParamPortFeaturesList"], vport_name, emulation_host, filters)


class IxnOfPortFeaturesLearnedInfoListEmulation(IxnEmulationHost):
    """Generated NGPF ofPortFeaturesLearnedInfoList emulation host """


    def __init__(self, ixnhttp):
        super(IxnOfPortFeaturesLearnedInfoListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ofPortFeaturesLearnedInfoList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                localIp: list
                remoteIp: list
                datapathId: list
                datapathIdHex: list
                oFVersion: list
                oFPortNumber: list
                oFPortName: list
                oFPortEtherAddr: list
                portModPortNumber: number
                customPortNumber: bool
                portModEtherAddr: href
                customEtherAddr: bool
                portAdminDown: bool
                dropFrwdPackets: bool
                dropAllPkts: bool
                dontSendPktIn: bool
                customPortConf: bool
                customConfig: number
                customMask: number
                linkMode: href
                linkType: href
                linkFeature: href
                enableCustomAdvertiseFeature: bool
                customAdvertiseFeature: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOfPortFeaturesLearnedInfoListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofPortFeaturesLearnedInfoList"], vport_name, emulation_host, filters)


class IxnOfSwitchPortsEmulation(IxnEmulationHost):
    """Generated NGPF ofSwitchPorts emulation host """

    STATE_AUTO = 'auto'
    STATE_EXTERNALSWITCH = 'externalSwitch'
    STATE_HOST = 'host'
    STATE_INTERNALSWITCH = 'internalSwitch'
    STATE_NOCONNECTION = 'noConnection'

    def __init__(self, ixnhttp):
        super(IxnOfSwitchPortsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ofSwitchPorts emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                parentSwitch: string
                active: href
                switchIndex: href
                portIndex: href
                portName: href
                portNumber: href
                etherAddr: href
                numQueueRange: number
                config: href
                state: href
                currentFeatures: href
                advertisedFeatures: href
                supportedFeatures: href
                peerAdvertisedFeatures: href
                currentSpeed: href
                maxSpeed: href
                portLivenessSupport: href
                forcedConnectionType: href
                remoteSwitchIndex: href
                remoteSwitch: href
                remotePortIndex: href
                remoteSwitchPort: href
                transmissionDelay: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOfSwitchPortsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch","ofSwitchPorts"], vport_name, emulation_host, filters)


class IxnOfSwitchQueuesEmulation(IxnEmulationHost):
    """Generated NGPF ofSwitchQueues emulation host """


    def __init__(self, ixnhttp):
        super(IxnOfSwitchQueuesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ofSwitchQueues emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                switchIndex: href
                parentPort: href
                queueId: href
                queueProperty: href
                minRate: href
                maxRate: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOfSwitchQueuesEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch","ofSwitchPorts","ofSwitchQueues"], vport_name, emulation_host, filters)


class IxnOpenFlowChannelEmulation(IxnEmulationHost):
    """Generated NGPF openFlowChannel emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOpenFlowChannelEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific openFlowChannel emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                remoteIp: href
                tablesPerChannel: number
                groupsPerChannel: number
                metersPerChannel: number
                sendRoleRequest: href
                startupRoleRequest: href
                startupGenerationId: href
                maxFlowsAtATime: href
                calcFlowRate: href
                flowTxBurstSize: href
                interFlowBurstGap: href
                calcFlowRateWithBarrier: href
                enableHelloElement: href
                useDatapathID: href
                datapathId: href
                datapathIdHex: href
                controllerName: string
                controllerIndex: list
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOpenFlowChannelEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel"], vport_name, emulation_host, filters)

    def getasynchronousconfiguration(self, expected_state=None, timeout=None):
        """Get Asynchronous Configurationr
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('getAsynchronousConfiguration', expected_state, timeout)

    def pauseechoreply(self, expected_state=None, timeout=None):
        """Pause Sending Echo Reply Messages
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('pauseEchoReply', expected_state, timeout)

    def pauseechorequest(self, expected_state=None, timeout=None):
        """Pause Sending Echo Request Messages
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('pauseEchoRequest', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumeechoreply(self, expected_state=None, timeout=None):
        """Resume Sending Echo Reply Messages
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('resumeEchoReply', expected_state, timeout)

    def resumeechorequest(self, expected_state=None, timeout=None):
        """Resume Sending Echo Request Messages
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('resumeEchoRequest', expected_state, timeout)

    def sendbarrierrequest(self, expected_state=None, timeout=None):
        """Send Barrier Request to Switch
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendBarrierRequest', expected_state, timeout)

    def sendconfigrequest(self, expected_state=None, timeout=None):
        """Send Config Request to Switch
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendConfigRequest', expected_state, timeout)

    def senddescriptionstatrequest(self, expected_state=None, timeout=None):
        """Send Description Stat Request
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendDescriptionStatRequest', expected_state, timeout)

    def sendfeaturerequest(self, expected_state=None, timeout=None):
        """Send Feature Request to Switch
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendFeatureRequest', expected_state, timeout)

    def sendgroupdescriptionrequest(self, expected_state=None, timeout=None):
        """Send Group Description Request to Switch
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendGroupDescriptionRequest', expected_state, timeout)

    def sendgroupfeaturesrequest(self, expected_state=None, timeout=None):
        """Send Group Features Request to Switch
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendGroupFeaturesRequest', expected_state, timeout)

    def sendmeterfeaturesrequest(self, expected_state=None, timeout=None):
        """Send Meter Features Request to Switch
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendMeterFeaturesRequest', expected_state, timeout)

    def sendportdescription(self, expected_state=None, timeout=None):
        """Send Port Description
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendPortDescription', expected_state, timeout)

    def sendtablestatsrequest(self, expected_state=None, timeout=None):
        """Send Table Stats Request to Switch
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('sendTableStatsRequest', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('start', expected_state, timeout)

    def startchannel(self, expected_state=None, timeout=None):
        """Start OpenFlow Channel
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('startChannel', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('stop', expected_state, timeout)

    def stopchannel(self, expected_state=None, timeout=None):
        """Stop OpenFlow Channel
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowChannelEmulation, self).call_operation('stopChannel', expected_state, timeout)


class IxnOpenFlowControllerEmulation(IxnEmulationHost):
    """Generated NGPF openFlowController emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOpenFlowControllerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific openFlowController emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                controllerLocalIp: list
                numberOfChannels: number
                version: number
                versionSupported: href
                modeOfConnection: href
                typeOfConnection: href
                tcpPort: href
                directoryName: href
                filePrivKey: href
                fileCertificate: href
                fileCaCertificate: href
                periodicLLDP: href
                periodicLLDPInterval: href
                installFlowForLLDP: href
                lldpDstMacAddress: href
                auxNonHelloStartupOption: href
                badVersionErrorAction: href
                auxConnTimeout: href
                featRequestTimeout: href
                featureRquestTimeoutAction: href
                periodicEcho: href
                echoInterval: href
                echoTimeOut: href
                timeoutOption: href
                timeoutOptionValue: href
                sendPortFeatureAtStartup: href
                acceptUnconfiguredChannel: href
                delFlowsAtStartup: href
                startupFeatureRequest: href
                startupEmptyTableFeatureRequest: href
                triggerLldp: href
                installLLDPFlow: href
                lLDPDestinactionMac: href
                responseTimeout: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOpenFlowControllerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getofchannellearnedinfo(self, expected_state=None, timeout=None):
        """Get OF Channel Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('getOFChannelLearnedInfo', expected_state, timeout)

    def getoftopologylearnedinfo(self, expected_state=None, timeout=None):
        """Get OF Topology Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('getOFTopologyLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('start', expected_state, timeout)

    def startcontroller(self, expected_state=None, timeout=None):
        """Start OpenFlow Controller
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('startController', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('stop', expected_state, timeout)

    def stopcontroller(self, expected_state=None, timeout=None):
        """Stop OpenFlow Controller
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowControllerEmulation, self).call_operation('stopController', expected_state, timeout)


class IxnOpenFlowSwitchEmulation(IxnEmulationHost):
    """Generated NGPF openFlowSwitch emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOpenFlowSwitchEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific openFlowSwitch emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                switchDesc: href
                switchLocalIp: list
                numberOfChannels: number
                numberOfTableRanges: number
                versionSupported: href
                datapathId: href
                datapathIdHex: href
                typeOfConnection: href
                tcpPort: href
                directoryName: href
                filePrivKey: href
                fileCertificate: href
                fileCaCertificate: href
                periodicEcho: href
                echoInterval: href
                echoTimeOut: href
                timeoutOption: href
                timeoutOptionValue: href
                enableHelloElement: href
                transactionID: href
                capabilities: href
                packetInMaskMaster: href
                packetInMaskSlave: href
                portStatusMaskMaster: href
                portStatusMaskSlave: href
                storeFlows: href
                controllerFlowTxRate: href
                tableMissAction: href
                flowRemovedMask: href
                flowRemovedMaskSlave: href
                barrierReplyDelayType: href
                barrierReplyMaxDelay: href
                manufacturerDesc: href
                hardwareDesc: href
                softwareDesc: href
                serialNumber: href
                datapathDesc: href
                numberOfPorts: number
                numberOfTopologyPorts: number
                numberOfHostPorts: number
                numberOfUnconnectedPorts: number
                numberOfPacketIn: number
                numberOfBuffers: href
                maxPacketInBytes: href
                packetInTxBurst: href
                interPacketInBurstGap: href
                packetInReplyDelay: href
                packetInReplyTimeout: href
                packetOutRxRate: href
                auxNonHelloStartupOption: href
                badVersionErrorAction: href
                auxConnTimeout: href
                groupType: href
                groupCapabilities: href
                maxNumberOfBucketsPerGroups: href
                numMeter: href
                bandTypes: href
                meterCapabilities: href
                maxBandPerMeter: href
                maxColorValue: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOpenFlowSwitchEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowSwitchEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowSwitchEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOpenFlowSwitchEmulation, self).call_operation('stop', expected_state, timeout)


class IxnOspfPseudoInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF ospfPseudoInterface emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfPseudoInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfPseudoInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                enable: href
                metricLevel: href
                administratorGroup: href
                maxBandwidth: href
                maxReservableBandwidth: href
                bandwidthPriority0: href
                bandwidthPriority1: href
                bandwidthPriority2: href
                bandwidthPriority3: href
                bandwidthPriority4: href
                bandwidthPriority5: href
                bandwidthPriority6: href
                bandwidthPriority7: href
                enableSRLG: href
                srlgCount: number
                enLinkProtection: href
                extraTraffic: href
                unprotected: href
                shared: href
                dedicated1To1: href
                dedicated1Plus1: href
                enhanced: href
                reserved40: href
                reserved80: href
                enableAdjSID: href
                adjSID: href
                bFlag: href
                vFlag: href
                lFlag: href
                sFlag: href
                weight: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfPseudoInterfaceEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","simInterfaceIPv4Config","ospfPseudoInterface"], vport_name, emulation_host, filters)


class IxnOspfPseudoRouterEmulation(IxnEmulationHost):
    """Generated NGPF ospfPseudoRouter emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfPseudoRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfPseudoRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                advertiseRouterIdAsStubNetwork: href
                bBit: href
                eBit: href
                enableSegmentRouting: bool
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                srgbRangeCount: number
                sRAlgorithmCount: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfPseudoRouterEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfPseudoRouter"], vport_name, emulation_host, filters)


class IxnOspfPseudoRouterStubNetworksEmulation(IxnEmulationHost):
    """Generated NGPF ospfPseudoRouterStubNetworks emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfPseudoRouterStubNetworksEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfPseudoRouterStubNetworks emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                networkAddress: href
                rangeSize: href
                prefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfPseudoRouterStubNetworksEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfPseudoRouter","ospfPseudoRouterStubNetworks"], vport_name, emulation_host, filters)


class IxnOspfPseudoRouterStubRoutesEmulation(IxnEmulationHost):
    """Generated NGPF ospfPseudoRouterStubRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfPseudoRouterStubRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfPseudoRouterStubRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                networkAddress: href
                rangeSize: href
                prefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfPseudoRouterStubRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfPseudoRouter","ospfPseudoRouterStubRoutes"], vport_name, emulation_host, filters)


class IxnOspfPseudoRouterSummaryRoutesEmulation(IxnEmulationHost):
    """Generated NGPF ospfPseudoRouterSummaryRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfPseudoRouterSummaryRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfPseudoRouterSummaryRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                networkAddress: href
                rangeSize: href
                prefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfPseudoRouterSummaryRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfPseudoRouter","ospfPseudoRouterSummaryRoutes"], vport_name, emulation_host, filters)


class IxnOspfPseudoRouterType1ExtRoutesEmulation(IxnEmulationHost):
    """Generated NGPF ospfPseudoRouterType1ExtRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfPseudoRouterType1ExtRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfPseudoRouterType1ExtRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                networkAddress: href
                rangeSize: href
                prefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfPseudoRouterType1ExtRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfPseudoRouter","ospfPseudoRouterType1ExtRoutes"], vport_name, emulation_host, filters)


class IxnOspfPseudoRouterType2ExtRoutesEmulation(IxnEmulationHost):
    """Generated NGPF ospfPseudoRouterType2ExtRoutes emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfPseudoRouterType2ExtRoutesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfPseudoRouterType2ExtRoutes emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                networkAddress: href
                rangeSize: href
                prefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfPseudoRouterType2ExtRoutesEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfPseudoRouter","ospfPseudoRouterType2ExtRoutes"], vport_name, emulation_host, filters)


class IxnOspfRoutePropertyEmulation(IxnEmulationHost):
    """Generated NGPF ospfRouteProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfRoutePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfRouteProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                routeOrigin: href
                allowPropagate: href
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfRoutePropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","ospfRouteProperty"], vport_name, emulation_host, filters)


class IxnOspfSRAlgorithmListEmulation(IxnEmulationHost):
    """Generated NGPF ospfSRAlgorithmList emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfSRAlgorithmListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfSRAlgorithmList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                ospfSrAlgorithm: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfSRAlgorithmListEmulation, self).find(["topology","deviceGroup","ospfv2Router","ospfSRAlgorithmList"], vport_name, emulation_host, filters)


class IxnOspfSRGBRangeSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF ospfSRGBRangeSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfSRGBRangeSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfSRGBRangeSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                startSIDLabel: href
                sidCount: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfSRGBRangeSubObjectsListEmulation, self).find(["topology","deviceGroup","ospfv2Router","ospfSRGBRangeSubObjectsList"], vport_name, emulation_host, filters)


class IxnOspfSRMappingServerListEmulation(IxnEmulationHost):
    """Generated NGPF ospfSRMappingServerList emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfSRMappingServerListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfSRMappingServerList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localRouterID: list
                networkAddress: href
                prefixLength: href
                range: href
                lastNetworkAddress: list
                iaFlag: href
                sidIndexLabel: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                algorithm: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfSRMappingServerListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ospfv2","ospfSRMappingServerList"], vport_name, emulation_host, filters)


class IxnOspfSimulatedTopologyConfigEmulation(IxnEmulationHost):
    """Generated NGPF ospfSimulatedTopologyConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfSimulatedTopologyConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfSimulatedTopologyConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfSimulatedTopologyConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","ospfSimulatedTopologyConfig"], vport_name, emulation_host, filters)


class IxnOspfTrafficEngineeringEmulation(IxnEmulationHost):
    """Generated NGPF ospfTrafficEngineering emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfTrafficEngineeringEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfTrafficEngineering emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enable: href
                metricLevel: href
                administratorGroup: href
                maxBandwidth: href
                maxReservableBandwidth: href
                bandwidthPriority0: href
                bandwidthPriority1: href
                bandwidthPriority2: href
                bandwidthPriority3: href
                bandwidthPriority4: href
                bandwidthPriority5: href
                bandwidthPriority6: href
                bandwidthPriority7: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfTrafficEngineeringEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ospfv2","ospfTrafficEngineering"], vport_name, emulation_host, filters)


class IxnOspfv2Emulation(IxnEmulationHost):
    """Generated NGPF ospfv2 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOspfv2Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv2 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localRouterID: list
                typeAreaId: href
                areaId: href
                areaIdIp: href
                networkType: href
                neighborIp: href
                enableBfdRegistration: href
                enableSRLG: href
                srlgCount: number
                enLinkProtection: href
                extraTraffic: href
                unprotected: href
                shared: href
                dedicated1To1: href
                dedicated1Plus1: href
                enhanced: href
                reserved40: href
                reserved80: href
                enableAdjSID: href
                adjSID: href
                bFlag: href
                vFlag: href
                lFlag: href
                sFlag: href
                weight: href
                suppressHello: href
                enableFast2wayConvergence: bool
                enableFastHello: href
                helloMultiplier: href
                helloInterval: href
                deadInterval: href
                metric: href
                validateRxMtu: href
                maxMtu: href
                priority: href
                unused: href
                opaqueLsaForwarded: href
                demandCircuit: href
                externalAttribute: href
                nssaCapability: href
                multicastCapability: href
                externalCapability: href
                typeOfServiceRouting: href
                authentication: href
                authenticationPassword: href
                md5KeyId: href
                md5Key: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOspfv2Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ospfv2"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getbasiclearnedinfo(self, expected_state=None, timeout=None):
        """Get Basic Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('getBasicLearnedInfo', expected_state, timeout)

    def getdetailedlearnedinfo(self, expected_state=None, timeout=None):
        """Get Detailed Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('getDetailedLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('restartDown', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume sending OSPFv2 Hellos
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('resumeHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start OSPF Interface
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop OSPF Interface
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('stop', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop sending OSPFv2 Hellos
            For expected_state options see the class state variables
        """
        super(IxnOspfv2Emulation, self).call_operation('stopHello', expected_state, timeout)


class IxnOspfv2RouterEmulation(IxnEmulationHost):
    """Generated NGPF ospfv2Router emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOspfv2RouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv2Router emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                localRouterID: list
                discardLearnedLsa: href
                gracefulRestart: href
                oobResyncBreakout: href
                supportForRfc3623: href
                strictLsaChecking: href
                supportReasonSoftRestart: href
                supportReasonSoftReloadUpgrade: href
                supportReasonSwitchRedundantCntrlProcessor: href
                supportReasonUnknown: href
                doNotGenerateRouterLsa: href
                lsaRetransmitTime: href
                lsaRefreshTime: href
                interFloodLsUpdateBurstGap: href
                maxLsUpdatesPerBurst: href
                loopBackAddress: list
                enableSegmentRouting: bool
                configureSIDIndexLabel: href
                sidIndexLabel: href
                algorithm: href
                npFlag: href
                mFlag: href
                eFlag: href
                vFlag: href
                lFlag: href
                srgbRangeCount: number
                sRAlgorithmCount: number
                enableMappingServer: href
                noOfAddressPrefix: number
                bBit: href
                eBit: href
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOspfv2RouterEmulation, self).find(["topology","deviceGroup","ospfv2Router"], vport_name, emulation_host, filters)

    def ospfstartrouter(self, expected_state=None, timeout=None):
        """Start OSPF Router
            For expected_state options see the class state variables
        """
        super(IxnOspfv2RouterEmulation, self).call_operation('ospfStartRouter', expected_state, timeout)

    def ospfstoprouter(self, expected_state=None, timeout=None):
        """Stop OSPF Router
            For expected_state options see the class state variables
        """
        super(IxnOspfv2RouterEmulation, self).call_operation('ospfStopRouter', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOspfv2RouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOspfv2RouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOspfv2RouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnOspfv3Emulation(IxnEmulationHost):
    """Generated NGPF ospfv3 emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOspfv3Emulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv3 emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localRouterID: list
                typeAreaId: href
                areaId: href
                areaIdIp: href
                networkType: href
                enableFastHello: href
                helloMultiplier: href
                helloInterval: href
                deadInterval: href
                linkMetric: href
                priority: href
                instanceId: href
                enableIgnoreDbDescMtu: href
                enableBfdRegistration: href
                demandCircuit: href
                router: href
                nssaCapability: href
                externalCapability: href
                v6: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOspfv3Emulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ospfv3"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getbasiclearnedinfo(self, expected_state=None, timeout=None):
        """Get Basic Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('getBasicLearnedInfo', expected_state, timeout)

    def getdetailedlearnedinfo(self, expected_state=None, timeout=None):
        """Get Detailed Learned Info
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('getDetailedLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('restartDown', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume sending OSPFv3 Hellos
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('resumeHello', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start OSPFv3 Interface
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop OSPF Interface
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('stop', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop sending OSPFv3 Hellos
            For expected_state options see the class state variables
        """
        super(IxnOspfv3Emulation, self).call_operation('stopHello', expected_state, timeout)


class IxnOspfv3PseudoInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF ospfv3PseudoInterface emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfv3PseudoInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv3PseudoInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfv3PseudoInterfaceEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","simInterfaceIPv6Config","ospfv3PseudoInterface"], vport_name, emulation_host, filters)


class IxnOspfv3PseudoRouterEmulation(IxnEmulationHost):
    """Generated NGPF ospfv3PseudoRouter emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfv3PseudoRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv3PseudoRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                bBit: href
                eBit: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfv3PseudoRouterEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter","ospfv3PseudoRouter"], vport_name, emulation_host, filters)


class IxnOspfv3RoutePropertyEmulation(IxnEmulationHost):
    """Generated NGPF ospfv3RouteProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfv3RoutePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv3RouteProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                metric: href
                routeOrigin: href
                allowPropagate: href
                autoSelectForwardingAddress: href
                forwardingAddress: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfv3RoutePropertyEmulation, self).find(["topology","deviceGroup","networkGroup","macPools","ipv6PrefixPools","ospfv3RouteProperty"], vport_name, emulation_host, filters)


class IxnOspfv3RouterEmulation(IxnEmulationHost):
    """Generated NGPF ospfv3Router emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOspfv3RouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv3Router emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                localRouterId: list
                discardLearnedLsa: href
                enableGracefulRestartHelperMode: href
                enableStrictLsaChecking: href
                enableSupportReasonSwRestart: href
                enableSupportReasonSwReloadUpgrade: href
                enableSupportReasonSwitchToRedundantControlProcessor: href
                enableSupportReasonUnknown: href
                lsaRetransmitTime: href
                lsaRefreshTime: href
                disableAutoGenerateRouterLsa: href
                disableAutoGenerateLinkLsa: href
                maxNumLsaPerSecond: href
                bBit: href
                eBit: href
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOspfv3RouterEmulation, self).find(["topology","deviceGroup","ospfv3Router"], vport_name, emulation_host, filters)

    def ospfv3startrouter(self, expected_state=None, timeout=None):
        """Start OSPFv3 Router
            For expected_state options see the class state variables
        """
        super(IxnOspfv3RouterEmulation, self).call_operation('ospfv3StartRouter', expected_state, timeout)

    def ospfv3stoprouter(self, expected_state=None, timeout=None):
        """Stop OSPFv3 Router
            For expected_state options see the class state variables
        """
        super(IxnOspfv3RouterEmulation, self).call_operation('ospfv3StopRouter', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOspfv3RouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOspfv3RouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOspfv3RouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnOspfv3SimulatedTopologyConfigEmulation(IxnEmulationHost):
    """Generated NGPF ospfv3SimulatedTopologyConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnOspfv3SimulatedTopologyConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ospfv3SimulatedTopologyConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnOspfv3SimulatedTopologyConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","ospfv3SimulatedTopologyConfig"], vport_name, emulation_host, filters)


class IxnOvsdbcontrollerEmulation(IxnEmulationHost):
    """Generated NGPF ovsdbcontroller emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOvsdbcontrollerEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ovsdbcontroller emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vxlan: href
                vxlanReplicator: href
                ovsdbSchema: href
                connectionType: href
                controllerTcpPort: href
                directoryName: href
                filePrivKey: href
                fileCertificate: href
                verifyPeerCertificate: href
                fileCaCertificate: href
                timeOut: number
                dumpdbDirectoryName: href
                enableOvsdbServerIp: href
                enableLogging: bool
                ovsdbServerIp: href
                tableNames: href
                clearDumpDbFiles: href
                errorLogDirectoryName: href
                errorCode: href
                errorTimeStamp: href
                errorDesc: href
                errorPhysicalSwitchName: href
                errorLogicalSwitchName: href
                pseudoConnectedTo: href
                pseudoMultiplier: number
                pseudoConnectedToVxlanReplicator: href
                pseudoMultiplierVxlanReplicator: number
                pseudoConnectedToBfd: href
                pseudoMultiplierBfd: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOvsdbcontrollerEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ovsdbcontroller"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOvsdbcontrollerEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOvsdbcontrollerEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOvsdbcontrollerEmulation, self).call_operation('stop', expected_state, timeout)


class IxnOvsdbserverEmulation(IxnEmulationHost):
    """Generated NGPF ovsdbserver emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnOvsdbserverEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ovsdbserver emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vxlan: href
                ovsdbSchema: href
                connectionType: href
                serverTcpPort: href
                directoryName: href
                filePrivKey: href
                fileCertificate: href
                fileCaCertificate: href
                managerCount: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnOvsdbserverEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ovsdbserver"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnOvsdbserverEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOvsdbserverEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnOvsdbserverEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPacketOutActionProfileEmulation(IxnEmulationHost):
    """Generated NGPF packetOutActionProfile emulation host """


    def __init__(self, ixnhttp):
        super(IxnPacketOutActionProfileEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific packetOutActionProfile emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPacketOutActionProfileEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","packetOutActionProfile"], vport_name, emulation_host, filters)


class IxnPacketsTxEmulation(IxnEmulationHost):
    """Generated NGPF packetsTx emulation host """


    def __init__(self, ixnhttp):
        super(IxnPacketsTxEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific packetsTx emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnPacketsTxEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueStatLearnedInfo","packetsTx"], vport_name, emulation_host, filters)


class IxnPbbEVpnParameterEmulation(IxnEmulationHost):
    """Generated NGPF pbbEVpnParameter emulation host """


    def __init__(self, ixnhttp):
        super(IxnPbbEVpnParameterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pbbEVpnParameter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                usePbbEVpnParameters: bool
                bMac: href
                count: number
        """
        return super(IxnPbbEVpnParameterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","pbbEVpnParameter"], vport_name, emulation_host, filters)


class IxnPcReplyLspParametersEmulation(IxnEmulationHost):
    """Generated NGPF pcReplyLspParameters emulation host """

    STATE_DELEGATEDACTIVE = 'delegatedActive'
    STATE_DELEGATEDDOWN = 'delegatedDown'
    STATE_DELEGATEDGOINGUP = 'delegatedGoingUp'
    STATE_DELEGATEDUP = 'delegatedUp'
    STATE_NOLSPOBJECTINPCREQUEST = 'noLSPObjectInPCRequest'
    STATE_NONE = 'none'
    STATE_NOTDELEGATEDACTIVE = 'notDelegatedActive'
    STATE_NOTDELEGATEDDOWN = 'notDelegatedDown'
    STATE_NOTDELEGATEDGOINGUP = 'notDelegatedGoingUp'
    STATE_NOTDELEGATEDUP = 'notDelegatedUp'
    STATE_PCERRORRECEIVED = 'pcErrorReceived'
    STATE_REMOVEDBYPCC = 'removedByPCC'
    STATE_REPLYSENTREPORTNOTRECEIVED = 'replySentReportNotReceived'

    def __init__(self, ixnhttp):
        super(IxnPcReplyLspParametersEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pcReplyLspParameters emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                responseOptions: href
                responsePathType: href
                includeRp: href
                includeLsp: href
                enableEro: href
                includeMetric: href
                includeBandwidth: href
                includeLspa: href
                reflectRP: href
                requestId: href
                enableLoose: href
                biDirectional: href
                priorityValue: href
                numberOfEroSubObjects: number
                numberOfMetricSubObject: number
                bandwidth: href
                reflectLSP: href
                plspId: href
                includeSymbolicPathNameTlv: href
                symbolicPathName: href
                receivedSymbolicPath: list
                receivedPLSPID: list
                setupPriority: href
                holdingPriority: href
                localProtection: href
                includeAny: href
                includeAll: href
                excludeAny: href
                natureOfIssue: href
                enableCFlag: href
                reflectedObjectNoPath: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPcReplyLspParametersEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pce","pccGroup","pcReplyLspParameters"], vport_name, emulation_host, filters)

    def returndelegation(self, expected_state=None, timeout=None):
        """Return Delegation of PCE-Replied LSPs
            For expected_state options see the class state variables
        """
        super(IxnPcReplyLspParametersEmulation, self).call_operation('returnDelegation', expected_state, timeout)


class IxnPcRequestMatchCriteriaEmulation(IxnEmulationHost):
    """Generated NGPF pcRequestMatchCriteria emulation host """


    def __init__(self, ixnhttp):
        super(IxnPcRequestMatchCriteriaEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pcRequestMatchCriteria emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                matchEndPoints: href
                iroType: href
                ipVersion: href
                srcIpv4Address: href
                destIpv4Address: href
                srcIpv6Address: href
                destIpv6Address: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPcRequestMatchCriteriaEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pce","pccGroup","pcRequestMatchCriteria"], vport_name, emulation_host, filters)


class IxnPccEmulation(IxnEmulationHost):
    """Generated NGPF pcc emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPccEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pcc emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srPceCapability: href
                maximumSidDepth: href
                pceIpv4Address: href
                tcpPort: href
                maxLspsPerPcRpt: href
                keepaliveInterval: href
                deadInterval: href
                stateTimeoutInterval: href
                reconnectInterval: href
                maxReconnectInterval: href
                returnInstantiationError: href
                errorValue: href
                authentication: href
                mD5Key: href
                requestedLspsPerPcc: number
                preEstablishedSrLspsPerPcc: number
                active_pre_established_lsps: number
                expectedInitiatedLspsForTraffic: number
                numberOfBackupPCEs: number
                rateControl: href
                burstInterval: href
                maxRequestedLspPerInterval: href
                maxSyncLspPerInterval: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPccEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcc"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPccEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPccEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPccEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPccGroupEmulation(IxnEmulationHost):
    """Generated NGPF pccGroup emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPccGroupEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pccGroup emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                pccIpv4Address: href
                maxLspsPerPcInitiate: href
                keepaliveInterval: href
                deadInterval: href
                pcReplyLspsPerPcc: number
                pceInitiatedLspsPerPcc: number
                srPceCapability: href
                authentication: href
                mD5Key: href
                rateControl: href
                burstInterval: href
                maxInitiatedLspPerInterval: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPccGroupEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pce","pccGroup"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPccGroupEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPccGroupEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPccGroupEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPceEmulation(IxnEmulationHost):
    """Generated NGPF pce emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pce emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                maxUnknownMessage: href
                maxUnknownRequest: href
                maxPendingConnection: href
                tcpPort: href
                pceActionMode: enum
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPceEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pce"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPceEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPceInitiateLSPParametersEmulation(IxnEmulationHost):
    """Generated NGPF pceInitiateLSPParameters emulation host """

    STATE_ADVERTISED = 'advertised'
    STATE_DELEGATEDACTIVE = 'delegatedActive'
    STATE_DELEGATEDDOWN = 'delegatedDown'
    STATE_DELEGATEDGOINGUP = 'delegatedGoingUp'
    STATE_DELEGATEDUP = 'delegatedUp'
    STATE_INIT = 'init'
    STATE_NONE = 'none'
    STATE_NOTDELEGATEDACTIVE = 'notDelegatedActive'
    STATE_NOTDELEGATEDDOWN = 'notDelegatedDown'
    STATE_NOTDELEGATEDGOINGUP = 'notDelegatedGoingUp'
    STATE_NOTDELEGATEDUP = 'notDelegatedUp'
    STATE_PCERRORRECEIVED = 'pcErrorReceived'
    STATE_REMOVEDBYPCC = 'removedByPCC'
    STATE_REMOVEDBYPCE = 'removedByPCE'
    STATE_RETURNDELEGATION = 'returnDelegation'

    def __init__(self, ixnhttp):
        super(IxnPceInitiateLSPParametersEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pceInitiateLSPParameters emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                pathSetupType: href
                includeEndPoints: href
                includeSrp: href
                includeLsp: href
                includeEro: href
                includeMetric: href
                includeBandwidth: href
                includeLspa: href
                ipVersion: href
                srcEndPointIpv4: href
                destEndPointIpv4: href
                srcEndPointIpv6: href
                destEndPointIpv6: href
                overrideSrpIdNumber: bool
                srpIdNumber: href
                overridePlspId: bool
                plspId: href
                includeSymbolicPathNameTlv: href
                symbolicPathName: href
                numberOfEroSubObjects: number
                numberOfMetricSubObject: number
                bandwidth: href
                setupPriority: href
                holdingPriority: href
                localProtection: href
                includeAny: href
                includeAll: href
                excludeAny: href
                includeAssociation: href
                associationId: href
                protectionLsp: href
                standbyMode: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPceInitiateLSPParametersEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pce","pccGroup","pceInitiateLSPParameters"], vport_name, emulation_host, filters)

    def returndelegation(self, expected_state=None, timeout=None):
        """Return Delegation of PCE-Initiated LSPs
            For expected_state options see the class state variables
        """
        super(IxnPceInitiateLSPParametersEmulation, self).call_operation('returnDelegation', expected_state, timeout)

    def takecontrol(self, expected_state=None, timeout=None):
        """Take Control of PCE-Initiated LSPs
            For expected_state options see the class state variables
        """
        super(IxnPceInitiateLSPParametersEmulation, self).call_operation('takeControl', expected_state, timeout)


class IxnPcepBackupPCEsEmulation(IxnEmulationHost):
    """Generated NGPF pcepBackupPCEs emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPcepBackupPCEsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pcepBackupPCEs emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                pceIpv4Address: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPcepBackupPCEsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcepBackupPCEs"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPcepBackupPCEsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPcepBackupPCEsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPcepBackupPCEsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPcepEroSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF pcepEroSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnPcepEroSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pcepEroSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                looseHop: href
                subObjectType: href
                prefixLength: href
                ipv4Prefix: href
                ipv6Prefix: href
                asNumber: href
                sidType: href
                sid: href
                mplsLabel: href
                tc: href
                bos: href
                ttl: href
                naiType: href
                fBit: href
                ipv4NodeId: href
                ipv6NodeId: href
                localIpv4Address: href
                remoteIpv4Address: href
                localIpv6Address: href
                remoteIpv6Address: href
                localNodeId: href
                localInterfaceId: href
                remoteNodeId: href
                remoteInterfaceId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPcepEroSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcc","preEstablishedSrLsps","pcepEroSubObjectsList"], vport_name, emulation_host, filters)


class IxnPcepIroSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF pcepIroSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnPcepIroSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pcepIroSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                subObjectType: href
                prefixLength: href
                ipv4Address: href
                ipv6Address: href
                routerId: href
                interfaceId: href
                asNumber: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPcepIroSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcc","requestedLsps","pcepIroSubObjectsList"], vport_name, emulation_host, filters)


class IxnPcepMetricSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF pcepMetricSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnPcepMetricSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pcepMetricSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                pFlagMetric: href
                metricType: href
                metricValue: href
                enableCflag: href
                enableBflag: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPcepMetricSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcc","requestedLsps","pcepMetricSubObjectsList"], vport_name, emulation_host, filters)


class IxnPimRouterEmulation(IxnEmulationHost):
    """Generated NGPF pimRouter emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPimRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                localRouterId: list
                drPriority: href
                joinPruneInterval: href
                joinPruneHoldTime: href
                active: href
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPimRouterEmulation, self).find(["topology","deviceGroup","pimRouter"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPimRouterEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate Router
            For expected_state options see the class state variables
        """
        super(IxnPimRouterEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Router
            For expected_state options see the class state variables
        """
        super(IxnPimRouterEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPimV4CandidateRPsListEmulation(IxnEmulationHost):
    """Generated NGPF pimV4CandidateRPsList emulation host """

    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_STARTED = 'started'

    def __init__(self, ixnhttp):
        super(IxnPimV4CandidateRPsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV4CandidateRPsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                groupAddress: href
                groupMaskLen: href
                crpAddress: href
                localRouterId: list
                groupCount: href
                meshingType: href
                crpAddressCount: href
                periodicAdvertisementInterval: href
                advertisementHoldTime: href
                backOffInterval: href
                triggeredCrpMessageCount: href
                priority: href
                priorityType: href
                priorityChangeInterval: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV4CandidateRPsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","pimV4Interface","pimV4CandidateRPsList"], vport_name, emulation_host, filters)

    def start(self, expected_state=None, timeout=None):
        """Activate Candidate RP
            For expected_state options see the class state variables
        """
        super(IxnPimV4CandidateRPsListEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Candidate RP
            For expected_state options see the class state variables
        """
        super(IxnPimV4CandidateRPsListEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPimV4InterfaceEmulation(IxnEmulationHost):
    """Generated NGPF pimV4Interface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPimV4InterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV4Interface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                v4Neighbor: href
                bootstrapHashMaskLength: href
                localRouterId: list
                helloInterval: href
                helloHoldTime: href
                disableTriggered: href
                triggeredHelloDelay: href
                autoPickNeighbor: href
                joinPrunes: number
                sources: number
                crpRanges: number
                discardLearnedRpInfo: href
                learnSelectedRpSet: href
                enableBootstrap: href
                enableBfdRegistration: href
                enablePrune: href
                pruneDelay: href
                overrideInterval: href
                lanPruneTbit: href
                sendGenerationIdOption: href
                sendGenerationMode: href
                sendBidirectional: href
                bootstrapPriority: href
                bootstrapInterval: href
                bootstrapTimeout: href
                forceSemantic: href
                supportUnicastBsm: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPimV4InterfaceEmulation, self).find(["topology","deviceGroup","ipv4Loopback","pimV4Interface"], vport_name, emulation_host, filters)

    def clearlearnedinfo(self, expected_state=None, timeout=None):
        """Clear Learned Info
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('clearLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def incrementgenid(self, expected_state=None, timeout=None):
        """Increment GenID
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('incrementGenID', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumebsm(self, expected_state=None, timeout=None):
        """Resume Bootstrap
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('resumeBSM', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume Hello
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('resumeHello', expected_state, timeout)

    def sendbsm(self, expected_state=None, timeout=None):
        """Stop Bootstrap
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('sendBSM', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate Interface
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Interface
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('stop', expected_state, timeout)

    def stopbsm(self, expected_state=None, timeout=None):
        """Stop Bootstrap
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('stopBSM', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop Hello
            For expected_state options see the class state variables
        """
        super(IxnPimV4InterfaceEmulation, self).call_operation('stopHello', expected_state, timeout)


class IxnPimV4JoinPruneListEmulation(IxnEmulationHost):
    """Generated NGPF pimV4JoinPruneList emulation host """

    STATE_JOIN = 'join'
    STATE_LEAVE = 'leave'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'

    def __init__(self, ixnhttp):
        super(IxnPimV4JoinPruneListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV4JoinPruneList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rpV4Address: href
                groupV4Address: href
                groupV4MaskWidth: href
                sourceV4Address: href
                sourceV4MaskWidth: href
                pruneSourceV4Address: href
                pruneSourceV4MaskWidth: href
                localRouterId: list
                rangeType: href
                sourceGroupMappingType: href
                groupAddressCount: href
                sourceAddressCount: href
                pruneSourceAddressCount: href
                registerStopTriggerCount: href
                enablePack: href
                switchOverInterval: href
                enableFlapInfo: href
                flapInterval: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV4JoinPruneListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","pimV4Interface","pimV4JoinPruneList"], vport_name, emulation_host, filters)

    def join(self, expected_state=None, timeout=None):
        """Join
            For expected_state options see the class state variables
        """
        super(IxnPimV4JoinPruneListEmulation, self).call_operation('join', expected_state, timeout)

    def leave(self, expected_state=None, timeout=None):
        """Leave
            For expected_state options see the class state variables
        """
        super(IxnPimV4JoinPruneListEmulation, self).call_operation('leave', expected_state, timeout)

    def resumeperiodicjoin(self, expected_state=None, timeout=None):
        """Resume Periodic Join
            For expected_state options see the class state variables
        """
        super(IxnPimV4JoinPruneListEmulation, self).call_operation('resumePeriodicJoin', expected_state, timeout)

    def stopperiodicjoin(self, expected_state=None, timeout=None):
        """Stop Periodic Join
            For expected_state options see the class state variables
        """
        super(IxnPimV4JoinPruneListEmulation, self).call_operation('stopPeriodicJoin', expected_state, timeout)


class IxnPimV4SourcesListEmulation(IxnEmulationHost):
    """Generated NGPF pimV4SourcesList emulation host """

    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_STARTED = 'started'

    def __init__(self, ixnhttp):
        super(IxnPimV4SourcesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV4SourcesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                groupAddress: href
                sourceAddress: href
                rpAddress: href
                localRouterId: list
                groupCount: href
                sourceCount: href
                discardSgJoinStates: href
                sendNullRegAtBegin: href
                multicastDataLength: href
                txIterationGap: href
                udpSourcePort: href
                udpDestinationPort: href
                switchOverInterval: href
                supressionTime: href
                registerProbeTime: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV4SourcesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","pimV4Interface","pimV4SourcesList"], vport_name, emulation_host, filters)

    def start(self, expected_state=None, timeout=None):
        """Activate Source
            For expected_state options see the class state variables
        """
        super(IxnPimV4SourcesListEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Source
            For expected_state options see the class state variables
        """
        super(IxnPimV4SourcesListEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPimV6CandidateRPsListEmulation(IxnEmulationHost):
    """Generated NGPF pimV6CandidateRPsList emulation host """

    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_STARTED = 'started'

    def __init__(self, ixnhttp):
        super(IxnPimV6CandidateRPsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV6CandidateRPsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                groupAddress: href
                groupMaskLen: href
                crpAddress: href
                localRouterId: list
                groupCount: href
                meshingType: href
                crpAddressCount: href
                periodicAdvertisementInterval: href
                advertisementHoldTime: href
                backOffInterval: href
                triggeredCrpMessageCount: href
                priority: href
                priorityType: href
                priorityChangeInterval: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV6CandidateRPsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","pimV6Interface","pimV6CandidateRPsList"], vport_name, emulation_host, filters)

    def start(self, expected_state=None, timeout=None):
        """Activate Candidate RP
            For expected_state options see the class state variables
        """
        super(IxnPimV6CandidateRPsListEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Candidate RP
            For expected_state options see the class state variables
        """
        super(IxnPimV6CandidateRPsListEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPimV6InterfaceEmulation(IxnEmulationHost):
    """Generated NGPF pimV6Interface emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPimV6InterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV6Interface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                neighborV6Address: href
                bootstrapHashMaskLength: href
                localRouterId: list
                helloInterval: href
                helloHoldTime: href
                disableTriggered: href
                triggeredHelloDelay: href
                autoPickNeighbor: href
                joinPrunes: number
                sources: number
                crpRanges: number
                discardLearnedRpInfo: href
                learnSelectedRpSet: href
                enableBootstrap: href
                enableBfdRegistration: href
                enablePrune: href
                pruneDelay: href
                overrideInterval: href
                lanPruneTbit: href
                sendGenerationIdOption: href
                sendGenerationMode: href
                sendBidirectional: href
                bootstrapPriority: href
                bootstrapInterval: href
                bootstrapTimeout: href
                forceSemantic: href
                supportUnicastBsm: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPimV6InterfaceEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","pimV6Interface"], vport_name, emulation_host, filters)

    def clearlearnedinfo(self, expected_state=None, timeout=None):
        """Clear Learned Info
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('clearLearnedInfo', expected_state, timeout)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def incrementgenid(self, expected_state=None, timeout=None):
        """Increment GenID
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('incrementGenID', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('restartDown', expected_state, timeout)

    def resumebsm(self, expected_state=None, timeout=None):
        """Resume Bootstrap
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('resumeBSM', expected_state, timeout)

    def resumehello(self, expected_state=None, timeout=None):
        """Resume Hello
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('resumeHello', expected_state, timeout)

    def sendbsm(self, expected_state=None, timeout=None):
        """Stop Bootstrap
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('sendBSM', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate Interface
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Interface
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('stop', expected_state, timeout)

    def stopbsm(self, expected_state=None, timeout=None):
        """Stop Bootstrap
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('stopBSM', expected_state, timeout)

    def stophello(self, expected_state=None, timeout=None):
        """Stop Hello
            For expected_state options see the class state variables
        """
        super(IxnPimV6InterfaceEmulation, self).call_operation('stopHello', expected_state, timeout)


class IxnPimV6JoinPruneListEmulation(IxnEmulationHost):
    """Generated NGPF pimV6JoinPruneList emulation host """

    STATE_JOIN = 'join'
    STATE_LEAVE = 'leave'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'

    def __init__(self, ixnhttp):
        super(IxnPimV6JoinPruneListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV6JoinPruneList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rpV6Address: href
                groupV6Address: href
                groupV6MaskWidth: href
                sourceV6Address: href
                sourceV6MaskWidth: href
                pruneSourceV6Address: href
                pruneSourceV6MaskWidth: href
                localRouterId: list
                rangeType: href
                sourceGroupMappingType: href
                groupAddressCount: href
                sourceAddressCount: href
                pruneSourceAddressCount: href
                registerStopTriggerCount: href
                enablePack: href
                switchOverInterval: href
                enableFlapInfo: href
                flapInterval: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV6JoinPruneListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","pimV6Interface","pimV6JoinPruneList"], vport_name, emulation_host, filters)

    def join(self, expected_state=None, timeout=None):
        """Join
            For expected_state options see the class state variables
        """
        super(IxnPimV6JoinPruneListEmulation, self).call_operation('join', expected_state, timeout)

    def leave(self, expected_state=None, timeout=None):
        """Leave
            For expected_state options see the class state variables
        """
        super(IxnPimV6JoinPruneListEmulation, self).call_operation('leave', expected_state, timeout)

    def resumeperiodicjoin(self, expected_state=None, timeout=None):
        """Resume Periodic Join
            For expected_state options see the class state variables
        """
        super(IxnPimV6JoinPruneListEmulation, self).call_operation('resumePeriodicJoin', expected_state, timeout)

    def stopperiodicjoin(self, expected_state=None, timeout=None):
        """Stop Periodic Join
            For expected_state options see the class state variables
        """
        super(IxnPimV6JoinPruneListEmulation, self).call_operation('stopPeriodicJoin', expected_state, timeout)


class IxnPimV6SourcesListEmulation(IxnEmulationHost):
    """Generated NGPF pimV6SourcesList emulation host """

    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_STARTED = 'started'

    def __init__(self, ixnhttp):
        super(IxnPimV6SourcesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pimV6SourcesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                groupAddress: href
                sourceAddress: href
                rpAddress: href
                localRouterId: list
                groupCount: href
                sourceCount: href
                discardSgJoinStates: href
                sendNullRegAtBegin: href
                multicastDataLength: href
                txIterationGap: href
                udpSourcePort: href
                udpDestinationPort: href
                switchOverInterval: href
                supressionTime: href
                registerProbeTime: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV6SourcesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","pimV6Interface","pimV6SourcesList"], vport_name, emulation_host, filters)

    def start(self, expected_state=None, timeout=None):
        """Activate Source
            For expected_state options see the class state variables
        """
        super(IxnPimV6SourcesListEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate Source
            For expected_state options see the class state variables
        """
        super(IxnPimV6SourcesListEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPktInMasterEmulation(IxnEmulationHost):
    """Generated NGPF pktInMaster emulation host """


    def __init__(self, ixnhttp):
        super(IxnPktInMasterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pktInMaster emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnPktInMasterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","asyncConfStatLearnedInfo","pktInMaster"], vport_name, emulation_host, filters)


class IxnPktInSlaveEmulation(IxnEmulationHost):
    """Generated NGPF pktInSlave emulation host """


    def __init__(self, ixnhttp):
        super(IxnPktInSlaveEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pktInSlave emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnPktInSlaveEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","asyncConfStatLearnedInfo","pktInSlave"], vport_name, emulation_host, filters)


class IxnPnTLVListEmulation(IxnEmulationHost):
    """Generated NGPF pnTLVList emulation host """


    def __init__(self, ixnhttp):
        super(IxnPnTLVListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pnTLVList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                type: href
                tlvLength: href
                value: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPnTLVListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6Autoconfiguration","bgpIpv6Peer","bgpIPv6EvpnEvi","broadcastDomainV6","pnTLVList"], vport_name, emulation_host, filters)


class IxnPortNumberEmulation(IxnEmulationHost):
    """Generated NGPF portNumber emulation host """


    def __init__(self, ixnhttp):
        super(IxnPortNumberEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific portNumber emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnPortNumberEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","portNumber"], vport_name, emulation_host, filters)


class IxnPortStatusMasterEmulation(IxnEmulationHost):
    """Generated NGPF portStatusMaster emulation host """


    def __init__(self, ixnhttp):
        super(IxnPortStatusMasterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific portStatusMaster emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnPortStatusMasterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","asyncConfStatLearnedInfo","portStatusMaster"], vport_name, emulation_host, filters)


class IxnPortStatusSlaveEmulation(IxnEmulationHost):
    """Generated NGPF portStatusSlave emulation host """


    def __init__(self, ixnhttp):
        super(IxnPortStatusSlaveEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific portStatusSlave emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnPortStatusSlaveEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","asyncConfStatLearnedInfo","portStatusSlave"], vport_name, emulation_host, filters)


class IxnPppoxServerSessionsEmulation(IxnEmulationHost):
    """Generated NGPF pppoxServerSessions emulation host """

    STATE_CLS_CFG_REJ_AUTH = 'cLS_CFG_REJ_AUTH'
    STATE_CLS_CHAP_PEER_DET_FAIL = 'cLS_CHAP_PEER_DET_FAIL'
    STATE_CLS_CHAP_PEER_RESP_BAD = 'cLS_CHAP_PEER_RESP_BAD'
    STATE_CLS_CODE_REJ_IPCP = 'cLS_CODE_REJ_IPCP'
    STATE_CLS_CODE_REJ_IPV6CP = 'cLS_CODE_REJ_IPV6CP'
    STATE_CLS_CODE_REJ_LCP = 'cLS_CODE_REJ_LCP'
    STATE_CLS_ERR_PPP_NO_BUF = 'cLS_ERR_PPP_NO_BUF'
    STATE_CLS_ERR_PPP_SEND_PKT = 'cLS_ERR_PPP_SEND_PKT'
    STATE_CLS_LINK_DISABLE = 'cLS_LINK_DISABLE'
    STATE_CLS_LOC_IPADDR_BROADCAST = 'cLS_LOC_IPADDR_BROADCAST'
    STATE_CLS_LOC_IPADDR_CLASS_E = 'cLS_LOC_IPADDR_CLASS_E'
    STATE_CLS_LOC_IPADDR_INVAL_ACKS_0 = 'cLS_LOC_IPADDR_INVAL_ACKS_0'
    STATE_CLS_LOC_IPADDR_INVAL_ACKS_DIFF = 'cLS_LOC_IPADDR_INVAL_ACKS_DIFF'
    STATE_CLS_LOC_IPADDR_LOOPBACK = 'cLS_LOC_IPADDR_LOOPBACK'
    STATE_CLS_LOC_IPADDR_PEER_MATCH_LOC = 'cLS_LOC_IPADDR_PEER_MATCH_LOC'
    STATE_CLS_LOC_IPADDR_PEER_NO_GIVE = 'cLS_LOC_IPADDR_PEER_NO_GIVE'
    STATE_CLS_LOC_IPADDR_PEER_NO_HELP = 'cLS_LOC_IPADDR_PEER_NO_HELP'
    STATE_CLS_LOC_IPADDR_PEER_NO_TAKE = 'cLS_LOC_IPADDR_PEER_NO_TAKE'
    STATE_CLS_LOC_IPADDR_PEER_REJ = 'cLS_LOC_IPADDR_PEER_REJ'
    STATE_CLS_LOOPBACK_DETECT = 'cLS_LOOPBACK_DETECT'
    STATE_CLS_NO_NCP = 'cLS_NO_NCP'
    STATE_CLS_NONE = 'cLS_NONE'
    STATE_CLS_PAP_BAD_PASSWD = 'cLS_PAP_BAD_PASSWD'
    STATE_CLS_PEER_DISCONNECTED = 'cLS_PEER_DISCONNECTED'
    STATE_CLS_PEER_IPADDR_MATCH_LOC = 'cLS_PEER_IPADDR_MATCH_LOC'
    STATE_CLS_PEER_IPADDR_PEER_NO_SET = 'cLS_PEER_IPADDR_PEER_NO_SET'
    STATE_CLS_PPOE_AC_SYSTEM_ERROR = 'cLS_PPOE_AC_SYSTEM_ERROR'
    STATE_CLS_PPOE_GENERIC_ERROR = 'cLS_PPOE_GENERIC_ERROR'
    STATE_CLS_PPP_DISABLE = 'cLS_PPP_DISABLE'
    STATE_CLS_PPPOE_PADI_TIMEOUT = 'cLS_PPPOE_PADI_TIMEOUT'
    STATE_CLS_PPPOE_PADO_TIMEOUT = 'cLS_PPPOE_PADO_TIMEOUT'
    STATE_CLS_PPPOE_PADR_TIMEOUT = 'cLS_PPPOE_PADR_TIMEOUT'
    STATE_CLS_PROTO_REJ_IPCP = 'cLS_PROTO_REJ_IPCP'
    STATE_CLS_PROTO_REJ_IPV6CP = 'cLS_PROTO_REJ_IPv6CP'
    STATE_CLS_TIMEOUT_CHAP_CHAL = 'cLS_TIMEOUT_CHAP_CHAL'
    STATE_CLS_TIMEOUT_CHAP_RESP = 'cLS_TIMEOUT_CHAP_RESP'
    STATE_CLS_TIMEOUT_IPCP_CFG_REQ = 'cLS_TIMEOUT_IPCP_CFG_REQ'
    STATE_CLS_TIMEOUT_IPV6CP_CFG_REQ = 'cLS_TIMEOUT_IPV6CP_CFG_REQ'
    STATE_CLS_TIMEOUT_IPV6CP_RA = 'cLS_TIMEOUT_IPV6CP_RA'
    STATE_CLS_TIMEOUT_LCP_CFG_REQ = 'cLS_TIMEOUT_LCP_CFG_REQ'
    STATE_CLS_TIMEOUT_LCP_ECHO_REQ = 'cLS_TIMEOUT_LCP_ECHO_REQ'
    STATE_CLS_TIMEOUT_PAP_AUTH_REQ = 'cLS_TIMEOUT_PAP_AUTH_REQ'

    def __init__(self, ixnhttp):
        super(IxnPppoxServerSessionsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pppoxServerSessions emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                serverIpv4Addresses: list
                serverIpv6Addresses: list
                discoveredSessionIds: list
                discoveredTunnelIds: list
                discoveredClientsMacs: list
                discoveredRemoteSessionIds: list
                discoveredRemoteTunnelIds: list
                discoveredTunnelIPs: list
                papUser: href
                papPassword: href
                chapName: href
                chapSecret: href
                enableDomainGroups: href
                domainList: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPppoxServerSessionsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pppoxServerSessions"], vport_name, emulation_host, filters)

    def closeipcp(self, expected_state=None, timeout=None):
        """Close IPCP for selected PPPoX Server Sessions items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxServerSessionsEmulation, self).call_operation('closeIpcp', expected_state, timeout)

    def closeipv6cp(self, expected_state=None, timeout=None):
        """Close IPv6CP for selected PPPoX Severs Sessions items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxServerSessionsEmulation, self).call_operation('closeIpv6cp', expected_state, timeout)


class IxnPppoxclientEmulation(IxnEmulationHost):
    """Generated NGPF pppoxclient emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPppoxclientEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pppoxclient emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                pppoxClientGlobalAndPortData: href
                discoveredIpv4Addresses: list
                discoveredIpv6Addresses: list
                discoveredSessionIds: list
                discoveredTunnelIds: list
                discoveredMacs: list
                discoveredRemoteSessionIds: list
                discoveredRemoteTunnelIds: list
                discoveredTunnelIPs: list
                papUser: href
                papPassword: href
                chapName: href
                chapSecret: href
                enableDomainGroups: href
                domainList: href
                clientNcpOptions: href
                clientLocalIp: href
                clientV6NcpOptions: href
                clientLocalIpv6Iid: href
                clientDnsOptions: href
                clientPrimaryDnsAddress: href
                clientSecondaryDnsAddress: href
                clientNetmaskOptions: href
                clientNetmask: href
                clientWinsOptions: href
                clientWinsPrimaryAddress: href
                clientWinsSecondaryAddress: href
                padiTimeout: href
                padiRetries: href
                padrTimeout: href
                padrRetries: href
                serviceName: href
                serviceOptions: href
                acOptions: href
                acMatchName: href
                acMatchMac: href
                enableRedial: href
                redialTimeout: href
                unlimitedRedialAttempts: href
                redialMax: href
                enableMaxPayload: href
                maxPayload: href
                enableHostUniq: href
                hostUniqLength: href
                hostUniq: href
                clientSignalLoopId: href
                agentCircuitId: href
                agentRemoteId: href
                clientSignalLoopChar: href
                actualRateUpstream: href
                actualRateDownstream: href
                clientSignalIWF: href
                clientSignalLoopEncapsulation: href
                dataLink: href
                encaps1: href
                encaps2: href
                dslTypeTlv: href
                userDefinedDslType: href
                mruNegotiation: href
                mtu: href
                enableEchoRsp: href
                enableEchoReq: href
                echoReqInterval: href
                lcpTimeout: href
                lcpRetries: href
                lcpTermRetries: href
                lcpEnableAccm: href
                lcpAccm: href
                lcpMaxFailure: href
                lcpStartDelay: href
                ncpType: href
                ncpTimeout: href
                ncpRetries: href
                authType: href
                authTimeout: href
                authRetries: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPppoxclientEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","pppoxclient"], vport_name, emulation_host, filters)

    def closeipcp(self, expected_state=None, timeout=None):
        """Close IPCP for selected PPPoX items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('closeIpcp', expected_state, timeout)

    def closeipv6cp(self, expected_state=None, timeout=None):
        """Close IPv6CP for selected PPPoX items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('closeIpv6cp', expected_state, timeout)

    def openipcp(self, expected_state=None, timeout=None):
        """Open IPCP for selected PPPoX items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('openIpcp', expected_state, timeout)

    def openipv6cp(self, expected_state=None, timeout=None):
        """Open IPv6CP for selected PPPoX items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('openIpv6cp', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('restartDown', expected_state, timeout)

    def sendping(self, expected_state=None, timeout=None):
        """Send Ping IPv4 for selected PPPoX items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('sendPing', expected_state, timeout)

    def sendping6(self, expected_state=None, timeout=None):
        """Send Ping IPv6 for selected PPPoX items.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('sendPing6', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPppoxclientEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPppoxserverEmulation(IxnEmulationHost):
    """Generated NGPF pppoxserver emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPppoxserverEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific pppoxserver emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                pppoxServerGlobalAndPortData: href
                sessionsCount: number
                serverNcpOptions: href
                clientBaseIp: href
                clientIpIncr: href
                serverBaseIp: href
                serverIpIncr: href
                serverV6NcpOptions: href
                clientIID: href
                clientIIDIncr: href
                serverIID: href
                serverIIDIncr: href
                ipv6PoolPrefix: href
                ipv6PoolPrefixLen: href
                ipv6AddrPrefixLen: href
                enableDnsRa: href
                dnsServerList: href
                acceptAnyAuthValue: href
                serverDnsOptions: href
                serverPrimaryDnsAddress: href
                serverSecondaryDnsAddress: href
                serverNetmaskOptions: href
                serverNetmask: href
                serverWinsOptions: href
                serverWinsPrimaryAddress: href
                serverWinsSecondaryAddress: href
                serviceName: href
                acName: href
                enableMaxPayload: href
                serverSignalLoopId: href
                serverSignalLoopChar: href
                serverSignalIWF: href
                serverSignalLoopEncapsulation: href
                serverSignalDslTypeTlv: href
                mruNegotiation: href
                mtu: href
                enableEchoRsp: href
                enableEchoReq: href
                echoReqInterval: href
                lcpTimeout: href
                lcpRetries: href
                lcpTermRetries: href
                lcpEnableAccm: href
                lcpAccm: href
                lcpMaxFailure: href
                lcpStartDelay: href
                ncpType: href
                ncpTimeout: href
                ncpRetries: href
                authType: href
                authTimeout: href
                authRetries: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPppoxserverEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPppoxserverEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPppoxserverEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPppoxserverEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPreEstablishedSrLspsEmulation(IxnEmulationHost):
    """Generated NGPF preEstablishedSrLsps emulation host """

    STATE_EXPIRED = 'expired'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_RUNNING = 'running'
    STATE_STOPPED = 'stopped'

    def __init__(self, ixnhttp):
        super(IxnPreEstablishedSrLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific preEstablishedSrLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                includeSrp: href
                includeLsp: href
                includeEro: href
                includeMetric: href
                includeBandwidth: href
                includeLspa: href
                initialDelegation: href
                overridePlspId: bool
                plspId: href
                includeSymbolicPathNameTlv: href
                symbolicPathName: href
                redelegationTimeoutInterval: href
                numberOfEroSubObjects: number
                numberOfMetricSubObject: number
                bandwidth: href
                setupPriority: href
                holdingPriority: href
                localProtection: href
                includeAny: href
                includeAll: href
                excludeAny: href
                includePpag: href
                destEndPointIpv4: href
                associationId: href
                protectionLspBit: href
                standbyLspBit: href
                includeEro: href
                srcEndPointIpv4: href
                srcEndPointIpv6: href
                insertIpv6ExplicitNull: bool
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPreEstablishedSrLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcc","preEstablishedSrLsps"], vport_name, emulation_host, filters)


class IxnPropertyRateEmulation(IxnEmulationHost):
    """Generated NGPF propertyRate emulation host """


    def __init__(self, ixnhttp):
        super(IxnPropertyRateEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific propertyRate emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnPropertyRateEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","propertyRate"], vport_name, emulation_host, filters)


class IxnPtpEmulation(IxnEmulationHost):
    """Generated NGPF ptp emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnPtpEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ptp emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                masterClockId: list
                role: href
                customClockId: href
                clockIdentity: href
                profile: href
                oneWay: href
                delayMechanism: href
                communicationMode: href
                stepMode: href
                domain: href
                portNumber: href
                announceReceiptTimeout: href
                logAnnounceInterval: href
                logSyncInterval: href
                logDelayReqInterval: href
                strictGrant: href
                pathTraceTLV: href
                priority1: href
                clockClass: href
                clockAccuracy: href
                offsetScaledLogVariance: href
                priority2: href
                timeSource: href
                signalUnicastHandling: href
                masterMacAddress: href
                masterMacIncrementBy: href
                masterIpAddress: href
                masterIpIncrementBy: href
                masterIpv6Address: href
                masterIpv6IncrementBy: href
                masterCount: href
                slaveMacAddress: href
                slaveMacIncrementBy: href
                slaveIpAddress: href
                slaveIpIncrementBy: href
                slaveIpv6Address: href
                slaveIpv6IncrementBy: href
                slaveCount: href
                handleCancelTlv: href
                handleAnnounceTlv: href
                sendMulticastAnnounce: href
                renewalInvited: href
                learnPortId: href
                signalInterval: href
                grantUnicastDurationInterval: href
                grantSyncDurationInterval: href
                grantDelayRespDurationInterval: href
                requestInterval: href
                requestAttempts: href
                requestHolddown: href
                syncReceiptTimeout: href
                delayRespReceiptTimeout: href
                multicastAddress: href
                notSlave: href
                dropMalformed: href
                syncReceiptTimeoutgPTP: href
                bmca: href
                reverseSync: href
                reverseSyncIntervalPercent: href
                cumulativeScaledRateOffset: href
                gmTimeBaseIndicator: href
                lastGmPhaseChange: href
                scaledLastGmFreqChange: href
                updateTime: href
                timestampOffset: href
                nanosecondsPerSecond: href
                txCalibration: href
                txTwoStepCalibration: href
                rxCalibration: href
                alternateMasterFlag: href
                announceTimeTraceable: href
                announceFrequencyTraceable: href
                announceLeap59: href
                announceLeap61: href
                announceCurrentUtcOffsetValid: href
                currentUtcOffset: href
                announcePtpTimescale: href
                simulateBoundary: href
                grandmasterIdentity: href
                stepsRemoved: href
                simulateTransparent: href
                syncResidenceTime: href
                followUpResidenceTime: href
                delayReqResidenceTime: href
                delayRespResidenceTime: href
                pDelayFollowUpResidenceTime: href
                announceDropRate: href
                syncDropRate: href
                followUpDelay: href
                followUpDelayInsertionRate: href
                followUpDropRate: href
                followUpBadCrcRate: href
                delayReqDropRate: href
                delayReqOffset: href
                delayReqSpread: href
                delayResponseDelay: href
                delayResponseDelayInsertionRate: href
                delayRespDropRate: href
                pDelayFollowUpDelay: href
                pDelayFollowUpDelayInsertionRate: href
                pDelayFollowUpDropRate: href
                dropSignalReqAnnounce: href
                dropSignalReqSync: href
                dropSignalReqDelayResp: href
                enableNegativeTesting: bool
                frequency: number
                numberOFMsgs: number
                avnuMode: enum
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnPtpEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ptp"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnPtpEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPtpEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnPtpEmulation, self).call_operation('stop', expected_state, timeout)


class IxnPtpNegBehaveListEmulation(IxnEmulationHost):
    """Generated NGPF ptpNegBehaveList emulation host """


    def __init__(self, ixnhttp):
        super(IxnPtpNegBehaveListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific ptpNegBehaveList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                mvActive: href
                ptpMsgType: href
                mvMsgAction: href
                mvDelay: href
                mvPtpMsgField: href
                mvFieldValue: href
                ptpValueDisPattern: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPtpNegBehaveListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ptp","ptpNegBehaveList"], vport_name, emulation_host, filters)


class IxnQueueConfigLearnedInfoEmulation(IxnEmulationHost):
    """Generated NGPF queueConfigLearnedInfo emulation host """


    def __init__(self, ixnhttp):
        super(IxnQueueConfigLearnedInfoEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific queueConfigLearnedInfo emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnQueueConfigLearnedInfoEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo"], vport_name, emulation_host, filters)


class IxnQueueIDEmulation(IxnEmulationHost):
    """Generated NGPF queueID emulation host """


    def __init__(self, ixnhttp):
        super(IxnQueueIDEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific queueID emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnQueueIDEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","queueID"], vport_name, emulation_host, filters)


class IxnQueuePortNumberEmulation(IxnEmulationHost):
    """Generated NGPF queuePortNumber emulation host """


    def __init__(self, ixnhttp):
        super(IxnQueuePortNumberEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific queuePortNumber emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnQueuePortNumberEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","queuePortNumber"], vport_name, emulation_host, filters)


class IxnQueuePropertyEmulation(IxnEmulationHost):
    """Generated NGPF queueProperty emulation host """


    def __init__(self, ixnhttp):
        super(IxnQueuePropertyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific queueProperty emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnQueuePropertyEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueConfigLearnedInfo","queueProperty"], vport_name, emulation_host, filters)


class IxnQueueStatLearnedInfoEmulation(IxnEmulationHost):
    """Generated NGPF queueStatLearnedInfo emulation host """


    def __init__(self, ixnhttp):
        super(IxnQueueStatLearnedInfoEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific queueStatLearnedInfo emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnQueueStatLearnedInfoEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","queueStatLearnedInfo"], vport_name, emulation_host, filters)


class IxnRemoteIpBaseEmulation(IxnEmulationHost):
    """Generated NGPF remoteIpBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnRemoteIpBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific remoteIpBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnRemoteIpBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","remoteIpBase"], vport_name, emulation_host, filters)


class IxnReplyStateBaseEmulation(IxnEmulationHost):
    """Generated NGPF replyStateBase emulation host """


    def __init__(self, ixnhttp):
        super(IxnReplyStateBaseEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific replyStateBase emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                count: number
        """
        return super(IxnReplyStateBaseEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","container","replyStateBase"], vport_name, emulation_host, filters)


class IxnRequestedLspsEmulation(IxnEmulationHost):
    """Generated NGPF requestedLsps emulation host """

    STATE_EXPIRED = 'expired'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_RUNNING = 'running'
    STATE_STOPPED = 'stopped'

    def __init__(self, ixnhttp):
        super(IxnRequestedLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific requestedLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                includeRp: href
                includeEndPoints: href
                includeLsp: href
                includeLspa: href
                includeBandwidth: href
                includeMetric: href
                includeIro: href
                pFlagRp: href
                overrideRequestId: bool
                requestId: href
                loose: href
                biDirectional: href
                reOptimization: href
                priority: href
                pflagEndpoints: href
                overrideSourceAddress: href
                ipVersion: href
                sourceIpv4Address: href
                destinationIpv4Address: href
                sourceIpv6Address: href
                destinationIpv6Address: href
                initialDelegation: href
                pFlagLsp: href
                overridePlspId: bool
                plspId: href
                includeSymbolicPathNameTlv: href
                symbolicPathName: href
                redelegationTimeoutInterval: href
                pFlagLspa: href
                setupPriority: href
                holdingPriority: href
                localProtection: href
                includeAny: href
                includeAll: href
                excludeAny: href
                pFlagBandwidth: href
                bandwidth: href
                maxNumberOfMetrics: number
                pFlagIro: href
                maxNoOfIroSubObjects: number
                activeDataTrafficEndPoints: href
                sourceIpv4Address: href
                sourceIpv6Address: href
                maxExpectedSegmentCount: number
                insertIpv6ExplicitNull: bool
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRequestedLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","pcc","requestedLsps"], vport_name, emulation_host, filters)


class IxnRootRangesEmulation(IxnEmulationHost):
    """Generated NGPF rootRanges emulation host """


    def __init__(self, ixnhttp):
        super(IxnRootRangesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rootRanges emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                rootAddress: href
                rootAddressCount: href
                rootAddressStep: href
                lspCountPerRoot: href
                continuousIncrementOVAcrossRoot: href
                numberOfTLVs: number
                sourceAddressV4: href
                sourceAddressV6: href
                sourceCountPerLSP: href
                filterOnGroupAddress: href
                startGroupAddressV4: href
                startGroupAddressV6: href
                groupCountPerLSP: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRootRangesEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","rootRanges"], vport_name, emulation_host, filters)


class IxnRouterDataEmulation(IxnEmulationHost):
    """Generated NGPF routerData emulation host """


    def __init__(self, ixnhttp):
        super(IxnRouterDataEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific routerData emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                routerId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRouterDataEmulation, self).find(["topology","deviceGroup","routerData"], vport_name, emulation_host, filters)


class IxnRsvpDetourSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF rsvpDetourSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnRsvpDetourSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpDetourSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                plrId: href
                avoidNodeId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpDetourSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2PIngressLsps","rsvpDetourSubObjectsList"], vport_name, emulation_host, filters)


class IxnRsvpEROSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF rsvpEROSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnRsvpEROSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpEROSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                type: href
                ip: href
                prefixLength: href
                asNumber: href
                looseFlag: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpEROSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2PIngressLsps","rsvpEROSubObjectsList"], vport_name, emulation_host, filters)


class IxnRsvpEroSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF rsvpEroSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnRsvpEroSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpEroSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                p2mpIdAsNum: list
                p2mpIdAsIp: list
                leafIp: list
                type: href
                ip: href
                prefixLength: href
                asNumber: href
                looseFlag: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpEroSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2mpIngressLsps","rsvpP2mpIngressSubLsps","rsvpEroSubObjectsList"], vport_name, emulation_host, filters)


class IxnRsvpIngressRROSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF rsvpIngressRROSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnRsvpIngressRROSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpIngressRROSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                type: href
                ip: href
                protectionAvailable: href
                protectionInUse: href
                label: href
                cType: href
                globalLabel: href
                bandwidthProtection: href
                nodeProtection: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpIngressRROSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2PIngressLsps","rsvpIngressRROSubObjectsList"], vport_name, emulation_host, filters)


class IxnRsvpIngressRroSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF rsvpIngressRroSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnRsvpIngressRroSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpIngressRroSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                p2mpIdAsNum: list
                p2mpIdAsIp: list
                type: href
                ip: href
                protectionAvailable: href
                protectionInUse: href
                label: href
                cType: href
                globalLabel: href
                bandwidthProtection: href
                nodeProtection: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpIngressRroSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2mpIngressLsps","rsvpIngressRroSubObjectsList"], vport_name, emulation_host, filters)


class IxnRsvpP2PEgressLspsEmulation(IxnEmulationHost):
    """Generated NGPF rsvpP2PEgressLsps emulation host """

    STATE_DOWN = 'down'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnRsvpP2PEgressLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpP2PEgressLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                refreshInterval: href
                timeoutMultiplier: href
                sendReservationConfirmation: href
                enableFixedLabelForReservations: href
                labelValue: href
                reservationStyle: href
                endPointIpv6: href
                reflectRro: href
                numberOfRroSubObjects: number
                enableReplyingLspPing: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpP2PEgressLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2PEgressLsps"], vport_name, emulation_host, filters)

    def start(self, expected_state=None, timeout=None):
        """Activate/Enable selected Tunnel Tail Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PEgressLspsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate/Disable selected Tunnel Tail Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PEgressLspsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnRsvpP2PIngressLspsEmulation(IxnEmulationHost):
    """Generated NGPF rsvpP2PIngressLsps emulation host """

    STATE_EXPIRED = 'expired'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_RUNNING = 'running'
    STATE_STOPPED = 'stopped'

    def __init__(self, ixnhttp):
        super(IxnRsvpP2PIngressLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpP2PIngressLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                remoteIp: href
                tunnelId: href
                lspId: href
                refreshInterval: href
                timeoutMultiplier: href
                doMBBOnApplyChanges: bool
                delayLspSwitchOver: bool
                lspSwitchOverDelayTime: number
                usingHeadendIp: href
                sourceIp: href
                autorouteTraffic: href
                sourceIpv6: href
                insertIPv6ExplicitNull: href
                autoGenerateSessionName: href
                sessionName: href
                setupPriority: href
                holdingPriority: href
                localProtectionDesired: href
                labelRecordingDesired: href
                seStyleDesired: href
                bandwidthProtectionDesired: href
                nodeProtectionDesired: href
                resourceAffinities: href
                excludeAny: href
                includeAny: href
                includeAll: href
                tokenBucketRate: href
                tokenBucketSize: href
                peakDataRate: href
                minimumPolicedUnit: href
                maximumPacketSize: href
                enableFastReroute: href
                fastRerouteSetupPriority: href
                fastRerouteHoldingPriority: href
                hopLimit: href
                fastRerouteBandwidth: href
                fastRerouteExcludeAny: href
                fastRerouteIncludeAny: href
                fastRerouteIncludeAll: href
                oneToOneBackupDesired: href
                facilityBackupDesired: href
                sendDetour: href
                numberOfDetourSubObjects: number
                backupLspId: href
                enablePathReOptimization: href
                enablePeriodicReEvaluationRequest: href
                reEvaluationRequestInterval: href
                enableEro: href
                prependDutToEro: href
                prefixLength: href
                numberOfEroSubObjects: number
                sendRro: href
                numberOfRroSubObjects: number
                initialDelegation: href
                redelegationTimeoutInterval: href
                lspCount: href
                lspOperativeMode: href
                configureSyncLspObject: href
                enableBfdMpls: href
                enableLspPing: href
                includeAssociation: href
                associationId: href
                protectionLsp: href
                standbyMode: href
                tSpecSameAsPrimary: bool
                backupLspTokenBucketRate: href
                backupLspTokenBucketSize: href
                backupLspPeakDataRate: href
                backupLspMinimumPolicedUnit: href
                backupLspMaximumPacketSize: href
                eroSameAsPrimary: bool
                backupLspEnableEro: href
                backupLspPrependDutToEro: href
                backupLspPrefixLength: href
                backupLspNumberOfEroSubObjects: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpP2PIngressLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2PIngressLsps"], vport_name, emulation_host, filters)

    def initiatepathreoptimization(self, expected_state=None, timeout=None):
        """Send Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PIngressLspsEmulation, self).call_operation('initiatePathReoptimization', expected_state, timeout)

    def makebeforebreak(self, expected_state=None, timeout=None):
        """Initiate Make Before Break for selected Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PIngressLspsEmulation, self).call_operation('makeBeforeBreak', expected_state, timeout)

    def pcepdelegate(self, expected_state=None, timeout=None):
        """Delegate the non-delegated LSPs among the selected RSVP-TE LSPs to PCE.
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PIngressLspsEmulation, self).call_operation('pcepDelegate', expected_state, timeout)

    def pceprevokedelegation(self, expected_state=None, timeout=None):
        """Revoke Delegation from PCE for delegated LSPs among the selected LSPs.
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PIngressLspsEmulation, self).call_operation('pcepRevokeDelegation', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate/Enable Tunnel selected Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PIngressLspsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate/Disable selected Tunnel Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2PIngressLspsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnRsvpP2mpEgressLspsEmulation(IxnEmulationHost):
    """Generated NGPF rsvpP2mpEgressLsps emulation host """

    STATE_DOWN = 'down'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnRsvpP2mpEgressLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpP2mpEgressLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                typeP2mpId: enum
                p2mpIdAsNumber: href
                p2mpIdIp: href
                localIp: list
                refreshInterval: href
                timeoutMultiplier: href
                sendReservationConfirmation: href
                enableFixedLabelForReservations: href
                labelValue: href
                reservationStyle: href
                subLspsDown: href
                destinationIpv4GroupAddress: href
                endPointIpv6: href
                reflectRro: href
                includeLeafIpAtBottom: href
                includeConnectedIpOnTop: href
                sendAsRro: href
                sendAsSrro: href
                numberOfRroSubObjects: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpP2mpEgressLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2mpEgressLsps"], vport_name, emulation_host, filters)

    def graftsublsp(self, expected_state=None, timeout=None):
        """Activate/Enable Tunnel selected SubLsp Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpEgressLspsEmulation, self).call_operation('graftSubLsp', expected_state, timeout)

    def prunesublsp(self, expected_state=None, timeout=None):
        """Deactivate/Disable selected Tunnel SubLsp Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpEgressLspsEmulation, self).call_operation('pruneSubLsp', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate/Enable selected Tunnel Tail Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpEgressLspsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate/Disable selected Tunnel Tail Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpEgressLspsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnRsvpP2mpIngressLspsEmulation(IxnEmulationHost):
    """Generated NGPF rsvpP2mpIngressLsps emulation host """

    STATE_DOWN = 'down'
    STATE_NONE = 'none'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnRsvpP2mpIngressLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpP2mpIngressLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                typeP2mpId: enum
                p2mpIdAsNumber: href
                p2mpIdIp: href
                localIp: list
                tunnelId: href
                lspId: href
                refreshInterval: href
                timeoutMultiplier: href
                ingressP2mpSubLspRanges: number
                delayLspSwitchOver: bool
                lspSwitchOverDelayTime: number
                usingHeadendIp: href
                sourceIpv4: href
                sourceIpv6: href
                insertIPv6ExplicitNull: href
                autoGenerateSessionName: href
                sessionName: href
                setupPriority: href
                holdingPriority: href
                localProtectionDesired: href
                labelRecordingDesired: href
                seStyleDesired: href
                bandwidthProtectionDesired: href
                nodeProtectionDesired: href
                resourceAffinities: href
                excludeAny: href
                includeAny: href
                includeAll: href
                tokenBucketRate: href
                tokenBucketSize: href
                peakDataRate: href
                minimumPolicedUnit: href
                maximumPacketSize: href
                enableFastReroute: href
                fastRerouteSetupPriority: href
                fastRerouteHoldingPriority: href
                hopLimit: href
                fastRerouteBandwidth: href
                fastRerouteExcludeAny: href
                fastRerouteIncludeAny: href
                fastRerouteIncludeAll: href
                oneToOneBackupDesired: href
                facilityBackupDesired: href
                sendDetour: href
                numberOfDetourSubObjects: number
                backupLspId: href
                enablePathReOptimization: href
                enablePeriodicReEvaluationRequest: href
                reEvaluationRequestInterval: href
                sendRro: href
                includeHeadIpAtBottom: href
                includeConnectedIpOnTop: href
                numberOfRroSubObjects: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpP2mpIngressLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2mpIngressLsps"], vport_name, emulation_host, filters)

    def initiatep2mppathreoptimization(self, expected_state=None, timeout=None):
        """Send P2MP Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpIngressLspsEmulation, self).call_operation('initiateP2mpPathReoptimization', expected_state, timeout)

    def p2mpmakebeforebreak(self, expected_state=None, timeout=None):
        """Initiate P2MP Make Before Break for selected Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpIngressLspsEmulation, self).call_operation('p2mpMakeBeforeBreak', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate/Enable P2MP Tunnel selected Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpIngressLspsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate/Disable P2MP selected Tunnel Head Ranges
            For expected_state options see the class state variables
        """
        super(IxnRsvpP2mpIngressLspsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnRsvpP2mpIngressSubLspsEmulation(IxnEmulationHost):
    """Generated NGPF rsvpP2mpIngressSubLsps emulation host """

    STATE_LASTERRLSPADMISSIONCONTROLFAILURE = 'lastErrLSPAdmissionControlFailure'
    STATE_LASTERRLSPBADADSPECVALUE = 'lastErrLSPBadAdSpecValue'
    STATE_LASTERRLSPBADEXPLICITROUTE = 'lastErrLSPBadExplicitRoute'
    STATE_LASTERRLSPBADFLOWSPECVALUE = 'lastErrLSPBadFlowspecValue'
    STATE_LASTERRLSPBADINITIALSUBOBJECT = 'lastErrLSPBadInitialSubobject'
    STATE_LASTERRLSPBADLOOSENODE = 'lastErrLSPBadLooseNode'
    STATE_LASTERRLSPBADSTRICTNODE = 'lastErrLSPBadStrictNode'
    STATE_LASTERRLSPBADTSPECVALUE = 'lastErrLSPBadTSpecValue'
    STATE_LASTERRLSPDELAYBOUNDNOTMET = 'lastErrLSPDelayBoundNotMet'
    STATE_LASTERRLSPMPLSALLOCATIONFAILURE = 'lastErrLSPMPLSAllocationFailure'
    STATE_LASTERRLSPMTUTOOBIG = 'lastErrLSPMTUTooBig'
    STATE_LASTERRLSPNONRSVPROUTER = 'lastErrLSPNonRSVPRouter'
    STATE_LASTERRLSPNOROUTEAVAILABLE = 'lastErrLSPNoRouteAvailable'
    STATE_LASTERRLSPPATHERR = 'lastErrLSPPathErr'
    STATE_LASTERRLSPPATHTEARSENT = 'lastErrLSPPathTearSent'
    STATE_LASTERRLSPREQUESTEDBANDWIDTHUNAVAILABLE = 'lastErrLSPRequestedBandwidthUnavailable'
    STATE_LASTERRLSPRESERVATIONTEARRECEIVED = 'lastErrLSPReservationTearReceived'
    STATE_LASTERRLSPRESERVATIONTEARSENT = 'lastErrLSPReservationTearSent'
    STATE_LASTERRLSPRESERVATIONTIMEOUT = 'lastErrLSPReservationTimeout'
    STATE_LASTERRLSPROUTINGLOOPS = 'lastErrLSPRoutingLoops'
    STATE_LASTERRLSPROUTINGPROBLEM = 'lastErrLSPRoutingProblem'
    STATE_LASTERRLSPRSVPSYSTEMERROR = 'lastErrLSPRSVPSystemError'
    STATE_LASTERRLSPSERVICECONFLICT = 'lastErrLSPServiceConflict'
    STATE_LASTERRLSPSERVICEUNSUPPORTED = 'lastErrLSPServiceUnsupported'
    STATE_LASTERRLSPTRAFFICCONTROLERROR = 'lastErrLSPTrafficControlError'
    STATE_LASTERRLSPTRAFFICCONTROLSYSTEMERROR = 'lastErrLSPTrafficControlSystemError'
    STATE_LASTERRLSPTRAFFICORGANIZATIONERROR = 'lastErrLSPTrafficOrganizationError'
    STATE_LASTERRLSPTRAFFICSERVICEERROR = 'lastErrLSPTrafficServiceError'
    STATE_LASTERRLSPUNKNOWNOBJECTCLASS = 'lastErrLSPUnknownObjectClass'
    STATE_LASTERRLSPUNKNOWNOBJECTCTYPE = 'lastErrLSPUnknownObjectCType'
    STATE_LASTERRLSPUNSUPPORTEDL3PID = 'lastErrLSPUnsupportedL3PID'
    STATE_LSPADMISSIONCONTROLFAILURE = 'lSPAdmissionControlFailure'
    STATE_LSPBADADSPECVALUE = 'lSPBadAdSpecValue'
    STATE_LSPBADEXPLICITROUTE = 'lSPBadExplicitRoute'
    STATE_LSPBADFLOWSPECVALUE = 'lSPBadFlowspecValue'
    STATE_LSPBADINITIALSUBOBJECT = 'lSPBadInitialSubobject'
    STATE_LSPBADLOOSENODE = 'lSPBadLooseNode'
    STATE_LSPBADSTRICTNODE = 'lSPBadStrictNode'
    STATE_LSPBADTSPECVALUE = 'lSPBadTSpecValue'
    STATE_LSPDELAYBOUNDNOTMET = 'lSPDelayBoundNotMet'
    STATE_LSPMPLSALLOCATIONFAILURE = 'lSPMPLSAllocationFailure'
    STATE_LSPMTUTOOBIG = 'lSPMTUTooBig'
    STATE_LSPNONRSVPROUTER = 'lSPNonRSVPRouter'
    STATE_LSPNOROUTEAVAILABLE = 'lSPNoRouteAvailable'
    STATE_LSPPATHERR = 'lSPPathErr'
    STATE_LSPPATHTEARSENT = 'lSPPathTearSent'
    STATE_LSPREQUESTEDBANDWIDTHUNAVAILABLE = 'lSPRequestedBandwidthUnavailable'
    STATE_LSPRESERVATIONNOTRECEIVED = 'lSPReservationNotReceived'
    STATE_LSPRESERVATIONTEARRECEIVED = 'lSPReservationTearReceived'
    STATE_LSPRESERVATIONTEARSENT = 'lSPReservationTearSent'
    STATE_LSPRESERVATIONTIMEOUT = 'lSPReservationTimeout'
    STATE_LSPROUTINGLOOPS = 'lSPRoutingLoops'
    STATE_LSPROUTINGPROBLEM = 'lSPRoutingProblem'
    STATE_LSPRSVPSYSTEMERROR = 'lSPRSVPSystemError'
    STATE_LSPSERVICECONFLICT = 'lSPServiceConflict'
    STATE_LSPSERVICEUNSUPPORTED = 'lSPServiceUnsupported'
    STATE_LSPTRAFFICCONTROLERROR = 'lSPTrafficControlError'
    STATE_LSPTRAFFICCONTROLSYSTEMERROR = 'lSPTrafficControlSystemError'
    STATE_LSPTRAFFICORGANIZATIONERROR = 'lSPTrafficOrganizationError'
    STATE_LSPTRAFFICSERVICEERROR = 'lSPTrafficServiceError'
    STATE_LSPUNKNOWNOBJECTCLASS = 'lSPUnknownObjectClass'
    STATE_LSPUNKNOWNOBJECTCTYPE = 'lSPUnknownObjectCType'
    STATE_LSPUNSUPPORTEDL3PID = 'lSPUnsupportedL3PID'
    STATE_MBBCOMPLETED = 'mbbCompleted'
    STATE_MBBTRIGGERED = 'mbbTriggered'
    STATE_NONE = 'none'

    def __init__(self, ixnhttp):
        super(IxnRsvpP2mpIngressSubLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpP2mpIngressSubLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                localIp: list
                p2mpIdAsNum: list
                p2mpIdAsIp: list
                leafIp: href
                enableEro: href
                prependDut: href
                prefixLengthOfDut: href
                appendLeaf: href
                prefixLengthOfLeaf: href
                sendAsEro: href
                sendAsSero: href
                numberOfEroSubObjects: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpP2mpIngressSubLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2mpIngressLsps","rsvpP2mpIngressSubLsps"], vport_name, emulation_host, filters)


class IxnRsvpPcepExpectedInitiatedLspsEmulation(IxnEmulationHost):
    """Generated NGPF rsvpPcepExpectedInitiatedLsps emulation host """

    STATE_LASTERRLSPADMISSIONCONTROLFAILURE = 'lastErrLSPAdmissionControlFailure'
    STATE_LASTERRLSPBADADSPECVALUE = 'lastErrLSPBadAdSpecValue'
    STATE_LASTERRLSPBADEXPLICITROUTE = 'lastErrLSPBadExplicitRoute'
    STATE_LASTERRLSPBADFLOWSPECVALUE = 'lastErrLSPBadFlowspecValue'
    STATE_LASTERRLSPBADINITIALSUBOBJECT = 'lastErrLSPBadInitialSubobject'
    STATE_LASTERRLSPBADLOOSENODE = 'lastErrLSPBadLooseNode'
    STATE_LASTERRLSPBADSTRICTNODE = 'lastErrLSPBadStrictNode'
    STATE_LASTERRLSPBADTSPECVALUE = 'lastErrLSPBadTSpecValue'
    STATE_LASTERRLSPDELAYBOUNDNOTMET = 'lastErrLSPDelayBoundNotMet'
    STATE_LASTERRLSPMPLSALLOCATIONFAILURE = 'lastErrLSPMPLSAllocationFailure'
    STATE_LASTERRLSPMTUTOOBIG = 'lastErrLSPMTUTooBig'
    STATE_LASTERRLSPNONRSVPROUTER = 'lastErrLSPNonRSVPRouter'
    STATE_LASTERRLSPNOROUTEAVAILABLE = 'lastErrLSPNoRouteAvailable'
    STATE_LASTERRLSPPATHERR = 'lastErrLSPPathErr'
    STATE_LASTERRLSPPATHTEARSENT = 'lastErrLSPPathTearSent'
    STATE_LASTERRLSPREQUESTEDBANDWIDTHUNAVAILABLE = 'lastErrLSPRequestedBandwidthUnavailable'
    STATE_LASTERRLSPRESERVATIONTEARRECEIVED = 'lastErrLSPReservationTearReceived'
    STATE_LASTERRLSPRESERVATIONTEARSENT = 'lastErrLSPReservationTearSent'
    STATE_LASTERRLSPRESERVATIONTIMEOUT = 'lastErrLSPReservationTimeout'
    STATE_LASTERRLSPROUTINGLOOPS = 'lastErrLSPRoutingLoops'
    STATE_LASTERRLSPROUTINGPROBLEM = 'lastErrLSPRoutingProblem'
    STATE_LASTERRLSPRSVPSYSTEMERROR = 'lastErrLSPRSVPSystemError'
    STATE_LASTERRLSPSERVICECONFLICT = 'lastErrLSPServiceConflict'
    STATE_LASTERRLSPSERVICEUNSUPPORTED = 'lastErrLSPServiceUnsupported'
    STATE_LASTERRLSPTRAFFICCONTROLERROR = 'lastErrLSPTrafficControlError'
    STATE_LASTERRLSPTRAFFICCONTROLSYSTEMERROR = 'lastErrLSPTrafficControlSystemError'
    STATE_LASTERRLSPTRAFFICORGANIZATIONERROR = 'lastErrLSPTrafficOrganizationError'
    STATE_LASTERRLSPTRAFFICSERVICEERROR = 'lastErrLSPTrafficServiceError'
    STATE_LASTERRLSPUNKNOWNOBJECTCLASS = 'lastErrLSPUnknownObjectClass'
    STATE_LASTERRLSPUNKNOWNOBJECTCTYPE = 'lastErrLSPUnknownObjectCType'
    STATE_LASTERRLSPUNSUPPORTEDL3PID = 'lastErrLSPUnsupportedL3PID'
    STATE_LSPADMISSIONCONTROLFAILURE = 'lSPAdmissionControlFailure'
    STATE_LSPBADADSPECVALUE = 'lSPBadAdSpecValue'
    STATE_LSPBADEXPLICITROUTE = 'lSPBadExplicitRoute'
    STATE_LSPBADFLOWSPECVALUE = 'lSPBadFlowspecValue'
    STATE_LSPBADINITIALSUBOBJECT = 'lSPBadInitialSubobject'
    STATE_LSPBADLOOSENODE = 'lSPBadLooseNode'
    STATE_LSPBADSTRICTNODE = 'lSPBadStrictNode'
    STATE_LSPBADTSPECVALUE = 'lSPBadTSpecValue'
    STATE_LSPDELAYBOUNDNOTMET = 'lSPDelayBoundNotMet'
    STATE_LSPMPLSALLOCATIONFAILURE = 'lSPMPLSAllocationFailure'
    STATE_LSPMTUTOOBIG = 'lSPMTUTooBig'
    STATE_LSPNONRSVPROUTER = 'lSPNonRSVPRouter'
    STATE_LSPNOROUTEAVAILABLE = 'lSPNoRouteAvailable'
    STATE_LSPPATHERR = 'lSPPathErr'
    STATE_LSPPATHTEARSENT = 'lSPPathTearSent'
    STATE_LSPPCEINITIATEDMSGNOTRECEIVED = 'lSPPceInitiatedMsgNotReceived'
    STATE_LSPREQUESTEDBANDWIDTHUNAVAILABLE = 'lSPRequestedBandwidthUnavailable'
    STATE_LSPRESERVATIONNOTRECEIVED = 'lSPReservationNotReceived'
    STATE_LSPRESERVATIONTEARRECEIVED = 'lSPReservationTearReceived'
    STATE_LSPRESERVATIONTEARSENT = 'lSPReservationTearSent'
    STATE_LSPRESERVATIONTIMEOUT = 'lSPReservationTimeout'
    STATE_LSPROUTINGLOOPS = 'lSPRoutingLoops'
    STATE_LSPROUTINGPROBLEM = 'lSPRoutingProblem'
    STATE_LSPRSVPSYSTEMERROR = 'lSPRSVPSystemError'
    STATE_LSPSERVICECONFLICT = 'lSPServiceConflict'
    STATE_LSPSERVICEUNSUPPORTED = 'lSPServiceUnsupported'
    STATE_LSPTRAFFICCONTROLERROR = 'lSPTrafficControlError'
    STATE_LSPTRAFFICCONTROLSYSTEMERROR = 'lSPTrafficControlSystemError'
    STATE_LSPTRAFFICORGANIZATIONERROR = 'lSPTrafficOrganizationError'
    STATE_LSPTRAFFICSERVICEERROR = 'lSPTrafficServiceError'
    STATE_LSPUNKNOWNOBJECTCLASS = 'lSPUnknownObjectClass'
    STATE_LSPUNKNOWNOBJECTCTYPE = 'lSPUnknownObjectCType'
    STATE_LSPUNSUPPORTEDL3PID = 'lSPUnsupportedL3PID'
    STATE_MBBCOMPLETED = 'mbbCompleted'
    STATE_MBBTRIGGERED = 'mbbTriggered'
    STATE_NONE = 'none'

    def __init__(self, ixnhttp):
        super(IxnRsvpPcepExpectedInitiatedLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpPcepExpectedInitiatedLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                symbolicPathName: href
                backupLspId: href
                enableRRO: href
                numberOfRroSubObjects: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpPcepExpectedInitiatedLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpPcepExpectedInitiatedLsps"], vport_name, emulation_host, filters)


class IxnRsvpRROSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF rsvpRROSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnRsvpRROSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpRROSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                type: href
                ip: href
                protectionAvailable: href
                protectionInUse: href
                label: href
                cType: href
                globalLabel: href
                bandwidthProtection: href
                nodeProtection: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpRROSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2PEgressLsps","rsvpRROSubObjectsList"], vport_name, emulation_host, filters)


class IxnRsvpRroSubObjectsListEmulation(IxnEmulationHost):
    """Generated NGPF rsvpRroSubObjectsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnRsvpRroSubObjectsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpRroSubObjectsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localIp: list
                p2mpIdAsNum: list
                p2mpIdAsIp: list
                type: href
                ip: href
                protectionAvailable: href
                protectionInUse: href
                label: href
                cType: href
                globalLabel: href
                bandwidthProtection: href
                nodeProtection: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnRsvpRroSubObjectsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps","rsvpP2mpEgressLsps","rsvpRroSubObjectsList"], vport_name, emulation_host, filters)


class IxnRsvpteIfEmulation(IxnEmulationHost):
    """Generated NGPF rsvpteIf emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnRsvpteIfEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpteIf emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                usingGatewayIp: href
                ourIp: list
                dutIp: href
                labelSpaceStart: href
                labelSpaceEnd: href
                enableRefreshReduction: href
                summaryRefreshInterval: href
                enableBundleMessageSending: href
                enableHelloExtension: href
                helloInterval: href
                helloTimeoutMultiplier: href
                enableGracefulRestartHelperMode: href
                enableGracefulRestartRestartingMode: href
                advertisedRestartTime: href
                actualRestartTime: href
                recoveryTime: href
                numberOfRestarts: href
                restartStartTime: href
                restartUpTime: href
                enableBfdRegistration: href
                enableBundleMessageThresholdTimer: href
                bundleMessageThresholdTime: href
                labelReqRefCount: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnRsvpteIfEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","rsvpteIf"], vport_name, emulation_host, filters)

    def getlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('getLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('restartDown', expected_state, timeout)

    def rsvprestartneighbor(self, expected_state=None, timeout=None):
        """Gracefully restart selected Neighbors
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('rsvpRestartNeighbor', expected_state, timeout)

    def rsvpresumehello(self, expected_state=None, timeout=None):
        """Resume sending Hello messages from selected Neighbors
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('rsvpResumeHello', expected_state, timeout)

    def rsvpstartsrefresh(self, expected_state=None, timeout=None):
        """Start sending SRefresh messages from selected Neighbors
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('rsvpStartSRefresh', expected_state, timeout)

    def rsvpstophello(self, expected_state=None, timeout=None):
        """Stop sending Hello messages from selected Neighbors
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('rsvpStopHello', expected_state, timeout)

    def rsvpstopsrefresh(self, expected_state=None, timeout=None):
        """Stop sending SRefresh messages from selected Neighbors
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('rsvpStopSRefresh', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Activate/Enable selected Neighbor Pairs
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Deactivate/Disable selected Neighbor Pairs
            For expected_state options see the class state variables
        """
        super(IxnRsvpteIfEmulation, self).call_operation('stop', expected_state, timeout)


class IxnRsvpteLspsEmulation(IxnEmulationHost):
    """Generated NGPF rsvpteLsps emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnRsvpteLspsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific rsvpteLsps emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                portData: href
                localIp: list
                ingressP2PLsps: number
                enableP2PEgress: bool
                p2mpIngressLspCount: number
                p2mpEgressTunnelCount: number
                expectedPceInitiatedLspsCount: number
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnRsvpteLspsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","rsvpteLsps"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnRsvpteLspsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnRsvpteLspsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnRsvpteLspsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnSendgPtpSignalingParamsEmulation(IxnEmulationHost):
    """Generated NGPF sendgPtpSignalingParams emulation host """


    def __init__(self, ixnhttp):
        super(IxnSendgPtpSignalingParamsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific sendgPtpSignalingParams emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                linkDelayInterval: enum
                timeSyncInterval: enum
                announceInterval: enum
                computeNeighborRateRatio: bool
                computeNeighborPropDelay: bool
        """
        return super(IxnSendgPtpSignalingParamsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","ptp","sendgPtpSignalingParams"], vport_name, emulation_host, filters)


class IxnSimInterfaceEmulation(IxnEmulationHost):
    """Generated NGPF simInterface emulation host """


    def __init__(self, ixnhttp):
        super(IxnSimInterfaceEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific simInterface emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSimInterfaceEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface"], vport_name, emulation_host, filters)


class IxnSimInterfaceEthernetConfigEmulation(IxnEmulationHost):
    """Generated NGPF simInterfaceEthernetConfig emulation host """


    def __init__(self, ixnhttp):
        super(IxnSimInterfaceEthernetConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific simInterfaceEthernetConfig emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                fromMac: href
                toMac: href
                vlanCount: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSimInterfaceEthernetConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","simInterfaceEthernetConfig"], vport_name, emulation_host, filters)


class IxnSimInterfaceIPv4ConfigEmulation(IxnEmulationHost):
    """Generated NGPF simInterfaceIPv4Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnSimInterfaceIPv4ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific simInterfaceIPv4Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableIp: href
                fromIP: href
                toIP: href
                subnetPrefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSimInterfaceIPv4ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","simInterfaceIPv4Config"], vport_name, emulation_host, filters)


class IxnSimInterfaceIPv6ConfigEmulation(IxnEmulationHost):
    """Generated NGPF simInterfaceIPv6Config emulation host """


    def __init__(self, ixnhttp):
        super(IxnSimInterfaceIPv6ConfigEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific simInterfaceIPv6Config emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enableIp: href
                fromIP: href
                toIP: href
                subnetPrefixLength: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSimInterfaceIPv6ConfigEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simInterface","simInterfaceIPv6Config"], vport_name, emulation_host, filters)


class IxnSimRouterEmulation(IxnEmulationHost):
    """Generated NGPF simRouter emulation host """


    def __init__(self, ixnhttp):
        super(IxnSimRouterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific simRouter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                routerId: href
                systemId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSimRouterEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouter"], vport_name, emulation_host, filters)


class IxnSimRouterBridgeEmulation(IxnEmulationHost):
    """Generated NGPF simRouterBridge emulation host """


    def __init__(self, ixnhttp):
        super(IxnSimRouterBridgeEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific simRouterBridge emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                systemId: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSimRouterBridgeEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","simRouterBridge"], vport_name, emulation_host, filters)


class IxnSpbNodeTopologyListEmulation(IxnEmulationHost):
    """Generated NGPF spbNodeTopologyList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSpbNodeTopologyListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific spbNodeTopologyList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                cistExternalRootCost: href
                numberOfPorts: href
                portIdentifier: href
                vbit: href
                cistRootId: href
                baseVIDCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSpbNodeTopologyListEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisSpbSimulatedTopologyConfig","spbNodeTopologyList"], vport_name, emulation_host, filters)


class IxnSpbSimEdgeBaseVidListEmulation(IxnEmulationHost):
    """Generated NGPF spbSimEdgeBaseVidList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSpbSimEdgeBaseVidListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific spbSimEdgeBaseVidList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                baseVid: href
                baseVlanPriority: href
                bvlanTpid: href
                ectAlgorithm: href
                useFlagBit: href
                isidCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSpbSimEdgeBaseVidListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisSpbSimRouter","spbSimEdgeTopologyList","spbSimEdgeBaseVidList"], vport_name, emulation_host, filters)


class IxnSpbSimEdgeIsidListEmulation(IxnEmulationHost):
    """Generated NGPF spbSimEdgeIsidList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSpbSimEdgeIsidListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific spbSimEdgeIsidList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                itagEthernetType: href
                isid: href
                transmissionType: href
                tbit: href
                rbit: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSpbSimEdgeIsidListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisSpbSimRouter","spbSimEdgeTopologyList","spbSimEdgeBaseVidList","spbSimEdgeIsidList"], vport_name, emulation_host, filters)


class IxnSpbSimEdgeTopologyListEmulation(IxnEmulationHost):
    """Generated NGPF spbSimEdgeTopologyList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSpbSimEdgeTopologyListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific spbSimEdgeTopologyList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                cistExternalRootCost: href
                numberOfPorts: href
                portIdentifier: href
                vbit: href
                cistRootId: href
                baseVIDCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSpbSimEdgeTopologyListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisSpbSimRouter","spbSimEdgeTopologyList"], vport_name, emulation_host, filters)


class IxnSpbTopologyListEmulation(IxnEmulationHost):
    """Generated NGPF spbTopologyList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSpbTopologyListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific spbTopologyList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                cistExternalRootCost: href
                bridgePriority: href
                spSourceId: href
                linkMetric: href
                numberOfPorts: href
                portIdentifier: href
                vbit: href
                cistRootId: href
                mcidConfName: href
                mcidSignature: href
                auxMcidConfName: href
                auxMcidSignature: href
                baseVidCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSpbTopologyListEmulation, self).find(["topology","deviceGroup","isisSpbRouter","spbTopologyList"], vport_name, emulation_host, filters)


class IxnSrlgValueListEmulation(IxnEmulationHost):
    """Generated NGPF srlgValueList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSrlgValueListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific srlgValueList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                srlgValue: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSrlgValueListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ospfv2","srlgValueList"], vport_name, emulation_host, filters)


class IxnStaticLagEmulation(IxnEmulationHost):
    """Generated NGPF staticLag emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnStaticLagEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific staticLag emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                lagId: href
                portData: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnStaticLagEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","staticLag"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnStaticLagEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start LACP
            For expected_state options see the class state variables
        """
        super(IxnStaticLagEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop LACP
            For expected_state options see the class state variables
        """
        super(IxnStaticLagEmulation, self).call_operation('stop', expected_state, timeout)


class IxnStreamsEmulation(IxnEmulationHost):
    """Generated NGPF streams emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnStreamsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific streams emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                sourceMac: href
                uniqueId: href
                streamId: href
                streamName: href
                destinationMac: href
                vlanId: href
                maxFrameSize: href
                maxIntervalFrames: href
                perFrameOverhead: href
                classMeasurementInterval: href
                srClass: href
                actualBandwidth: list
                dataFramePriority: href
                rank: href
                portTcMaxLatency: href
                active: href
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnStreamsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","streams"], vport_name, emulation_host, filters)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnStreamsEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start MSRP Talker Streams
            For expected_state options see the class state variables
        """
        super(IxnStreamsEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop MSRP Talker Stream
            For expected_state options see the class state variables
        """
        super(IxnStreamsEmulation, self).call_operation('stop', expected_state, timeout)


class IxnSubscribedStreamsEmulation(IxnEmulationHost):
    """Generated NGPF subscribedStreams emulation host """


    def __init__(self, ixnhttp):
        super(IxnSubscribedStreamsEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific subscribedStreams emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                streamId: href
                attributeType: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSubscribedStreamsEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","msrpListener","subscribedStreams"], vport_name, emulation_host, filters)


class IxnSwitchConfigLearnedInfoEmulation(IxnEmulationHost):
    """Generated NGPF switchConfigLearnedInfo emulation host """


    def __init__(self, ixnhttp):
        super(IxnSwitchConfigLearnedInfoEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific switchConfigLearnedInfo emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSwitchConfigLearnedInfoEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","ofChannelLearnedInfoList","switchConfigLearnedInfo"], vport_name, emulation_host, filters)


class IxnSwitchGroupsListEmulation(IxnEmulationHost):
    """Generated NGPF switchGroupsList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSwitchGroupsListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific switchGroupsList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                parentSwitch: string
                active: href
                groupType: href
                maxNumberOfGroups: href
                output: href
                copyTtlOut: href
                copyTtlIn: href
                setMplsTtl: href
                decrementMplsTtl: href
                pushVlan: href
                popVlan: href
                pushMpls: href
                popMpls: href
                setQueue: href
                applyGroup: href
                setNetwork: href
                decrementNetwork: href
                setField: href
                pushPbb: href
                popPbb: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSwitchGroupsListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch","switchGroupsList"], vport_name, emulation_host, filters)


class IxnSwitchTablesListEmulation(IxnEmulationHost):
    """Generated NGPF switchTablesList emulation host """


    def __init__(self, ixnhttp):
        super(IxnSwitchTablesListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific switchTablesList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                parentSwitch: string
                active: href
                tableName: href
                tableId: href
                maxTableEntries: href
                metadataMatch: href
                metadataWrite: href
                featuresSupported: href
                instruction: href
                instructionMiss: href
                autoConfigNextTable: href
                nextTable: href
                nextTableMiss: href
                writeActions: href
                writeActionsMiss: href
                applyActions: href
                applyActionsMiss: href
                match: href
                matchMask: href
                wildcardFeature: href
                wildcardFeatureMask: href
                writeSetField: href
                writeSetFieldMask: href
                writeSetFieldMiss: href
                writeSetFieldMissMask: href
                applySetField: href
                applySetFieldMask: href
                applySetFieldMiss: href
                applySetFieldMissMask: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnSwitchTablesListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowSwitch","switchTablesList"], vport_name, emulation_host, filters)


class IxnTablesEmulation(IxnEmulationHost):
    """Generated NGPF tables emulation host """


    def __init__(self, ixnhttp):
        super(IxnTablesEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific tables emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                channelRemoteIp: list
                channelIndex: list
                active: href
                tableId: href
                tableName: href
                numberOfFlowSet: number
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTablesEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","openFlowController","openFlowChannel","tables"], vport_name, emulation_host, filters)


class IxnTagEmulation(IxnEmulationHost):
    """Generated NGPF tag emulation host """


    def __init__(self, ixnhttp):
        super(IxnTagEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific tag emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                enabled: bool
                name: string
                __id__: href
                count: number
        """
        return super(IxnTagEmulation, self).find(["topology","deviceGroup","ipv4Loopback","tag"], vport_name, emulation_host, filters)


class IxnTopologyEmulation(IxnEmulationHost):
    """Generated NGPF topology emulation host """


    def __init__(self, ixnhttp):
        super(IxnTopologyEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific topology emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                assignedPortCount: number
                descriptiveName: string
                errors: list
                l1SettingsGroup: href
                name: string
                portCount: number
                status: enum
                vports: list
        """
        return super(IxnTopologyEmulation, self).find(["topology"], vport_name, emulation_host, filters)


class IxnTrillMCastIpv4GroupListEmulation(IxnEmulationHost):
    """Generated NGPF trillMCastIpv4GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillMCastIpv4GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillMCastIpv4GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localSystemID: list
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillMCastIpv4GroupListEmulation, self).find(["topology","deviceGroup","isisTrillRouter","trillMCastIpv4GroupList"], vport_name, emulation_host, filters)


class IxnTrillMCastIpv6GroupListEmulation(IxnEmulationHost):
    """Generated NGPF trillMCastIpv6GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillMCastIpv6GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillMCastIpv6GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localSystemID: list
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillMCastIpv6GroupListEmulation, self).find(["topology","deviceGroup","isisTrillRouter","trillMCastIpv6GroupList"], vport_name, emulation_host, filters)


class IxnTrillMCastMacGroupListEmulation(IxnEmulationHost):
    """Generated NGPF trillMCastMacGroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillMCastMacGroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillMCastMacGroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                localSystemID: list
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrCnt: href
                mcastAddrIncr: href
                startUcastAddr: href
                ucastSrcCnt: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillMCastMacGroupListEmulation, self).find(["topology","deviceGroup","isisTrillRouter","trillMCastMacGroupList"], vport_name, emulation_host, filters)


class IxnTrillNodeTopologyListEmulation(IxnEmulationHost):
    """Generated NGPF trillNodeTopologyList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillNodeTopologyListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillNodeTopologyList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                noOfTreesToCompute: href
                interestedVlanRangeCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillNodeTopologyListEmulation, self).find(["topology","deviceGroup","networkGroup","networkTopology","isisTrillSimulatedTopologyConfig","trillNodeTopologyList"], vport_name, emulation_host, filters)


class IxnTrillSimulatedMCastIpv4GroupListEmulation(IxnEmulationHost):
    """Generated NGPF trillSimulatedMCastIpv4GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillSimulatedMCastIpv4GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillSimulatedMCastIpv4GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillSimulatedMCastIpv4GroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisTrillSimRouter","trillSimulatedMCastIpv4GroupList"], vport_name, emulation_host, filters)


class IxnTrillSimulatedMCastIpv6GroupListEmulation(IxnEmulationHost):
    """Generated NGPF trillSimulatedMCastIpv6GroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillSimulatedMCastIpv6GroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillSimulatedMCastIpv6GroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrIncr: href
                mcastAddrCnt: href
                ucastSrcCnt: href
                startUcastAddr: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillSimulatedMCastIpv6GroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisTrillSimRouter","trillSimulatedMCastIpv6GroupList"], vport_name, emulation_host, filters)


class IxnTrillSimulatedMCastMacGroupListEmulation(IxnEmulationHost):
    """Generated NGPF trillSimulatedMCastMacGroupList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillSimulatedMCastMacGroupListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillSimulatedMCastMacGroupList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                topologyId: href
                srcGrpMapping: href
                startMcastAddr: href
                mcastAddrCnt: href
                mcastAddrIncr: href
                startUcastAddr: href
                ucastSrcCnt: href
                ucastAddrIncr: href
                interGrpUcastAddrIncr: href
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillSimulatedMCastMacGroupListEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","greoipv4","isisTrillSimRouter","trillSimulatedMCastMacGroupList"], vport_name, emulation_host, filters)


class IxnTrillTopologyListEmulation(IxnEmulationHost):
    """Generated NGPF trillTopologyList emulation host """


    def __init__(self, ixnhttp):
        super(IxnTrillTopologyListEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific trillTopologyList emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                topologyId: href
                noOfTreesToCompute: href
                localSystemID: list
                nicknameCount: number
                interestedVlanRangeCount: number
                active: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnTrillTopologyListEmulation, self).find(["topology","deviceGroup","isisTrillRouter","trillTopologyList"], vport_name, emulation_host, filters)


class IxnVlanEmulation(IxnEmulationHost):
    """Generated NGPF vlan emulation host """


    def __init__(self, ixnhttp):
        super(IxnVlanEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific vlan emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                vlanId: href
                priority: href
                tpid: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnVlanEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","vlan"], vport_name, emulation_host, filters)


class IxnVpnParameterEmulation(IxnEmulationHost):
    """Generated NGPF vpnParameter emulation host """


    def __init__(self, ixnhttp):
        super(IxnVpnParameterEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific vpnParameter emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                useVpnParameters: bool
                siteId: href
                count: number
        """
        return super(IxnVpnParameterEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","vpnParameter"], vport_name, emulation_host, filters)


class IxnVxlanEmulation(IxnEmulationHost):
    """Generated NGPF vxlan emulation host """

    STATE_DOWN = 'down'
    STATE_NOTSTARTED = 'notStarted'
    STATE_UP = 'up'

    def __init__(self, ixnhttp):
        super(IxnVxlanEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific vxlan emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                globalAndPortData: href
                vni: href
                ipv4_multicast: href
                enableStaticInfo: bool
                externalLearning: bool
                runningMode: enum
                staticInfoCount: number
                ovsdbConnectorMultiplier: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: enum
                errors: list
        """
        return super(IxnVxlanEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","vxlan"], vport_name, emulation_host, filters)

    def clearalllearnedinfo(self, expected_state=None, timeout=None):
        """Clear All Learned Info
            For expected_state options see the class state variables
        """
        super(IxnVxlanEmulation, self).call_operation('clearAllLearnedInfo', expected_state, timeout)

    def getvxlanlearnedinfo(self, expected_state=None, timeout=None):
        """Get Learned Info
            For expected_state options see the class state variables
        """
        super(IxnVxlanEmulation, self).call_operation('getVXLANLearnedInfo', expected_state, timeout)

    def restartdown(self, expected_state=None, timeout=None):
        """Stop and start interfaces and sessions that are in Down state.
            For expected_state options see the class state variables
        """
        super(IxnVxlanEmulation, self).call_operation('restartDown', expected_state, timeout)

    def start(self, expected_state=None, timeout=None):
        """Start selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnVxlanEmulation, self).call_operation('start', expected_state, timeout)

    def stop(self, expected_state=None, timeout=None):
        """Stop selected protocols.
            For expected_state options see the class state variables
        """
        super(IxnVxlanEmulation, self).call_operation('stop', expected_state, timeout)


class IxnVxlanStaticInfoEmulation(IxnEmulationHost):
    """Generated NGPF vxlanStaticInfo emulation host """


    def __init__(self, ixnhttp):
        super(IxnVxlanStaticInfoEmulation, self).__init__(ixnhttp)

    def find(self, vport_name=None, emulation_host=None, **filters):
        """Find specific vxlanStaticInfo emulated host sessions using a virtual port name or a parent emulation host and optional filters.
            Filter values can be a single value or a list of values, see the specific **filter information below.

            vport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)
            emulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)
            **filters:
                active: href
                localVNI: list
                remoteVtepIpv4: href
                suppressArp: href
                remoteVmStaticMac: href
                remoteVmStaticIpv4: href
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnVxlanStaticInfoEmulation, self).find(["topology","deviceGroup","ipv4Loopback","ldpTargetedRouter","ldppwvpls","ipv6Loopback","ldpTargetedRouterV6","ldpotherpws","ethernet","ipv6","greoipv6","ipv4","lns","pppoxserver","vxlan","vxlanStaticInfo"], vport_name, emulation_host, filters)


