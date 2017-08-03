from ixnetwork.IxnEmulationHost import IxnEmulationHost

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
                sourceIp4: string | list[string] (string type: ipv4)
                localRouterId: list
                noOfSessions: number
                aggregateBfdSession: bool
                vni: list
                minRxInterval: string | list[string] (string type: decimal)
                txInterval: string | list[string] (string type: decimal)
                echoRxInterval: string | list[string] (string type: decimal)
                echoTxInterval: string | list[string] (string type: decimal)
                echoTimeOut: string | list[string] (string type: decimal)
                configureEchoSourceIp: string | list[string] (string type: bool)
                enableDemandMode: string | list[string] (string type: bool)
                enableControlPlaneIndependent: string | list[string] (string type: bool)
                pollInterval: string | list[string] (string type: decimal)
                timeoutMultiplier: string | list[string] (string type: decimal)
                flapTxIntervals: string | list[string] (string type: decimal)
                ipDiffServ: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnBfdv4InterfaceEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","bfdv4Interface"], vport_name, emulation_host, filters)

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
                sourceIp6: string | list[string] (string type: ipv6)
                localRouterId: list
                noOfSessions: number
                aggregateBfdSession: bool
                vni: list
                minRxInterval: string | list[string] (string type: decimal)
                txInterval: string | list[string] (string type: decimal)
                echoRxInterval: string | list[string] (string type: decimal)
                echoTxInterval: string | list[string] (string type: decimal)
                echoTimeOut: string | list[string] (string type: decimal)
                configureEchoSourceIp: string | list[string] (string type: bool)
                enableDemandMode: string | list[string] (string type: bool)
                enableControlPlaneIndependent: string | list[string] (string type: bool)
                pollInterval: string | list[string] (string type: decimal)
                timeoutMultiplier: string | list[string] (string type: decimal)
                flapTxIntervals: string | list[string] (string type: decimal)
                ipDiffServ: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnBfdv6InterfaceEmulation, self).find(["topology","deviceGroup","ethernet","ipv6","bfdv6Interface"], vport_name, emulation_host, filters)

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
                enableBgpId: string | list[string] (string type: bool)
                enableBgpIdSameasRouterId: string | list[string] (string type: bool)
                bgpId: string | list[string] (string type: ipv4)
                localIpv4Ver2: list
                dutIp: string | list[string] (string type: ipv4)
                ethernetSegmentsCountV4: number
                numberFlowSpecRangeV4: number
                numberFlowSpecRangeV6: number
                numberSRTEPolicies: number
                irbIpv4Address: string | list[string] (string type: ipv4)
                portData: href
                localRouterID: list
                vplsEnableNextHop: string | list[string] (string type: bool)
                vplsNextHop: string | list[string] (string type: ipv4)
                enable4ByteAs: string | list[string] (string type: bool)
                localAs2Bytes: string | list[string] (string type: decimal)
                localAs4Bytes: string | list[string] (string type: decimal)
                asSetMode: string (string type: enum  enums: dontincludelocalas|includelocalasasasseq|includelocalasasasset|includelocalasasasseqconfederation|includelocalasasassetconfederation|prependlocalastofirstsegment)
                enableBfdRegistration: string | list[string] (string type: bool)
                modeOfBfdOperations: string (string type: enum  enums: multihop|singlehop)
                holdTimer: string | list[string] (string type: decimal)
                configureKeepaliveTimer: string | list[string] (string type: bool)
                keepaliveTimer: string | list[string] (string type: decimal)
                updateInterval: string | list[string] (string type: decimal)
                ttl: string | list[string] (string type: decimal)
                enableGracefulRestart: string | list[string] (string type: bool)
                enableLlgr: string | list[string] (string type: bool)
                restartTime: string | list[string] (string type: decimal)
                staleTime: string | list[string] (string type: decimal)
                actAsRestarted: string | list[string] (string type: bool)
                advertiseEndOfRib: string | list[string] (string type: bool)
                type: string (string type: enum  enums: internal|external)
                authentication: string (string type: enum  enums: null|md5)
                md5Key: string | list[string] (string type: string)
                discardIxiaGeneratedRoutes: string | list[string] (string type: bool)
                sendIxiaSignatureWithRoutes: string | list[string] (string type: bool)
                tcpWindowSizeInBytes: string | list[string] (string type: decimal)
                numBgpUpdatesGeneratedPerIteration: string | list[string] (string type: decimal)
                flap: string | list[string] (string type: bool)
                uptimeInSec: string | list[string] (string type: decimal)
                downtimeInSec: string | list[string] (string type: decimal)
                filterIpV4Unicast: string | list[string] (string type: bool)
                filterIpV4Multicast: string | list[string] (string type: bool)
                filterIpV4Mpls: string | list[string] (string type: bool)
                filterIpV4MplsVpn: string | list[string] (string type: bool)
                filterIpV6Unicast: string | list[string] (string type: bool)
                filterIpV6Multicast: string | list[string] (string type: bool)
                filterIpV6Mpls: string | list[string] (string type: bool)
                filterIpV6MplsVpn: string | list[string] (string type: bool)
                filterVpls: string | list[string] (string type: bool)
                filterIpV4MulticastVpn: string | list[string] (string type: bool)
                filterIpV6MulticastVpn: string | list[string] (string type: bool)
                filterEvpn: string | list[string] (string type: bool)
                filterLinkState: string | list[string] (string type: bool)
                filterIpv4MulticastBgpMplsVpn: string | list[string] (string type: bool)
                filterIpv6MulticastBgpMplsVpn: string | list[string] (string type: bool)
                filterIpv4UnicastFlowSpec: string | list[string] (string type: bool)
                filterIpv6UnicastFlowSpec: string | list[string] (string type: bool)
                filterSRTEPoliciesV4: string | list[string] (string type: bool)
                filterSRTEPoliciesV6: string | list[string] (string type: bool)
                capabilityIpV4Unicast: string | list[string] (string type: bool)
                capabilityIpV4Multicast: string | list[string] (string type: bool)
                capabilityIpV4MplsVpn: string | list[string] (string type: bool)
                capabilityIpV6Unicast: string | list[string] (string type: bool)
                capabilityIpV6Multicast: string | list[string] (string type: bool)
                capabilityIpV6MplsVpn: string | list[string] (string type: bool)
                capabilityIpV4Mdt: string | list[string] (string type: bool)
                capabilityVpls: string | list[string] (string type: bool)
                capabilityIpV4MulticastVpn: string | list[string] (string type: bool)
                capabilityIpV6MulticastVpn: string | list[string] (string type: bool)
                capabilityRouteRefresh: string | list[string] (string type: bool)
                capabilityRouteConstraint: string | list[string] (string type: bool)
                capabilityLinkStateNonVpn: string | list[string] (string type: bool)
                evpn: string | list[string] (string type: bool)
                ipv4MulticastBgpMplsVpn: string | list[string] (string type: bool)
                ipv6MulticastBgpMplsVpn: string | list[string] (string type: bool)
                capabilityipv4UnicastFlowSpec: string | list[string] (string type: bool)
                capabilityipv6UnicastFlowSpec: string | list[string] (string type: bool)
                capabilitySRTEPoliciesV4: string | list[string] (string type: bool)
                capabilitySRTEPoliciesV6: string | list[string] (string type: bool)
                capabilityIpv4UnicastAddPath: string | list[string] (string type: bool)
                capabilityIpv6UnicastAddPath: string | list[string] (string type: bool)
                ipv4UnicastAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                ipv6UnicastAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                ipv4MplsAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                ipv6MplsAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                operationalModel: string (string type: enum  enums: symmetric|asymmetric)
                ipVrfToIpVrfType: string (string type: enum  enums: interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB|interfaceLess)
                routersMacOrIrbMacAddress: string | list[string] (string type: mac)
                irbInterfaceLabel: string | list[string] (string type: decimal)
                customSidType: string | list[string] (string type: decimal)
                ipv4MplsCapability: bool
                ipv6MplsCapability: bool
                capabilityIpv4MplsAddPath: bool
                capabilityIpv6MplsAddPath: bool
                sRGBRangeCount: number
                numBgpLsId: string | list[string] (string type: decimal)
                numBgpLsInstanceIdentifier: string | list[string] (string type: decimal)
                bgpLsNoOfCommunities: number
                enableBgpLsCommunity: string | list[string] (string type: bool)
                noOfExtendedCommunities: number
                bgpLsEnableExtendedCommunity: string | list[string] (string type: bool)
                bgpLsOverridePeerAsSetMode: string | list[string] (string type: bool)
                bgpLsAsSetMode: string (string type: enum  enums: dontincludelocalas|includelocalasasasseq|includelocalasasasset|includelocalasasasseqconfederation|includelocalasasassetconfederation|prependlocalastofirstsegment)
                bgpLsNoOfASPathSegments: number
                bgpLsEnableAsPathSegments: string | list[string] (string type: bool)
                bgpLsNoOfClusters: number
                bgpLsEnableCluster: string | list[string] (string type: bool)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnBgpIpv4PeerEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","bgpIpv4Peer"], vport_name, emulation_host, filters)

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
                enableBgpId: string | list[string] (string type: bool)
                enableBgpIdSameAsRouterId: string | list[string] (string type: bool)
                bgpId: string | list[string] (string type: ipv4)
                localIpv6Ver2: list
                dutIp: string | list[string] (string type: ipv6)
                ethernetSegmentsCountV6: number
                numberFlowSpecRangeV4: number
                numberFlowSpecRangeV6: number
                numberSRTEPolicies: number
                irbIpv6Address: string | list[string] (string type: ipv6)
                portData: href
                localRouterID: list
                vplsEnableNextHop: string | list[string] (string type: bool)
                vplsNextHop: string | list[string] (string type: ipv4)
                enable4ByteAs: string | list[string] (string type: bool)
                localAs2Bytes: string | list[string] (string type: decimal)
                localAs4Bytes: string | list[string] (string type: decimal)
                asSetMode: string (string type: enum  enums: dontincludelocalas|includelocalasasasseq|includelocalasasasset|includelocalasasasseqconfederation|includelocalasasassetconfederation|prependlocalastofirstsegment)
                enableBfdRegistration: string | list[string] (string type: bool)
                modeOfBfdOperations: string (string type: enum  enums: multihop|singlehop)
                holdTimer: string | list[string] (string type: decimal)
                configureKeepaliveTimer: string | list[string] (string type: bool)
                keepaliveTimer: string | list[string] (string type: decimal)
                updateInterval: string | list[string] (string type: decimal)
                ttl: string | list[string] (string type: decimal)
                enableGracefulRestart: string | list[string] (string type: bool)
                enableLlgr: string | list[string] (string type: bool)
                restartTime: string | list[string] (string type: decimal)
                staleTime: string | list[string] (string type: decimal)
                actAsRestarted: string | list[string] (string type: bool)
                advertiseEndOfRib: string | list[string] (string type: bool)
                type: string (string type: enum  enums: internal|external)
                authentication: string (string type: enum  enums: null|md5)
                md5Key: string | list[string] (string type: string)
                discardIxiaGeneratedRoutes: string | list[string] (string type: bool)
                sendIxiaSignatureWithRoutes: string | list[string] (string type: bool)
                tcpWindowSizeInBytes: string | list[string] (string type: decimal)
                numBgpUpdatesGeneratedPerIteration: string | list[string] (string type: decimal)
                flap: string | list[string] (string type: bool)
                uptimeInSec: string | list[string] (string type: decimal)
                downtimeInSec: string | list[string] (string type: decimal)
                filterIpV4Unicast: string | list[string] (string type: bool)
                filterIpV4Multicast: string | list[string] (string type: bool)
                filterIpV4Mpls: string | list[string] (string type: bool)
                filterIpV4MplsVpn: string | list[string] (string type: bool)
                filterIpV6Unicast: string | list[string] (string type: bool)
                filterIpV6Multicast: string | list[string] (string type: bool)
                filterIpV6Mpls: string | list[string] (string type: bool)
                filterIpV6MplsVpn: string | list[string] (string type: bool)
                filterVpls: string | list[string] (string type: bool)
                filterIpV4MulticastVpn: string | list[string] (string type: bool)
                filterIpV6MulticastVpn: string | list[string] (string type: bool)
                filterEvpn: string | list[string] (string type: bool)
                filterLinkState: string | list[string] (string type: bool)
                filterIpv4MulticastBgpMplsVpn: string | list[string] (string type: bool)
                filterIpv6MulticastBgpMplsVpn: string | list[string] (string type: bool)
                filterIpv4UnicastFlowSpec: string | list[string] (string type: bool)
                filterIpv6UnicastFlowSpec: string | list[string] (string type: bool)
                filterSRTEPoliciesV4: string | list[string] (string type: bool)
                filterSRTEPoliciesV6: string | list[string] (string type: bool)
                capabilityIpV4Unicast: string | list[string] (string type: bool)
                capabilityIpV4Multicast: string | list[string] (string type: bool)
                capabilityIpV4MplsVpn: string | list[string] (string type: bool)
                capabilityIpV6Unicast: string | list[string] (string type: bool)
                capabilityIpV6Multicast: string | list[string] (string type: bool)
                capabilityIpV6MplsVpn: string | list[string] (string type: bool)
                capabilityIpV4Mdt: string | list[string] (string type: bool)
                capabilityVpls: string | list[string] (string type: bool)
                capabilityIpV4MulticastVpn: string | list[string] (string type: bool)
                capabilityIpV6MulticastVpn: string | list[string] (string type: bool)
                capabilityRouteRefresh: string | list[string] (string type: bool)
                capabilityRouteConstraint: string | list[string] (string type: bool)
                capabilityLinkStateNonVpn: string | list[string] (string type: bool)
                evpn: string | list[string] (string type: bool)
                ipv4MulticastBgpMplsVpn: string | list[string] (string type: bool)
                ipv6MulticastBgpMplsVpn: string | list[string] (string type: bool)
                capabilityipv4UnicastFlowSpec: string | list[string] (string type: bool)
                capabilityipv6UnicastFlowSpec: string | list[string] (string type: bool)
                capabilitySRTEPoliciesV4: string | list[string] (string type: bool)
                capabilitySRTEPoliciesV6: string | list[string] (string type: bool)
                capabilityIpv4UnicastAddPath: string | list[string] (string type: bool)
                capabilityIpv6UnicastAddPath: string | list[string] (string type: bool)
                ipv4UnicastAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                ipv6UnicastAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                ipv4MplsAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                ipv6MplsAddPathMode: string (string type: enum  enums: receiveonly|sendonly|both)
                operationalModel: string (string type: enum  enums: symmetric|asymmetric)
                ipVrfToIpVrfType: string (string type: enum  enums: interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB|interfaceLess)
                routersMacOrIrbMacAddress: string | list[string] (string type: mac)
                irbInterfaceLabel: string | list[string] (string type: decimal)
                customSidType: string | list[string] (string type: decimal)
                ipv4MplsCapability: bool
                ipv6MplsCapability: bool
                capabilityIpv4MplsAddPath: bool
                capabilityIpv6MplsAddPath: bool
                sRGBRangeCount: number
                numBgpLsId: string | list[string] (string type: decimal)
                numBgpLsInstanceIdentifier: string | list[string] (string type: decimal)
                bgpLsNoOfCommunities: number
                enableBgpLsCommunity: string | list[string] (string type: bool)
                noOfExtendedCommunities: number
                bgpLsEnableExtendedCommunity: string | list[string] (string type: bool)
                bgpLsOverridePeerAsSetMode: string | list[string] (string type: bool)
                bgpLsAsSetMode: string (string type: enum  enums: dontincludelocalas|includelocalasasasseq|includelocalasasasset|includelocalasasasseqconfederation|includelocalasasassetconfederation|prependlocalastofirstsegment)
                bgpLsNoOfASPathSegments: number
                bgpLsEnableAsPathSegments: string | list[string] (string type: bool)
                bgpLsNoOfClusters: number
                bgpLsEnableCluster: string | list[string] (string type: bool)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnBgpIpv6PeerEmulation, self).find(["topology","deviceGroup","ethernet","ipv6","bgpIpv6Peer"], vport_name, emulation_host, filters)

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
                dhcp4GatewayAddress: string | list[string] (string type: ipv4)
                dhcp4GatewayMac: string | list[string] (string type: mac)
                renewTimer: string | list[string] (string type: decimal)
                useRapidCommit: string | list[string] (string type: bool)
                dhcp4UseFirstServer: string | list[string] (string type: bool)
                dhcp4ServerAddress: string | list[string] (string type: ipv4)
                dhcp4Broadcast: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnDhcpv4clientEmulation, self).find(["topology","deviceGroup","ethernet","dhcpv4client"], vport_name, emulation_host, filters)

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
                renewTimer: string | list[string] (string type: decimal)
                useRapidCommit: string | list[string] (string type: bool)
                dhcp6DuidType: string (string type: enum  enums: duid_llt|duid_en|duid_ll)
                dhcp6DuidEnterpriseId: string | list[string] (string type: decimal)
                dhcp6DuidVendorId: string | list[string] (string type: decimal)
                dhcp6IaType: string (string type: enum  enums: iana|iata|iapd|iana_iapd)
                dhcp6UsePDGlobalAddress: string | list[string] (string type: bool)
                dhcp6IaId: string | list[string] (string type: decimal)
                dhcp6IaIdInc: string | list[string] (string type: decimal)
                dhcp6IaT1: string | list[string] (string type: decimal)
                dhcp6IaT2: string | list[string] (string type: decimal)
                enableStateless: bool
                dhcp6GatewayAddress: string | list[string] (string type: ipv6)
                dhcp6GatewayMac: string | list[string] (string type: mac)
                noOfAddresses: list
                noOfPrefixes: list
                dhcp6IANACount: string | list[string] (string type: decimal)
                dhcp6IAPDCount: string | list[string] (string type: decimal)
                maxNoPerClient: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnDhcpv6clientEmulation, self).find(["topology","deviceGroup","ethernet","dhcpv6client"], vport_name, emulation_host, filters)

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
                mac: string | list[string] (string type: mac)
                mtu: string | list[string] (string type: decimal)
                notifyMACMove: bool
                enableVlans: string | list[string] (string type: bool)
                vlanCount: number
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnEthernetEmulation, self).find(["topology","deviceGroup","ethernet"], vport_name, emulation_host, filters)

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
                versionType: string (string type: enum  enums: version1|version2|version3)
                noOfGrpRanges: number
                routerAlert: string | list[string] (string type: bool)
                gQResponseMode: string | list[string] (string type: bool)
                gSResponseMode: string | list[string] (string type: bool)
                uSResponseMode: string | list[string] (string type: bool)
                reportFreq: string | list[string] (string type: decimal)
                imResponse: string | list[string] (string type: bool)
                jlMultiplier: number
                enableProxyReporting: string | list[string] (string type: bool)
                enableIptv: string | list[string] (string type: bool)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnIgmpHostEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","igmpHost"], vport_name, emulation_host, filters)

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
                startMcastAddr: string | list[string] (string type: ipv4)
                mcastAddrIncr: string | list[string] (string type: ipv4)
                sourceMode: string (string type: enum  enums: include|exclude)
                noOfSrcRanges: number
                mcastAddrCnt: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIgmpMcastIPv4GroupListEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","igmpHost","igmpMcastIPv4GroupList"], vport_name, emulation_host, filters)

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
                startUcastAddr: string | list[string] (string type: ipv4)
                ucastAddrIncr: string | list[string] (string type: ipv4)
                ucastSrcAddrCnt: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIgmpUcastIPv4SourceListEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","igmpHost","igmpMcastIPv4GroupList","igmpUcastIPv4SourceList"], vport_name, emulation_host, filters)

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
                stbLeaveJoinDelay: string | list[string] (string type: decimal)
                joinLatencyThreshold: string | list[string] (string type: decimal)
                leaveLatencyThreshold: string | list[string] (string type: decimal)
                logFailureTimestamps: string | list[string] (string type: bool)
                logAllTimestamps: string | list[string] (string type: bool)
                zapBehavior: string (string type: enum  enums: zaponly|zapandview|onetime)
                zapDirection: string (string type: enum  enums: up|down|random)
                zapIntervalType: string (string type: enum  enums: leavetoleave|multicasttoleave)
                zapInterval: string | list[string] (string type: decimal)
                numChannelChangesBeforeView: string | list[string] (string type: decimal)
                viewDuration: string | list[string] (string type: decimal)
                enableGeneralQueryResponse: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnIptvEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","igmpHost","iptv"], vport_name, emulation_host, filters)

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
                address: string | list[string] (string type: ipv4)
                prefix: string | list[string] (string type: decimal)
                gatewayIp: string | list[string] (string type: ipv4)
                resolveGateway: string | list[string] (string type: bool)
                resolvedGatewayMac: list
                manualGatewayMac: string | list[string] (string type: mac)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnIpv4Emulation, self).find(["topology","deviceGroup","ethernet","ipv4"], vport_name, emulation_host, filters)

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
                address: string | list[string] (string type: ipv6)
                prefix: string | list[string] (string type: decimal)
                gatewayIp: string | list[string] (string type: ipv6)
                resolveGateway: string | list[string] (string type: bool)
                resolvedGatewayMac: list
                manualGatewayMac: string | list[string] (string type: mac)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnIpv6Emulation, self).find(["topology","deviceGroup","ethernet","ipv6"], vport_name, emulation_host, filters)

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
                interfaceMetric: string | list[string] (string type: decimal)
                networkType: string (string type: enum  enums: pointpoint|broadcast)
                levelType: string (string type: enum  enums: level1|level2|l1l2)
                enable3WayHandshake: string | list[string] (string type: bool)
                extendedLocalCircuitId: string | list[string] (string type: decimal)
                level1HelloInterval: string | list[string] (string type: decimal)
                level1DeadInterval: string | list[string] (string type: decimal)
                localSystemID: list
                enableConfiguredHoldTime: string | list[string] (string type: bool)
                configuredHoldTime: string | list[string] (string type: decimal)
                authType: string (string type: enum  enums: none|password|md5)
                circuitTranmitPasswordOrMD5Key: string | list[string] (string type: string)
                autoAdjustMTU: string | list[string] (string type: bool)
                autoAdjustArea: string | list[string] (string type: bool)
                autoAdjustSupportedProtocols: string | list[string] (string type: bool)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnIsisFabricPathEmulation, self).find(["topology","deviceGroup","ethernet","isisFabricPath"], vport_name, emulation_host, filters)

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
                interfaceMetric: string | list[string] (string type: decimal)
                ipv6MTMetric: string | list[string] (string type: decimal)
                networkType: string (string type: enum  enums: pointpoint|broadcast)
                enable3WayHandshake: string | list[string] (string type: bool)
                extendedLocalCircuitId: string | list[string] (string type: decimal)
                levelType: string (string type: enum  enums: level1|level2|l1l2)
                level1Priority: string | list[string] (string type: decimal)
                level2Priority: string | list[string] (string type: decimal)
                level1HelloInterval: string | list[string] (string type: decimal)
                level1DeadInterval: string | list[string] (string type: decimal)
                level2HelloInterval: string | list[string] (string type: decimal)
                level2DeadInterval: string | list[string] (string type: decimal)
                enableBfdRegistration: string | list[string] (string type: bool)
                enableAdjSID: string | list[string] (string type: bool)
                adjSID: string | list[string] (string type: decimal)
                ipv6SidValue: string | list[string] (string type: ipv6)
                overrideFFlag: string | list[string] (string type: bool)
                fFlag: string | list[string] (string type: bool)
                bFlag: string | list[string] (string type: bool)
                vFlag: string | list[string] (string type: bool)
                lFlag: string | list[string] (string type: bool)
                sFlag: string | list[string] (string type: bool)
                weight: string | list[string] (string type: decimal)
                enableLinkProtection: string | list[string] (string type: bool)
                extraTraffic: string | list[string] (string type: bool)
                unprotected: string | list[string] (string type: bool)
                shared: string | list[string] (string type: bool)
                dedicatedOneToOne: string | list[string] (string type: bool)
                dedicatedOnePlusOne: string | list[string] (string type: bool)
                enhanced: string | list[string] (string type: bool)
                reserved0x40: string | list[string] (string type: bool)
                reserved0x80: string | list[string] (string type: bool)
                suppressHello: string | list[string] (string type: bool)
                enableSRLG: string | list[string] (string type: bool)
                srlgCount: number
                localSystemID: list
                enableConfiguredHoldTime: string | list[string] (string type: bool)
                configuredHoldTime: string | list[string] (string type: decimal)
                authType: string (string type: enum  enums: none|password|md5)
                circuitTranmitPasswordOrMD5Key: string | list[string] (string type: string)
                autoAdjustMTU: string | list[string] (string type: bool)
                autoAdjustArea: string | list[string] (string type: bool)
                autoAdjustSupportedProtocols: string | list[string] (string type: bool)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnIsisL3Emulation, self).find(["topology","deviceGroup","ethernet","isisL3"], vport_name, emulation_host, filters)

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
                administrativeKey: string | list[string] (string type: decimal)
                actorSystemId: string | list[string] (string type: hex8WithSpaces)
                actorSystemPriority: string | list[string] (string type: decimal)
                actorKey: string | list[string] (string type: decimal)
                actorPortNumber: string | list[string] (string type: decimal)
                actorPortPriority: string | list[string] (string type: decimal)
                sourceMac: list
                collectorsMaxdelay: string | list[string] (string type: decimal)
                lacpduPeriodicTimeInterval: string | list[string] (string type: decimal)
                lacpduTimeout: string | list[string] (string type: decimal)
                lacpActivity: string (string type: enum  enums: active|passive)
                supportRespondingToMarker: string | list[string] (string type: bool)
                markerResponseWaitTime: string | list[string] (string type: decimal)
                periodicSendingOfMarkerRequest: string | list[string] (string type: bool)
                markerRequestMode: string (string type: enum  enums: fixed|random)
                interMarkerPDUDelay: string | list[string] (string type: decimal)
                interMarkerPDUDelayRandomMin: string | list[string] (string type: decimal)
                interMarkerPDUDelayRandomMax: string | list[string] (string type: decimal)
                sendMarkerRequestOnLagChange: string | list[string] (string type: bool)
                aggregationFlagState: string | list[string] (string type: bool)
                synchronizationFlag: string | list[string] (string type: bool)
                distributingFlag: string | list[string] (string type: bool)
                collectingFlag: string | list[string] (string type: bool)
                portData: href
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnLacpEmulation, self).find(["topology","deviceGroup","ethernet","lacp"], vport_name, emulation_host, filters)

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
                versionType: string (string type: enum  enums: version1|version2)
                noOfGrpRanges: number
                routerAlert: string | list[string] (string type: bool)
                gQResponseMode: string | list[string] (string type: bool)
                gSResponseMode: string | list[string] (string type: bool)
                uSResponseMode: string | list[string] (string type: bool)
                reportFreq: string | list[string] (string type: decimal)
                imResponse: string | list[string] (string type: bool)
                jlMultiplier: number
                enableProxyReporting: string | list[string] (string type: bool)
                enableIptv: string | list[string] (string type: bool)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnMldHostEmulation, self).find(["topology","deviceGroup","ethernet","ipv6","mldHost"], vport_name, emulation_host, filters)

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
                startMcastAddr: string | list[string] (string type: ipv6)
                mcastAddrIncr: string | list[string] (string type: ipv6)
                sourceMode: string (string type: enum  enums: include|exclude)
                noOfSrcRanges: number
                mcastAddrCnt: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMldMcastIPv6GroupListEmulation, self).find(["topology","deviceGroup","ethernet","ipv6","mldHost","mldMcastIPv6GroupList"], vport_name, emulation_host, filters)

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
                startUcastAddr: string | list[string] (string type: ipv6)
                ucastAddrIncr: string | list[string] (string type: ipv6)
                ucastSrcAddrCnt: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnMldUcastIPv6SourceListEmulation, self).find(["topology","deviceGroup","ethernet","ipv6","mldHost","mldMcastIPv6GroupList","mldUcastIPv6SourceList"], vport_name, emulation_host, filters)

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
                upperLayer: string (string type: enum  enums: nhEthernet|nhIp)
                txLabelValue: string | list[string] (string type: decimal)
                rxLabelValue: string | list[string] (string type: decimal)
                enablecw: bool
                overridecos: bool
                cos: string | list[string] (string type: decimal)
                bos: string | list[string] (string type: decimal)
                ttl: string | list[string] (string type: decimal)
                destMac: string | list[string] (string type: mac)
                transportType: string (string type: enum  enums: overMac|overTunnel)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnMplsEmulation, self).find(["topology","deviceGroup","ethernet","mpls"], vport_name, emulation_host, filters)

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
                typeAreaId: string (string type: enum  enums: areadid|ip)
                areaId: string | list[string] (string type: decimal)
                areaIdIp: string | list[string] (string type: ipv4)
                networkType: string (string type: enum  enums: pointtopoint|broadcast|pointtomultipoint)
                neighborIp: string | list[string] (string type: ipv4)
                enableBfdRegistration: string | list[string] (string type: bool)
                enableSRLG: string | list[string] (string type: bool)
                srlgCount: number
                enLinkProtection: string | list[string] (string type: bool)
                extraTraffic: string | list[string] (string type: bool)
                unprotected: string | list[string] (string type: bool)
                shared: string | list[string] (string type: bool)
                dedicated1To1: string | list[string] (string type: bool)
                dedicated1Plus1: string | list[string] (string type: bool)
                enhanced: string | list[string] (string type: bool)
                reserved40: string | list[string] (string type: bool)
                reserved80: string | list[string] (string type: bool)
                enableAdjSID: string | list[string] (string type: bool)
                adjSID: string | list[string] (string type: decimal)
                bFlag: string | list[string] (string type: bool)
                vFlag: string | list[string] (string type: bool)
                lFlag: string | list[string] (string type: bool)
                sFlag: string | list[string] (string type: bool)
                weight: string | list[string] (string type: decimal)
                suppressHello: string | list[string] (string type: bool)
                enableFast2wayConvergence: bool
                enableFastHello: string | list[string] (string type: bool)
                helloMultiplier: string | list[string] (string type: decimal)
                helloInterval: string | list[string] (string type: decimal)
                deadInterval: string | list[string] (string type: decimal)
                metric: string | list[string] (string type: decimal)
                validateRxMtu: string | list[string] (string type: bool)
                maxMtu: string | list[string] (string type: decimal)
                priority: string | list[string] (string type: decimal)
                unused: string | list[string] (string type: bool)
                opaqueLsaForwarded: string | list[string] (string type: bool)
                demandCircuit: string | list[string] (string type: bool)
                externalAttribute: string | list[string] (string type: bool)
                nssaCapability: string | list[string] (string type: bool)
                multicastCapability: string | list[string] (string type: bool)
                externalCapability: string | list[string] (string type: bool)
                typeOfServiceRouting: string | list[string] (string type: bool)
                authentication: string (string type: enum  enums: null|password|md5)
                authenticationPassword: string | list[string] (string type: string)
                md5KeyId: string | list[string] (string type: decimal)
                md5Key: string | list[string] (string type: string)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnOspfv2Emulation, self).find(["topology","deviceGroup","ethernet","ipv4","ospfv2"], vport_name, emulation_host, filters)

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
                groupAddress: string | list[string] (string type: ipv4)
                groupMaskLen: string | list[string] (string type: decimal)
                crpAddress: string | list[string] (string type: ipv4)
                localRouterId: list
                groupCount: string | list[string] (string type: decimal)
                meshingType: string (string type: enum  enums: fullymeshed|onetoone)
                crpAddressCount: string | list[string] (string type: decimal)
                periodicAdvertisementInterval: string | list[string] (string type: decimal)
                advertisementHoldTime: string | list[string] (string type: decimal)
                backOffInterval: string | list[string] (string type: decimal)
                triggeredCrpMessageCount: string | list[string] (string type: decimal)
                priority: string | list[string] (string type: decimal)
                priorityType: string (string type: enum  enums: same|incremental|random)
                priorityChangeInterval: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV4CandidateRPsListEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","pimV4Interface","pimV4CandidateRPsList"], vport_name, emulation_host, filters)

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
                v4Neighbor: string | list[string] (string type: ipv4)
                bootstrapHashMaskLength: string | list[string] (string type: decimal)
                localRouterId: list
                helloInterval: string | list[string] (string type: decimal)
                helloHoldTime: string | list[string] (string type: decimal)
                disableTriggered: string | list[string] (string type: bool)
                triggeredHelloDelay: string | list[string] (string type: decimal)
                autoPickNeighbor: string | list[string] (string type: bool)
                joinPrunes: number
                sources: number
                crpRanges: number
                discardLearnedRpInfo: string | list[string] (string type: bool)
                learnSelectedRpSet: string | list[string] (string type: bool)
                enableBootstrap: string | list[string] (string type: bool)
                enableBfdRegistration: string | list[string] (string type: bool)
                enablePrune: string | list[string] (string type: bool)
                pruneDelay: string | list[string] (string type: decimal)
                overrideInterval: string | list[string] (string type: decimal)
                lanPruneTbit: string | list[string] (string type: bool)
                sendGenerationIdOption: string | list[string] (string type: bool)
                sendGenerationMode: string (string type: enum  enums: incremental|random|constant)
                sendBidirectional: string | list[string] (string type: bool)
                bootstrapPriority: string | list[string] (string type: decimal)
                bootstrapInterval: string | list[string] (string type: decimal)
                bootstrapTimeout: string | list[string] (string type: decimal)
                forceSemantic: string | list[string] (string type: bool)
                supportUnicastBsm: string | list[string] (string type: bool)
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnPimV4InterfaceEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","pimV4Interface"], vport_name, emulation_host, filters)

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
                rpV4Address: string | list[string] (string type: ipv4)
                groupV4Address: string | list[string] (string type: ipv4)
                groupV4MaskWidth: string | list[string] (string type: decimal)
                sourceV4Address: string | list[string] (string type: ipv4)
                sourceV4MaskWidth: string | list[string] (string type: decimal)
                pruneSourceV4Address: string | list[string] (string type: ipv4)
                pruneSourceV4MaskWidth: string | list[string] (string type: decimal)
                localRouterId: list
                rangeType: string (string type: enum  enums: startorp|startogroup|sourcetogroup|stargtosourcegroup|registeredtriggered)
                sourceGroupMappingType: string (string type: enum  enums: fullymeshed|onetoone)
                groupAddressCount: string | list[string] (string type: decimal)
                sourceAddressCount: string | list[string] (string type: decimal)
                pruneSourceAddressCount: string | list[string] (string type: decimal)
                registerStopTriggerCount: string | list[string] (string type: decimal)
                enablePack: string | list[string] (string type: bool)
                switchOverInterval: string | list[string] (string type: decimal)
                enableFlapInfo: string | list[string] (string type: bool)
                flapInterval: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV4JoinPruneListEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","pimV4Interface","pimV4JoinPruneList"], vport_name, emulation_host, filters)

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
                groupAddress: string | list[string] (string type: ipv4)
                sourceAddress: string | list[string] (string type: ipv4)
                rpAddress: string | list[string] (string type: ipv4)
                localRouterId: list
                groupCount: string | list[string] (string type: decimal)
                sourceCount: string | list[string] (string type: decimal)
                discardSgJoinStates: string | list[string] (string type: bool)
                sendNullRegAtBegin: string | list[string] (string type: bool)
                multicastDataLength: string | list[string] (string type: decimal)
                txIterationGap: string | list[string] (string type: decimal)
                udpSourcePort: string | list[string] (string type: decimal)
                udpDestinationPort: string | list[string] (string type: decimal)
                switchOverInterval: string | list[string] (string type: decimal)
                supressionTime: string | list[string] (string type: decimal)
                registerProbeTime: string | list[string] (string type: decimal)
                active: string | list[string] (string type: bool)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPimV4SourcesListEmulation, self).find(["topology","deviceGroup","ethernet","ipv4","pimV4Interface","pimV4SourcesList"], vport_name, emulation_host, filters)

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
                papUser: string | list[string] (string type: string)
                papPassword: string | list[string] (string type: string)
                chapName: string | list[string] (string type: string)
                chapSecret: string | list[string] (string type: string)
                enableDomainGroups: string | list[string] (string type: bool)
                domainList: string | list[string] (string type: string)
                name: string
                descriptiveName: string
                count: number
        """
        return super(IxnPppoxServerSessionsEmulation, self).find(["topology","deviceGroup","ethernet","pppoxserver","pppoxServerSessions"], vport_name, emulation_host, filters)

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
                papUser: string | list[string] (string type: string)
                papPassword: string | list[string] (string type: string)
                chapName: string | list[string] (string type: string)
                chapSecret: string | list[string] (string type: string)
                enableDomainGroups: string | list[string] (string type: bool)
                domainList: string | list[string] (string type: string)
                clientNcpOptions: string (string type: enum  enums: learned|request)
                clientLocalIp: string | list[string] (string type: ipv4)
                clientV6NcpOptions: string (string type: enum  enums: learned|request)
                clientLocalIpv6Iid: string | list[string] (string type: ipv6)
                clientDnsOptions: string (string type: enum  enums: request_primary_and_secondary|request_primary_only|accept_addresses_from_server|accept_only_primary_address_from_server|disable_extension)
                clientPrimaryDnsAddress: string | list[string] (string type: ipv4)
                clientSecondaryDnsAddress: string | list[string] (string type: ipv4)
                clientNetmaskOptions: string (string type: enum  enums: request_specific_netmask|accept_netmask_from_server|disable_extension)
                clientNetmask: string | list[string] (string type: ipv4)
                clientWinsOptions: string (string type: enum  enums: request_primaryandsecondary_wins|request_primaryonly_wins|accept_addresses_from_server|accept_only_primary_address_from_server|disable_extension)
                clientWinsPrimaryAddress: string | list[string] (string type: ipv4)
                clientWinsSecondaryAddress: string | list[string] (string type: ipv4)
                padiTimeout: string | list[string] (string type: decimal)
                padiRetries: string | list[string] (string type: decimal)
                padrTimeout: string | list[string] (string type: decimal)
                padrRetries: string | list[string] (string type: decimal)
                serviceName: string | list[string] (string type: string)
                serviceOptions: string (string type: enum  enums: any_service|service_name)
                acOptions: string (string type: enum  enums: use_first_responder|match_ac_name|match_ac_mac)
                acMatchName: string | list[string] (string type: string)
                acMatchMac: string | list[string] (string type: string)
                enableRedial: string | list[string] (string type: bool)
                redialTimeout: string | list[string] (string type: decimal)
                unlimitedRedialAttempts: string | list[string] (string type: bool)
                redialMax: string | list[string] (string type: decimal)
                enableMaxPayload: string | list[string] (string type: bool)
                maxPayload: string | list[string] (string type: decimal)
                enableHostUniq: string | list[string] (string type: bool)
                hostUniq: string | list[string] (string type: hex)
                clientSignalLoopId: string | list[string] (string type: bool)
                agentCircuitId: string | list[string] (string type: string)
                agentRemoteId: string | list[string] (string type: string)
                clientSignalLoopChar: string | list[string] (string type: bool)
                actualRateUpstream: string | list[string] (string type: decimal)
                actualRateDownstream: string | list[string] (string type: decimal)
                clientSignalIWF: string | list[string] (string type: bool)
                clientSignalLoopEncapsulation: string | list[string] (string type: bool)
                dataLink: string (string type: enum  enums: atm_aal5|ethernet)
                encaps1: string (string type: enum  enums: na|untagged_ethernet|single_tagged_ethernet)
                encaps2: string (string type: enum  enums: na|pppoa_llc|pppoa_null|ipoa_llc|ipoa_null|ethernet_over_aal5_llc_w_fcs|ethernet_over_aal5_llc_w_o_fcs|ethernet_over_aal5_null_w_fcs|ethernet_over_aal5_null_w_o_fcs)
                dslTypeTlv: string (string type: enum  enums: none|adsl_1|adsl_2|adsl_2_p|vdsl_1|vdsl_2|sdsl|g_fast|svvdsl|sdsl_bonded|vdsl_bonded|g_fast_bonded|svvdsl_bonded|other|userdefined)
                userDefinedDslType: string | list[string] (string type: decimal)
                mruNegotiation: string | list[string] (string type: bool)
                mtu: string | list[string] (string type: decimal)
                enableEchoRsp: string | list[string] (string type: bool)
                enableEchoReq: string | list[string] (string type: bool)
                echoReqInterval: string | list[string] (string type: decimal)
                lcpTimeout: string | list[string] (string type: decimal)
                lcpRetries: string | list[string] (string type: decimal)
                lcpTermRetries: string | list[string] (string type: decimal)
                lcpEnableAccm: string | list[string] (string type: bool)
                lcpAccm: string | list[string] (string type: hex)
                lcpMaxFailure: string | list[string] (string type: decimal)
                lcpStartDelay: string | list[string] (string type: decimal)
                ncpType: string (string type: enum  enums: ipv4|ipv6|dual_stack)
                ncpTimeout: string | list[string] (string type: decimal)
                ncpRetries: string | list[string] (string type: decimal)
                authType: string (string type: enum  enums: none|pap|chap|pap_or_chap)
                authTimeout: string | list[string] (string type: decimal)
                authRetries: string | list[string] (string type: decimal)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnPppoxclientEmulation, self).find(["topology","deviceGroup","ethernet","pppoxclient"], vport_name, emulation_host, filters)

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
                serverNcpOptions: string (string type: enum  enums: serveronly|clientmay)
                clientBaseIp: string | list[string] (string type: ipv4)
                clientIpIncr: string | list[string] (string type: ipv4)
                serverBaseIp: string | list[string] (string type: ipv4)
                serverIpIncr: string | list[string] (string type: ipv4)
                serverV6NcpOptions: string (string type: enum  enums: serveronly|clientmay)
                clientIID: string | list[string] (string type: kVoid)
                clientIIDIncr: string | list[string] (string type: decimal)
                serverIID: string | list[string] (string type: kVoid)
                serverIIDIncr: string | list[string] (string type: decimal)
                ipv6PoolPrefix: string | list[string] (string type: ipv6)
                ipv6PoolPrefixLen: string | list[string] (string type: decimal)
                ipv6AddrPrefixLen: string | list[string] (string type: decimal)
                enableDnsRa: string | list[string] (string type: bool)
                dnsServerList: string | list[string] (string type: ipv6)
                acceptAnyAuthValue: string | list[string] (string type: bool)
                serverDnsOptions: string (string type: enum  enums: accept_requested_addresses|accept_only_requested_primary_address|supply_primary_and_secondary|supply_primary_only|disable_extension)
                serverPrimaryDnsAddress: string | list[string] (string type: ipv4)
                serverSecondaryDnsAddress: string | list[string] (string type: ipv4)
                serverNetmaskOptions: string (string type: enum  enums: accept_requested_netmask|supply_netmask|disable_extension)
                serverNetmask: string | list[string] (string type: ipv4)
                serverWinsOptions: string (string type: enum  enums: accept_requested_addresses|accept_only_requested_primary_address|supply_primary_and_secondary|supply_primary_only|disable_extension)
                serverWinsPrimaryAddress: string | list[string] (string type: ipv4)
                serverWinsSecondaryAddress: string | list[string] (string type: ipv4)
                serviceName: string | list[string] (string type: string)
                acName: string | list[string] (string type: string)
                enableMaxPayload: string | list[string] (string type: bool)
                serverSignalLoopId: string | list[string] (string type: bool)
                serverSignalLoopChar: string | list[string] (string type: bool)
                serverSignalIWF: string | list[string] (string type: bool)
                serverSignalLoopEncapsulation: string | list[string] (string type: bool)
                serverSignalDslTypeTlv: string | list[string] (string type: bool)
                mruNegotiation: string | list[string] (string type: bool)
                mtu: string | list[string] (string type: decimal)
                enableEchoRsp: string | list[string] (string type: bool)
                enableEchoReq: string | list[string] (string type: bool)
                echoReqInterval: string | list[string] (string type: decimal)
                lcpTimeout: string | list[string] (string type: decimal)
                lcpRetries: string | list[string] (string type: decimal)
                lcpTermRetries: string | list[string] (string type: decimal)
                lcpEnableAccm: string | list[string] (string type: bool)
                lcpAccm: string | list[string] (string type: hex)
                lcpMaxFailure: string | list[string] (string type: decimal)
                lcpStartDelay: string | list[string] (string type: decimal)
                ncpType: string (string type: enum  enums: ipv4|ipv6|dual_stack)
                ncpTimeout: string | list[string] (string type: decimal)
                ncpRetries: string | list[string] (string type: decimal)
                authType: string (string type: enum  enums: none|pap|chap|pap_or_chap)
                authTimeout: string | list[string] (string type: decimal)
                authRetries: string | list[string] (string type: decimal)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnPppoxserverEmulation, self).find(["topology","deviceGroup","ethernet","pppoxserver"], vport_name, emulation_host, filters)

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
                role: string (string type: enum  enums: slave|master)
                customClockId: string | list[string] (string type: bool)
                clockIdentity: string | list[string] (string type: kVoid)
                profile: string (string type: enum  enums: ieee1588|g82651|g82751|ieee8021as)
                oneWay: string | list[string] (string type: bool)
                delayMechanism: string (string type: enum  enums: requestresponse|peerdelay)
                communicationMode: string (string type: enum  enums: multicast|unicast|mixedmode)
                stepMode: string (string type: enum  enums: twostep|singlestep)
                domain: string | list[string] (string type: decimal)
                portNumber: string | list[string] (string type: decimal)
                announceReceiptTimeout: string | list[string] (string type: decimal)
                logAnnounceInterval: string (string type: enum  enums: vneg9_512_per_second_|vneg8_256_per_second_|vneg7_128_per_second_|vneg6_64_per_second_|vneg5_32_per_second_|vneg4_16_per_second_|vneg3_8_per_second_|vneg2_4_per_second_|vneg1_2_per_second_|v0_1_per_second_|v1_1_per_2_seconds_|v2_1_per_4_seconds_|v3_1_per_8_seconds_|v4_1_per_16_seconds_|v5_1_per_32_seconds_|v6_1_per_64_seconds_|v7_1_per_128_seconds_|v8_1_per_256_seconds_|v9_1_per_512_seconds_)
                logSyncInterval: string (string type: enum  enums: vneg9_512_per_second_|vneg8_256_per_second_|vneg7_128_per_second_|vneg6_64_per_second_|vneg5_32_per_second_|vneg4_16_per_second_|vneg3_8_per_second_|vneg2_4_per_second_|vneg1_2_per_second_|v0_1_per_second_|v1_1_per_2_seconds_|v2_1_per_4_seconds_|v3_1_per_8_seconds_|v4_1_per_16_seconds_|v5_1_per_32_seconds_|v6_1_per_64_seconds_|v7_1_per_128_seconds_|v8_1_per_256_seconds_|v9_1_per_512_seconds_)
                logDelayReqInterval: string (string type: enum  enums: vneg9_512_per_second_|vneg8_256_per_second_|vneg7_128_per_second_|vneg6_64_per_second_|vneg5_32_per_second_|vneg4_16_per_second_|vneg3_8_per_second_|vneg2_4_per_second_|vneg1_2_per_second_|v0_1_per_second_|v1_1_per_2_seconds_|v2_1_per_4_seconds_|v3_1_per_8_seconds_|v4_1_per_16_seconds_|v5_1_per_32_seconds_|v6_1_per_64_seconds_|v7_1_per_128_seconds_|v8_1_per_256_seconds_|v9_1_per_512_seconds_)
                strictGrant: string | list[string] (string type: bool)
                pathTraceTLV: string | list[string] (string type: bool)
                priority1: string | list[string] (string type: decimal)
                clockClass: string | list[string] (string type: decimal)
                clockAccuracy: string (string type: enum  enums: the_time_is_accurate_to_within_25_ns|the_time_is_accurate_to_within_100_ns|the_time_is_accurate_to_within_250_ns|the_time_is_accurate_to_within_1_us|the_time_is_accurate_to_within_2_5_us|the_time_is_accurate_to_within_10_us|the_time_is_accurate_to_within_25_us|the_time_is_accurate_to_within_100_us|the_time_is_accurate_to_within_250_us|the_time_is_accurate_to_within_1_ms|the_time_is_accurate_to_within_2_5_ms|the_time_is_accurate_to_within_10_ms|the_time_is_accurate_to_within_25_ms|the_time_is_accurate_to_within_100_ms|the_time_is_accurate_to_within_250_ms|the_time_is_accurate_to_within_1_s|the_time_is_accurate_to_within_10_s|the_time_is_accurate_to_greater_than_10_s|unknown)
                offsetScaledLogVariance: string | list[string] (string type: hex)
                priority2: string | list[string] (string type: decimal)
                timeSource: string (string type: enum  enums: atomicclock|gps|terrestrialradio|ptp|ntp|handset|other|internaloscilator)
                signalUnicastHandling: string (string type: enum  enums: send_individually|send_in_one_message|do_not_send)
                masterMacAddress: string | list[string] (string type: mac)
                masterMacIncrementBy: string | list[string] (string type: mac)
                masterIpAddress: string | list[string] (string type: ipv4)
                masterIpIncrementBy: string | list[string] (string type: ipv4)
                masterIpv6Address: string | list[string] (string type: ipv6)
                masterIpv6IncrementBy: string | list[string] (string type: ipv6)
                masterCount: string | list[string] (string type: decimal)
                slaveMacAddress: string | list[string] (string type: mac)
                slaveMacIncrementBy: string | list[string] (string type: mac)
                slaveIpAddress: string | list[string] (string type: ipv4)
                slaveIpIncrementBy: string | list[string] (string type: ipv4)
                slaveIpv6Address: string | list[string] (string type: ipv6)
                slaveIpv6IncrementBy: string | list[string] (string type: ipv6)
                slaveCount: string | list[string] (string type: decimal)
                handleCancelTlv: string | list[string] (string type: bool)
                handleAnnounceTlv: string | list[string] (string type: bool)
                sendMulticastAnnounce: string | list[string] (string type: bool)
                renewalInvited: string | list[string] (string type: bool)
                learnPortId: string | list[string] (string type: bool)
                signalInterval: string | list[string] (string type: decimal)
                grantUnicastDurationInterval: string | list[string] (string type: decimal)
                grantSyncDurationInterval: string | list[string] (string type: decimal)
                grantDelayRespDurationInterval: string | list[string] (string type: decimal)
                requestInterval: string | list[string] (string type: decimal)
                requestAttempts: string | list[string] (string type: decimal)
                requestHolddown: string | list[string] (string type: decimal)
                syncReceiptTimeout: string | list[string] (string type: decimal)
                delayRespReceiptTimeout: string | list[string] (string type: decimal)
                multicastAddress: string (string type: enum  enums: nonforwardable|forwardable)
                notSlave: string | list[string] (string type: bool)
                dropMalformed: string | list[string] (string type: bool)
                syncReceiptTimeoutgPTP: string | list[string] (string type: decimal)
                bmca: string | list[string] (string type: bool)
                reverseSync: string | list[string] (string type: bool)
                reverseSyncIntervalPercent: string | list[string] (string type: decimal)
                cumulativeScaledRateOffset: string | list[string] (string type: hex)
                gmTimeBaseIndicator: string | list[string] (string type: decimal)
                lastGmPhaseChange: string | list[string] (string type: decimal)
                scaledLastGmFreqChange: string | list[string] (string type: decimal)
                updateTime: string | list[string] (string type: bool)
                timestampOffset: string | list[string] (string type: decimal)
                nanosecondsPerSecond: string | list[string] (string type: decimal)
                txCalibration: string | list[string] (string type: decimal)
                txTwoStepCalibration: string | list[string] (string type: decimal)
                rxCalibration: string | list[string] (string type: decimal)
                alternateMasterFlag: string | list[string] (string type: bool)
                announceTimeTraceable: string | list[string] (string type: bool)
                announceFrequencyTraceable: string | list[string] (string type: bool)
                announceLeap59: string | list[string] (string type: bool)
                announceLeap61: string | list[string] (string type: bool)
                announceCurrentUtcOffsetValid: string | list[string] (string type: bool)
                currentUtcOffset: string | list[string] (string type: decimal)
                announcePtpTimescale: string | list[string] (string type: bool)
                simulateBoundary: string | list[string] (string type: bool)
                grandmasterIdentity: string | list[string] (string type: kVoid)
                stepsRemoved: string | list[string] (string type: decimal)
                simulateTransparent: string | list[string] (string type: bool)
                syncResidenceTime: string | list[string] (string type: decimal)
                followUpResidenceTime: string | list[string] (string type: decimal)
                delayReqResidenceTime: string | list[string] (string type: decimal)
                delayRespResidenceTime: string | list[string] (string type: decimal)
                pDelayFollowUpResidenceTime: string | list[string] (string type: decimal)
                announceDropRate: string | list[string] (string type: decimal)
                syncDropRate: string | list[string] (string type: decimal)
                followUpDelay: string | list[string] (string type: decimal)
                followUpDelayInsertionRate: string | list[string] (string type: decimal)
                followUpDropRate: string | list[string] (string type: decimal)
                followUpBadCrcRate: string | list[string] (string type: decimal)
                delayReqDropRate: string | list[string] (string type: decimal)
                delayReqOffset: string | list[string] (string type: decimalFixed2)
                delayReqSpread: string | list[string] (string type: decimalFixed2)
                delayResponseDelay: string | list[string] (string type: decimal)
                delayResponseDelayInsertionRate: string | list[string] (string type: decimal)
                delayRespDropRate: string | list[string] (string type: decimal)
                pDelayFollowUpDelay: string | list[string] (string type: decimal)
                pDelayFollowUpDelayInsertionRate: string | list[string] (string type: decimal)
                pDelayFollowUpDropRate: string | list[string] (string type: decimal)
                dropSignalReqAnnounce: string | list[string] (string type: bool)
                dropSignalReqSync: string | list[string] (string type: bool)
                dropSignalReqDelayResp: string | list[string] (string type: bool)
                enableNegativeTesting: bool
                frequency: number
                numberOFMsgs: number
                avnuMode: string (string type: enum  enums: aVNU_GPTP|aVNU_NA)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnPtpEmulation, self).find(["topology","deviceGroup","ethernet","ptp"], vport_name, emulation_host, filters)

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
                lagId: string | list[string] (string type: decimal)
                portData: href
                active: string | list[string] (string type: bool)
                multiplier: number
                stackedLayers: list
                name: string
                descriptiveName: string
                count: number
                status: string (string type: enum  enums: error|mixed|notStarted|started|starting|stopping)
                errors: list
        """
        return super(IxnStaticLagEmulation, self).find(["topology","deviceGroup","ethernet","staticLag"], vport_name, emulation_host, filters)

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


