from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers


import pybindgen.settings
import warnings

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        warnings.warn("exception %r in wrapper %s" % (exception, wrapper))
        return True
pybindgen.settings.error_handler = ErrorHandler()


import sys

def module_init():
    root_module = Module('ns.wimax', cpp_namespace='::ns3')
    return root_module

def register_types(module):
    root_module = module.get_root()
    
    
    module.add_enum('ReqType', ['DATA', 'UNICAST_POLLING'])
    
    module.add_enum('LogLevel', ['LOG_NONE', 'LOG_ERROR', 'LOG_LEVEL_ERROR', 'LOG_WARN', 'LOG_LEVEL_WARN', 'LOG_DEBUG', 'LOG_LEVEL_DEBUG', 'LOG_INFO', 'LOG_LEVEL_INFO', 'LOG_FUNCTION', 'LOG_LEVEL_FUNCTION', 'LOG_LOGIC', 'LOG_LEVEL_LOGIC', 'LOG_ALL', 'LOG_LEVEL_ALL', 'LOG_PREFIX_FUNC', 'LOG_PREFIX_TIME', 'LOG_PREFIX_NODE'], import_from_module='ns.core')
    
    module.add_class('Address', import_from_module='ns.network')
    
    module.add_enum('MaxSize_e', ['MAX_SIZE'], outer_class=root_module['ns3::Address'], import_from_module='ns.network')
    
    module.add_class('AsciiTraceHelper', import_from_module='ns.network')
    
    module.add_class('AsciiTraceHelperForDevice', allow_subclassing=True, import_from_module='ns.network')
    
    module.add_class('AttributeConstructionList', import_from_module='ns.core')
    
    module.add_class('Item', import_from_module='ns.core', outer_class=root_module['ns3::AttributeConstructionList'])
    
    module.add_class('Buffer', import_from_module='ns.network')
    
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::Buffer'])
    
    module.add_class('ByteTagIterator', import_from_module='ns.network')
    
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagIterator'])
    
    module.add_class('ByteTagList', import_from_module='ns.network')
    
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList'])
    
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList::Iterator'])
    
    module.add_class('CallbackBase', import_from_module='ns.core')
    
    module.add_class('Cid')
    
    module.add_enum('Type', ['BROADCAST', 'INITIAL_RANGING', 'BASIC', 'PRIMARY', 'TRANSPORT', 'MULTICAST', 'PADDING'], outer_class=root_module['ns3::Cid'])
    
    module.add_class('CidFactory')
    
    module.add_class('CsParameters')
    
    module.add_enum('Action', ['ADD', 'REPLACE', 'DELETE'], outer_class=root_module['ns3::CsParameters'])
    
    module.add_class('DcdChannelEncodings', allow_subclassing=True)
    
    module.add_class('DlFramePrefixIe')
    
    module.add_class('EventId', import_from_module='ns.core')
    
    module.add_class('IpcsClassifierRecord')
    
    module.add_class('Ipv4Address', import_from_module='ns.network')
    
    root_module['ns3::Ipv4Address'].implicitly_converts_to(root_module['ns3::Address'])
    
    module.add_class('Ipv4Mask', import_from_module='ns.network')
    
    module.add_class('Ipv6Address', import_from_module='ns.network')
    
    root_module['ns3::Ipv6Address'].implicitly_converts_to(root_module['ns3::Address'])
    
    module.add_class('Ipv6Prefix', import_from_module='ns.network')
    
    module.add_class('LogComponent', import_from_module='ns.core')
    
    module.add_class('Mac48Address', import_from_module='ns.network')
    
    root_module['ns3::Mac48Address'].implicitly_converts_to(root_module['ns3::Address'])
    
    module.add_class('NetDeviceContainer', import_from_module='ns.network')
    
    module.add_class('NodeContainer', import_from_module='ns.network')
    
    module.add_class('ObjectBase', allow_subclassing=True, import_from_module='ns.core')
    
    module.add_class('ObjectDeleter', import_from_module='ns.core')
    
    module.add_class('ObjectFactory', import_from_module='ns.core')
    
    module.add_class('OfdmDcdChannelEncodings', parent=root_module['ns3::DcdChannelEncodings'])
    
    module.add_class('OfdmDlBurstProfile')
    
    module.add_enum('Diuc', ['DIUC_STC_ZONE', 'DIUC_BURST_PROFILE_1', 'DIUC_BURST_PROFILE_2', 'DIUC_BURST_PROFILE_3', 'DIUC_BURST_PROFILE_4', 'DIUC_BURST_PROFILE_5', 'DIUC_BURST_PROFILE_6', 'DIUC_BURST_PROFILE_7', 'DIUC_BURST_PROFILE_8', 'DIUC_BURST_PROFILE_9', 'DIUC_BURST_PROFILE_10', 'DIUC_BURST_PROFILE_11', 'DIUC_GAP', 'DIUC_END_OF_MAP'], outer_class=root_module['ns3::OfdmDlBurstProfile'])
    
    module.add_class('OfdmDlMapIe')
    
    module.add_class('OfdmUlBurstProfile')
    
    module.add_enum('Uiuc', ['UIUC_INITIAL_RANGING', 'UIUC_REQ_REGION_FULL', 'UIUC_REQ_REGION_FOCUSED', 'UIUC_FOCUSED_CONTENTION_IE', 'UIUC_BURST_PROFILE_5', 'UIUC_BURST_PROFILE_6', 'UIUC_BURST_PROFILE_7', 'UIUC_BURST_PROFILE_8', 'UIUC_BURST_PROFILE_9', 'UIUC_BURST_PROFILE_10', 'UIUC_BURST_PROFILE_11', 'UIUC_BURST_PROFILE_12', 'UIUC_SUBCH_NETWORK_ENTRY', 'UIUC_END_OF_MAP'], outer_class=root_module['ns3::OfdmUlBurstProfile'])
    
    module.add_class('OfdmUlMapIe')
    
    module.add_class('PacketMetadata', import_from_module='ns.network')
    
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    
    module.add_enum('', ['PAYLOAD', 'HEADER', 'TRAILER'], outer_class=root_module['ns3::PacketMetadata::Item'], import_from_module='ns.network')
    
    module.add_class('ItemIterator', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    
    module.add_class('PacketTagIterator', import_from_module='ns.network')
    
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagIterator'])
    
    module.add_class('PacketTagList', import_from_module='ns.network')
    
    module.add_class('TagData', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagList'])
    
    module.add_class('PcapFile', import_from_module='ns.network')
    
    module.add_class('PcapHelper', import_from_module='ns.network')
    
    module.add_enum('', ['DLT_NULL', 'DLT_EN10MB', 'DLT_PPP', 'DLT_RAW', 'DLT_IEEE802_11', 'DLT_PRISM_HEADER', 'DLT_IEEE802_11_RADIO'], outer_class=root_module['ns3::PcapHelper'], import_from_module='ns.network')
    
    module.add_class('PcapHelperForDevice', allow_subclassing=True, import_from_module='ns.network')
    
    module.add_class('RandomVariable', import_from_module='ns.core')
    
    module.add_class('SNRToBlockErrorRateManager')
    
    module.add_class('SNRToBlockErrorRateRecord')
    
    module.add_class('SSRecord')
    
    module.add_class('SeedManager', import_from_module='ns.core')
    
    module.add_class('SendParams')
    
    module.add_class('SequentialVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('ServiceFlow')
    
    module.add_enum('Direction', ['SF_DIRECTION_DOWN', 'SF_DIRECTION_UP'], outer_class=root_module['ns3::ServiceFlow'])
    
    module.add_enum('Type', ['SF_TYPE_PROVISIONED', 'SF_TYPE_ADMITTED', 'SF_TYPE_ACTIVE'], outer_class=root_module['ns3::ServiceFlow'])
    
    module.add_enum('SchedulingType', ['SF_TYPE_NONE', 'SF_TYPE_UNDEF', 'SF_TYPE_BE', 'SF_TYPE_NRTPS', 'SF_TYPE_RTPS', 'SF_TYPE_UGS', 'SF_TYPE_ALL'], outer_class=root_module['ns3::ServiceFlow'])
    
    module.add_enum('CsSpecification', ['ATM', 'IPV4', 'IPV6', 'ETHERNET', 'VLAN', 'IPV4_OVER_ETHERNET', 'IPV6_OVER_ETHERNET', 'IPV4_OVER_VLAN', 'IPV6_OVER_VLAN'], outer_class=root_module['ns3::ServiceFlow'])
    
    module.add_enum('ModulationType', ['MODULATION_TYPE_BPSK_12', 'MODULATION_TYPE_QPSK_12', 'MODULATION_TYPE_QPSK_34', 'MODULATION_TYPE_QAM16_12', 'MODULATION_TYPE_QAM16_34', 'MODULATION_TYPE_QAM64_23', 'MODULATION_TYPE_QAM64_34'], outer_class=root_module['ns3::ServiceFlow'])
    
    module.add_class('ServiceFlowRecord')
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Object', 'ns3::ObjectBase', 'ns3::ObjectDeleter'], parent=root_module['ns3::ObjectBase'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('Simulator', destructor_visibility='private', import_from_module='ns.core')
    
    module.add_class('Tag', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    
    module.add_class('TagBuffer', import_from_module='ns.network')
    
    module.add_class('TlvValue', allow_subclassing=True)
    
    module.add_class('TosTlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('TriangularVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('TypeId', import_from_module='ns.core')
    
    module.add_enum('AttributeFlag', ['ATTR_GET', 'ATTR_SET', 'ATTR_CONSTRUCT', 'ATTR_SGC'], outer_class=root_module['ns3::TypeId'], import_from_module='ns.core')
    
    module.add_class('AttributeInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    
    module.add_class('TraceSourceInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    
    module.add_class('U16TlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('U32TlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('U8TlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('UcdChannelEncodings', allow_subclassing=True)
    
    module.add_class('UniformVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('VectorTlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('WeibullVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('WimaxHelper', parent=[root_module['ns3::PcapHelperForDevice'], root_module['ns3::AsciiTraceHelperForDevice']])
    
    module.add_enum('NetDeviceType', ['DEVICE_TYPE_SUBSCRIBER_STATION', 'DEVICE_TYPE_BASE_STATION'], outer_class=root_module['ns3::WimaxHelper'])
    
    module.add_enum('PhyType', ['SIMPLE_PHY_TYPE_OFDM'], outer_class=root_module['ns3::WimaxHelper'])
    
    module.add_enum('SchedulerType', ['SCHED_TYPE_SIMPLE', 'SCHED_TYPE_RTPS', 'SCHED_TYPE_MBQOS'], outer_class=root_module['ns3::WimaxHelper'])
    
    module.add_class('ZetaVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('ZipfVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('empty', import_from_module='ns.core')
    
    module.add_class('int64x64_t', import_from_module='ns.core')
    
    module.add_class('simpleOfdmSendParam')
    
    module.add_class('Chunk', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    
    module.add_class('ClassificationRuleVectorTlvValue', parent=root_module['ns3::VectorTlvValue'])
    
    module.add_enum('ClassificationRuleTlvType', ['Priority', 'ToS', 'Protocol', 'IP_src', 'IP_dst', 'Port_src', 'Port_dst', 'Index'], outer_class=root_module['ns3::ClassificationRuleVectorTlvValue'])
    
    module.add_class('ConstantVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('CsParamVectorTlvValue', parent=root_module['ns3::VectorTlvValue'])
    
    module.add_enum('Type', ['Classifier_DSC_Action', 'Packet_Classification_Rule'], outer_class=root_module['ns3::CsParamVectorTlvValue'])
    
    module.add_class('DeterministicVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('EmpiricalVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('ErlangVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('ExponentialVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('GammaVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('Header', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    
    module.add_class('IntEmpiricalVariable', import_from_module='ns.core', parent=root_module['ns3::EmpiricalVariable'])
    
    module.add_class('Ipv4AddressTlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('ipv4Addr', outer_class=root_module['ns3::Ipv4AddressTlvValue'])
    
    module.add_class('LogNormalVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('MacHeaderType', parent=root_module['ns3::Header'])
    
    module.add_enum('HeaderType', ['HEADER_TYPE_GENERIC', 'HEADER_TYPE_BANDWIDTH'], outer_class=root_module['ns3::MacHeaderType'])
    
    module.add_class('ManagementMessageType', parent=root_module['ns3::Header'])
    
    module.add_enum('MessageType', ['MESSAGE_TYPE_UCD', 'MESSAGE_TYPE_DCD', 'MESSAGE_TYPE_DL_MAP', 'MESSAGE_TYPE_UL_MAP', 'MESSAGE_TYPE_RNG_REQ', 'MESSAGE_TYPE_RNG_RSP', 'MESSAGE_TYPE_REG_REQ', 'MESSAGE_TYPE_REG_RSP', 'MESSAGE_TYPE_DSA_REQ', 'MESSAGE_TYPE_DSA_RSP', 'MESSAGE_TYPE_DSA_ACK'], outer_class=root_module['ns3::ManagementMessageType'])
    
    module.add_class('NormalVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('Object', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    
    module.add_class('AggregateIterator', import_from_module='ns.core', outer_class=root_module['ns3::Object'])
    
    module.add_class('OfdmDownlinkFramePrefix', parent=root_module['ns3::Header'])
    
    module.add_class('OfdmSendParams', parent=root_module['ns3::SendParams'])
    
    module.add_class('OfdmUcdChannelEncodings', parent=root_module['ns3::UcdChannelEncodings'])
    
    module.add_class('PacketBurst', import_from_module='ns.network', parent=root_module['ns3::Object'])
    
    module.add_class('ParetoVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariable'])
    
    module.add_class('PcapFileWrapper', import_from_module='ns.network', parent=root_module['ns3::Object'])
    
    module.add_class('PortRangeTlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('PortRange', outer_class=root_module['ns3::PortRangeTlvValue'])
    
    module.add_class('PriorityUlJob', parent=root_module['ns3::Object'])
    
    module.add_class('PropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::Object'])
    
    module.add_class('ProtocolTlvValue', parent=root_module['ns3::TlvValue'])
    
    module.add_class('RandomPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('RangePropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('RngReq', parent=root_module['ns3::Header'])
    
    module.add_class('RngRsp', parent=root_module['ns3::Header'])
    
    module.add_class('SSManager', parent=root_module['ns3::Object'])
    
    module.add_class('ServiceFlowManager', parent=root_module['ns3::Object'])
    
    module.add_enum('ConfirmationCode', ['CONFIRMATION_CODE_SUCCESS', 'CONFIRMATION_CODE_REJECT'], outer_class=root_module['ns3::ServiceFlowManager'])
    
    module.add_class('SfVectorTlvValue', parent=root_module['ns3::VectorTlvValue'])
    
    module.add_enum('Type', ['SFID', 'CID', 'Service_Class_Name', 'reserved1', 'QoS_Parameter_Set_Type', 'Traffic_Priority', 'Maximum_Sustained_Traffic_Rate', 'Maximum_Traffic_Burst', 'Minimum_Reserved_Traffic_Rate', 'Minimum_Tolerable_Traffic_Rate', 'Service_Flow_Scheduling_Type', 'Request_Transmission_Policy', 'Tolerated_Jitter', 'Maximum_Latency', 'Fixed_length_versus_Variable_length_SDU_Indicator', 'SDU_Size', 'Target_SAID', 'ARQ_Enable', 'ARQ_WINDOW_SIZE', 'ARQ_RETRY_TIMEOUT_Transmitter_Delay', 'ARQ_RETRY_TIMEOUT_Receiver_Delay', 'ARQ_BLOCK_LIFETIME', 'ARQ_SYNC_LOSS', 'ARQ_DELIVER_IN_ORDER', 'ARQ_PURGE_TIMEOUT', 'ARQ_BLOCK_SIZE', 'reserved2', 'CS_Specification', 'IPV4_CS_Parameters'], outer_class=root_module['ns3::SfVectorTlvValue'])
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeChecker', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeChecker>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeValue', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeValue>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::CallbackImplBase', 'ns3::empty', 'ns3::DefaultDeleter<ns3::CallbackImplBase>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::EventImpl', 'ns3::empty', 'ns3::DefaultDeleter<ns3::EventImpl>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::NixVector', 'ns3::empty', 'ns3::DefaultDeleter<ns3::NixVector>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::OutputStreamWrapper', 'ns3::empty', 'ns3::DefaultDeleter<ns3::OutputStreamWrapper>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Packet', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Packet>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::TraceSourceAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::TraceSourceAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    
    module.add_class('SsServiceFlowManager', parent=root_module['ns3::ServiceFlowManager'])
    
    module.add_enum('ConfirmationCode', ['CONFIRMATION_CODE_SUCCESS', 'CONFIRMATION_CODE_REJECT'], outer_class=root_module['ns3::SsServiceFlowManager'])
    
    module.add_class('ThreeLogDistancePropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('Time', import_from_module='ns.core')
    
    module.add_enum('Unit', ['S', 'MS', 'US', 'NS', 'PS', 'FS', 'LAST'], outer_class=root_module['ns3::Time'], import_from_module='ns.core')
    
    root_module['ns3::Time'].implicitly_converts_to(root_module['ns3::int64x64_t'])
    
    module.add_class('Tlv', parent=root_module['ns3::Header'])
    
    module.add_enum('CommonTypes', ['HMAC_TUPLE', 'MAC_VERSION_ENCODING', 'CURRENT_TRANSMIT_POWER', 'DOWNLINK_SERVICE_FLOW', 'UPLINK_SERVICE_FLOW', 'VENDOR_ID_EMCODING', 'VENDOR_SPECIFIC_INFORMATION'], outer_class=root_module['ns3::Tlv'])
    
    module.add_class('TraceSourceAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    
    module.add_class('Trailer', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    
    module.add_class('TwoRayGroundPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('Ucd', parent=root_module['ns3::Header'])
    
    module.add_class('UlJob', parent=root_module['ns3::Object'])
    
    module.add_enum('JobPriority', ['LOW', 'INTERMEDIATE', 'HIGH'], outer_class=root_module['ns3::UlJob'])
    
    module.add_class('UlMap', parent=root_module['ns3::Header'])
    
    module.add_class('UplinkScheduler', parent=root_module['ns3::Object'])
    
    module.add_class('UplinkSchedulerMBQoS', parent=root_module['ns3::UplinkScheduler'])
    
    module.add_class('UplinkSchedulerRtps', parent=root_module['ns3::UplinkScheduler'])
    
    module.add_class('UplinkSchedulerSimple', parent=root_module['ns3::UplinkScheduler'])
    
    module.add_class('WimaxConnection', parent=root_module['ns3::Object'])
    
    module.add_class('WimaxMacQueue', parent=root_module['ns3::Object'])
    
    module.add_class('WimaxMacToMacHeader', parent=root_module['ns3::Header'])
    
    module.add_class('WimaxPhy', parent=root_module['ns3::Object'])
    
    module.add_enum('ModulationType', ['MODULATION_TYPE_BPSK_12', 'MODULATION_TYPE_QPSK_12', 'MODULATION_TYPE_QPSK_34', 'MODULATION_TYPE_QAM16_12', 'MODULATION_TYPE_QAM16_34', 'MODULATION_TYPE_QAM64_23', 'MODULATION_TYPE_QAM64_34'], outer_class=root_module['ns3::WimaxPhy'])
    
    module.add_enum('PhyState', ['PHY_STATE_IDLE', 'PHY_STATE_SCANNING', 'PHY_STATE_TX', 'PHY_STATE_RX'], outer_class=root_module['ns3::WimaxPhy'])
    
    module.add_enum('PhyType', ['SimpleWimaxPhy', 'simpleOfdmWimaxPhy'], outer_class=root_module['ns3::WimaxPhy'])
    
    module.add_class('AttributeAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    
    module.add_class('AttributeChecker', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    
    module.add_class('AttributeValue', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    
    module.add_class('BSScheduler', parent=root_module['ns3::Object'])
    
    module.add_class('BSSchedulerRtps', parent=root_module['ns3::BSScheduler'])
    
    module.add_class('BSSchedulerSimple', parent=root_module['ns3::BSScheduler'])
    
    module.add_class('BandwidthRequestHeader', parent=root_module['ns3::Header'])
    
    module.add_enum('HeaderType', ['HEADER_TYPE_INCREMENTAL', 'HEADER_TYPE_AGGREGATE'], outer_class=root_module['ns3::BandwidthRequestHeader'])
    
    module.add_class('BsServiceFlowManager', parent=root_module['ns3::ServiceFlowManager'])
    
    module.add_enum('ConfirmationCode', ['CONFIRMATION_CODE_SUCCESS', 'CONFIRMATION_CODE_REJECT'], outer_class=root_module['ns3::BsServiceFlowManager'])
    
    module.add_class('CallbackChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('CallbackImplBase', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    
    module.add_class('CallbackValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('Channel', import_from_module='ns.network', parent=root_module['ns3::Object'])
    
    module.add_class('ConnectionManager', parent=root_module['ns3::Object'])
    
    module.add_class('Dcd', parent=root_module['ns3::Header'])
    
    module.add_class('DlMap', parent=root_module['ns3::Header'])
    
    module.add_class('DsaAck', parent=root_module['ns3::Header'])
    
    module.add_class('DsaReq', parent=root_module['ns3::Header'])
    
    module.add_class('DsaRsp', parent=root_module['ns3::Header'])
    
    module.add_class('EmptyAttributeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('EventImpl', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    
    module.add_class('FixedRssLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('FragmentationSubheader', parent=root_module['ns3::Header'])
    
    module.add_class('FriisPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('GenericMacHeader', parent=root_module['ns3::Header'])
    
    module.add_class('GrantManagementSubheader', parent=root_module['ns3::Header'])
    
    module.add_class('IpcsClassifier', parent=root_module['ns3::Object'])
    
    module.add_class('Ipv4AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('Ipv4AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('Ipv4MaskChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('Ipv4MaskValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('Ipv6AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('Ipv6AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('Ipv6PrefixChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('Ipv6PrefixValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('LogDistancePropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('Mac48AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('Mac48AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('MatrixPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('NakagamiPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    
    module.add_class('NetDevice', import_from_module='ns.network', parent=root_module['ns3::Object'])
    
    module.add_enum('PacketType', ['PACKET_HOST', 'NS3_PACKET_HOST', 'PACKET_BROADCAST', 'NS3_PACKET_BROADCAST', 'PACKET_MULTICAST', 'NS3_PACKET_MULTICAST', 'PACKET_OTHERHOST', 'NS3_PACKET_OTHERHOST'], outer_class=root_module['ns3::NetDevice'], import_from_module='ns.network')
    
    module.add_class('NixVector', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    
    module.add_class('Node', import_from_module='ns.network', parent=root_module['ns3::Object'])
    
    module.add_class('ObjectFactoryChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('ObjectFactoryValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('OutputStreamWrapper', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >'])
    
    module.add_class('Packet', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    
    module.add_class('RandomVariableChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('RandomVariableValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('SimpleOfdmWimaxPhy', parent=root_module['ns3::WimaxPhy'])
    
    module.add_enum('FrameDurationCode', ['FRAME_DURATION_2_POINT_5_MS', 'FRAME_DURATION_4_MS', 'FRAME_DURATION_5_MS', 'FRAME_DURATION_8_MS', 'FRAME_DURATION_10_MS', 'FRAME_DURATION_12_POINT_5_MS', 'FRAME_DURATION_20_MS'], outer_class=root_module['ns3::SimpleOfdmWimaxPhy'])
    
    module.add_class('TimeChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('TimeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('TypeIdChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('TypeIdValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('UintegerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('WimaxChannel', parent=root_module['ns3::Channel'])
    
    module.add_class('WimaxNetDevice', parent=root_module['ns3::NetDevice'])
    
    module.add_enum('Direction', ['DIRECTION_DOWNLINK', 'DIRECTION_UPLINK'], outer_class=root_module['ns3::WimaxNetDevice'])
    
    module.add_enum('RangingStatus', ['RANGING_STATUS_EXPIRED', 'RANGING_STATUS_CONTINUE', 'RANGING_STATUS_ABORT', 'RANGING_STATUS_SUCCESS'], outer_class=root_module['ns3::WimaxNetDevice'])
    
    module.add_class('AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    
    module.add_class('AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    
    module.add_class('BaseStationNetDevice', parent=root_module['ns3::WimaxNetDevice'])
    
    module.add_enum('State', ['BS_STATE_DL_SUB_FRAME', 'BS_STATE_UL_SUB_FRAME', 'BS_STATE_TTG', 'BS_STATE_RTG'], outer_class=root_module['ns3::BaseStationNetDevice'])
    
    module.add_enum('MacPreamble', ['SHORT_PREAMBLE', 'LONG_PREAMBLE'], outer_class=root_module['ns3::BaseStationNetDevice'])
    
    module.add_class('SimpleOfdmWimaxChannel', parent=root_module['ns3::WimaxChannel'])
    
    module.add_enum('PropModel', ['RANDOM_PROPAGATION', 'FRIIS_PROPAGATION', 'LOG_DISTANCE_PROPAGATION', 'COST231_PROPAGATION'], outer_class=root_module['ns3::SimpleOfdmWimaxChannel'])
    
    module.add_class('SubscriberStationNetDevice', parent=root_module['ns3::WimaxNetDevice'])
    
    module.add_enum('State', ['SS_STATE_IDLE', 'SS_STATE_SCANNING', 'SS_STATE_SYNCHRONIZING', 'SS_STATE_ACQUIRING_PARAMETERS', 'SS_STATE_WAITING_REG_RANG_INTRVL', 'SS_STATE_WAITING_INV_RANG_INTRVL', 'SS_STATE_WAITING_RNG_RSP', 'SS_STATE_ADJUSTING_PARAMETERS', 'SS_STATE_REGISTERED', 'SS_STATE_TRANSMITTING', 'SS_STATE_STOPPED'], outer_class=root_module['ns3::SubscriberStationNetDevice'])
    
    module.add_enum('EventType', ['EVENT_NONE', 'EVENT_WAIT_FOR_RNG_RSP', 'EVENT_DL_MAP_SYNC_TIMEOUT', 'EVENT_LOST_DL_MAP', 'EVENT_LOST_UL_MAP', 'EVENT_DCD_WAIT_TIMEOUT', 'EVENT_UCD_WAIT_TIMEOUT', 'EVENT_RANG_OPP_WAIT_TIMEOUT'], outer_class=root_module['ns3::SubscriberStationNetDevice'])
    module.add_container('std::vector< ns3::ServiceFlow * >', 'ns3::ServiceFlow *', container_type='vector')
    module.add_container('std::vector< bool >', 'bool', container_type='vector')
    module.add_container('ns3::bvec', 'bool', container_type='vector')
    module.add_container('std::vector< ns3::DlFramePrefixIe >', 'ns3::DlFramePrefixIe', container_type='vector')
    module.add_container('std::list< ns3::Ptr< ns3::Packet > >', 'ns3::Ptr< ns3::Packet >', container_type='list')
    module.add_container('std::vector< ns3::SSRecord * >', 'ns3::SSRecord *', container_type='vector')
    module.add_container('std::vector< ns3::OfdmUlBurstProfile >', 'ns3::OfdmUlBurstProfile', container_type='vector')
    module.add_container('std::list< ns3::OfdmUlMapIe >', 'ns3::OfdmUlMapIe', container_type='list')
    module.add_container('std::list< ns3::Ptr< ns3::UlJob > >', 'ns3::Ptr< ns3::UlJob >', container_type='list')
    module.add_container('std::list< ns3::Ptr< ns3::Packet const > >', 'ns3::Ptr< ns3::Packet const >', container_type='list')
    module.add_container('std::deque< ns3::WimaxMacQueue::QueueElement >', 'ns3::WimaxMacQueue::QueueElement', container_type='dequeue')
    module.add_container('std::list< std::pair< ns3::OfdmDlMapIe *, ns3::Ptr< ns3::PacketBurst > > >', 'std::pair< ns3::OfdmDlMapIe *, ns3::Ptr< ns3::PacketBurst > >', container_type='list')
    module.add_container('std::vector< ns3::Ptr< ns3::WimaxConnection > >', 'ns3::Ptr< ns3::WimaxConnection >', container_type='vector')
    module.add_container('std::vector< ns3::OfdmDlBurstProfile >', 'ns3::OfdmDlBurstProfile', container_type='vector')
    module.add_container('std::list< ns3::OfdmDlMapIe >', 'ns3::OfdmDlMapIe', container_type='list')
    typehandlers.add_type_alias('void ( * ) ( std::ostream & ) *', 'ns3::LogNodePrinter')
    typehandlers.add_type_alias('void ( * ) ( std::ostream & ) **', 'ns3::LogNodePrinter*')
    typehandlers.add_type_alias('void ( * ) ( std::ostream & ) *&', 'ns3::LogNodePrinter&')
    typehandlers.add_type_alias('void ( * ) ( std::ostream & ) *', 'ns3::LogTimePrinter')
    typehandlers.add_type_alias('void ( * ) ( std::ostream & ) **', 'ns3::LogTimePrinter*')
    typehandlers.add_type_alias('void ( * ) ( std::ostream & ) *&', 'ns3::LogTimePrinter&')
    typehandlers.add_type_alias('std::vector< bool, std::allocator< bool > >', 'ns3::bvec')
    typehandlers.add_type_alias('std::vector< bool, std::allocator< bool > >*', 'ns3::bvec*')
    typehandlers.add_type_alias('std::vector< bool, std::allocator< bool > >&', 'ns3::bvec&')
    
    
    
    nested_module = module.add_cpp_namespace('FatalImpl')
    register_types_ns3_FatalImpl(nested_module)
    
    
    
    
    nested_module = module.add_cpp_namespace('internal')
    register_types_ns3_internal(nested_module)
    

def register_types_ns3_FatalImpl(module):
    root_module = module.get_root()
    

def register_types_ns3_internal(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    register_Ns3Address_methods(root_module, root_module['ns3::Address'])
    register_Ns3AsciiTraceHelper_methods(root_module, root_module['ns3::AsciiTraceHelper'])
    register_Ns3AsciiTraceHelperForDevice_methods(root_module, root_module['ns3::AsciiTraceHelperForDevice'])
    register_Ns3AttributeConstructionList_methods(root_module, root_module['ns3::AttributeConstructionList'])
    register_Ns3AttributeConstructionListItem_methods(root_module, root_module['ns3::AttributeConstructionList::Item'])
    register_Ns3Buffer_methods(root_module, root_module['ns3::Buffer'])
    register_Ns3BufferIterator_methods(root_module, root_module['ns3::Buffer::Iterator'])
    register_Ns3ByteTagIterator_methods(root_module, root_module['ns3::ByteTagIterator'])
    register_Ns3ByteTagIteratorItem_methods(root_module, root_module['ns3::ByteTagIterator::Item'])
    register_Ns3ByteTagList_methods(root_module, root_module['ns3::ByteTagList'])
    register_Ns3ByteTagListIterator_methods(root_module, root_module['ns3::ByteTagList::Iterator'])
    register_Ns3ByteTagListIteratorItem_methods(root_module, root_module['ns3::ByteTagList::Iterator::Item'])
    register_Ns3CallbackBase_methods(root_module, root_module['ns3::CallbackBase'])
    register_Ns3Cid_methods(root_module, root_module['ns3::Cid'])
    register_Ns3CidFactory_methods(root_module, root_module['ns3::CidFactory'])
    register_Ns3CsParameters_methods(root_module, root_module['ns3::CsParameters'])
    register_Ns3DcdChannelEncodings_methods(root_module, root_module['ns3::DcdChannelEncodings'])
    register_Ns3DlFramePrefixIe_methods(root_module, root_module['ns3::DlFramePrefixIe'])
    register_Ns3EventId_methods(root_module, root_module['ns3::EventId'])
    register_Ns3IpcsClassifierRecord_methods(root_module, root_module['ns3::IpcsClassifierRecord'])
    register_Ns3Ipv4Address_methods(root_module, root_module['ns3::Ipv4Address'])
    register_Ns3Ipv4Mask_methods(root_module, root_module['ns3::Ipv4Mask'])
    register_Ns3Ipv6Address_methods(root_module, root_module['ns3::Ipv6Address'])
    register_Ns3Ipv6Prefix_methods(root_module, root_module['ns3::Ipv6Prefix'])
    register_Ns3LogComponent_methods(root_module, root_module['ns3::LogComponent'])
    register_Ns3Mac48Address_methods(root_module, root_module['ns3::Mac48Address'])
    register_Ns3NetDeviceContainer_methods(root_module, root_module['ns3::NetDeviceContainer'])
    register_Ns3NodeContainer_methods(root_module, root_module['ns3::NodeContainer'])
    register_Ns3ObjectBase_methods(root_module, root_module['ns3::ObjectBase'])
    register_Ns3ObjectDeleter_methods(root_module, root_module['ns3::ObjectDeleter'])
    register_Ns3ObjectFactory_methods(root_module, root_module['ns3::ObjectFactory'])
    register_Ns3OfdmDcdChannelEncodings_methods(root_module, root_module['ns3::OfdmDcdChannelEncodings'])
    register_Ns3OfdmDlBurstProfile_methods(root_module, root_module['ns3::OfdmDlBurstProfile'])
    register_Ns3OfdmDlMapIe_methods(root_module, root_module['ns3::OfdmDlMapIe'])
    register_Ns3OfdmUlBurstProfile_methods(root_module, root_module['ns3::OfdmUlBurstProfile'])
    register_Ns3OfdmUlMapIe_methods(root_module, root_module['ns3::OfdmUlMapIe'])
    register_Ns3PacketMetadata_methods(root_module, root_module['ns3::PacketMetadata'])
    register_Ns3PacketMetadataItem_methods(root_module, root_module['ns3::PacketMetadata::Item'])
    register_Ns3PacketMetadataItemIterator_methods(root_module, root_module['ns3::PacketMetadata::ItemIterator'])
    register_Ns3PacketTagIterator_methods(root_module, root_module['ns3::PacketTagIterator'])
    register_Ns3PacketTagIteratorItem_methods(root_module, root_module['ns3::PacketTagIterator::Item'])
    register_Ns3PacketTagList_methods(root_module, root_module['ns3::PacketTagList'])
    register_Ns3PacketTagListTagData_methods(root_module, root_module['ns3::PacketTagList::TagData'])
    register_Ns3PcapFile_methods(root_module, root_module['ns3::PcapFile'])
    register_Ns3PcapHelper_methods(root_module, root_module['ns3::PcapHelper'])
    register_Ns3PcapHelperForDevice_methods(root_module, root_module['ns3::PcapHelperForDevice'])
    register_Ns3RandomVariable_methods(root_module, root_module['ns3::RandomVariable'])
    register_Ns3SNRToBlockErrorRateManager_methods(root_module, root_module['ns3::SNRToBlockErrorRateManager'])
    register_Ns3SNRToBlockErrorRateRecord_methods(root_module, root_module['ns3::SNRToBlockErrorRateRecord'])
    register_Ns3SSRecord_methods(root_module, root_module['ns3::SSRecord'])
    register_Ns3SeedManager_methods(root_module, root_module['ns3::SeedManager'])
    register_Ns3SendParams_methods(root_module, root_module['ns3::SendParams'])
    register_Ns3SequentialVariable_methods(root_module, root_module['ns3::SequentialVariable'])
    register_Ns3ServiceFlow_methods(root_module, root_module['ns3::ServiceFlow'])
    register_Ns3ServiceFlowRecord_methods(root_module, root_module['ns3::ServiceFlowRecord'])
    register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    register_Ns3Simulator_methods(root_module, root_module['ns3::Simulator'])
    register_Ns3Tag_methods(root_module, root_module['ns3::Tag'])
    register_Ns3TagBuffer_methods(root_module, root_module['ns3::TagBuffer'])
    register_Ns3TlvValue_methods(root_module, root_module['ns3::TlvValue'])
    register_Ns3TosTlvValue_methods(root_module, root_module['ns3::TosTlvValue'])
    register_Ns3TriangularVariable_methods(root_module, root_module['ns3::TriangularVariable'])
    register_Ns3TypeId_methods(root_module, root_module['ns3::TypeId'])
    register_Ns3TypeIdAttributeInformation_methods(root_module, root_module['ns3::TypeId::AttributeInformation'])
    register_Ns3TypeIdTraceSourceInformation_methods(root_module, root_module['ns3::TypeId::TraceSourceInformation'])
    register_Ns3U16TlvValue_methods(root_module, root_module['ns3::U16TlvValue'])
    register_Ns3U32TlvValue_methods(root_module, root_module['ns3::U32TlvValue'])
    register_Ns3U8TlvValue_methods(root_module, root_module['ns3::U8TlvValue'])
    register_Ns3UcdChannelEncodings_methods(root_module, root_module['ns3::UcdChannelEncodings'])
    register_Ns3UniformVariable_methods(root_module, root_module['ns3::UniformVariable'])
    register_Ns3VectorTlvValue_methods(root_module, root_module['ns3::VectorTlvValue'])
    register_Ns3WeibullVariable_methods(root_module, root_module['ns3::WeibullVariable'])
    register_Ns3WimaxHelper_methods(root_module, root_module['ns3::WimaxHelper'])
    register_Ns3ZetaVariable_methods(root_module, root_module['ns3::ZetaVariable'])
    register_Ns3ZipfVariable_methods(root_module, root_module['ns3::ZipfVariable'])
    register_Ns3Empty_methods(root_module, root_module['ns3::empty'])
    register_Ns3Int64x64_t_methods(root_module, root_module['ns3::int64x64_t'])
    register_Ns3SimpleOfdmSendParam_methods(root_module, root_module['ns3::simpleOfdmSendParam'])
    register_Ns3Chunk_methods(root_module, root_module['ns3::Chunk'])
    register_Ns3ClassificationRuleVectorTlvValue_methods(root_module, root_module['ns3::ClassificationRuleVectorTlvValue'])
    register_Ns3ConstantVariable_methods(root_module, root_module['ns3::ConstantVariable'])
    register_Ns3CsParamVectorTlvValue_methods(root_module, root_module['ns3::CsParamVectorTlvValue'])
    register_Ns3DeterministicVariable_methods(root_module, root_module['ns3::DeterministicVariable'])
    register_Ns3EmpiricalVariable_methods(root_module, root_module['ns3::EmpiricalVariable'])
    register_Ns3ErlangVariable_methods(root_module, root_module['ns3::ErlangVariable'])
    register_Ns3ExponentialVariable_methods(root_module, root_module['ns3::ExponentialVariable'])
    register_Ns3GammaVariable_methods(root_module, root_module['ns3::GammaVariable'])
    register_Ns3Header_methods(root_module, root_module['ns3::Header'])
    register_Ns3IntEmpiricalVariable_methods(root_module, root_module['ns3::IntEmpiricalVariable'])
    register_Ns3Ipv4AddressTlvValue_methods(root_module, root_module['ns3::Ipv4AddressTlvValue'])
    register_Ns3Ipv4AddressTlvValueIpv4Addr_methods(root_module, root_module['ns3::Ipv4AddressTlvValue::ipv4Addr'])
    register_Ns3LogNormalVariable_methods(root_module, root_module['ns3::LogNormalVariable'])
    register_Ns3MacHeaderType_methods(root_module, root_module['ns3::MacHeaderType'])
    register_Ns3ManagementMessageType_methods(root_module, root_module['ns3::ManagementMessageType'])
    register_Ns3NormalVariable_methods(root_module, root_module['ns3::NormalVariable'])
    register_Ns3Object_methods(root_module, root_module['ns3::Object'])
    register_Ns3ObjectAggregateIterator_methods(root_module, root_module['ns3::Object::AggregateIterator'])
    register_Ns3OfdmDownlinkFramePrefix_methods(root_module, root_module['ns3::OfdmDownlinkFramePrefix'])
    register_Ns3OfdmSendParams_methods(root_module, root_module['ns3::OfdmSendParams'])
    register_Ns3OfdmUcdChannelEncodings_methods(root_module, root_module['ns3::OfdmUcdChannelEncodings'])
    register_Ns3PacketBurst_methods(root_module, root_module['ns3::PacketBurst'])
    register_Ns3ParetoVariable_methods(root_module, root_module['ns3::ParetoVariable'])
    register_Ns3PcapFileWrapper_methods(root_module, root_module['ns3::PcapFileWrapper'])
    register_Ns3PortRangeTlvValue_methods(root_module, root_module['ns3::PortRangeTlvValue'])
    register_Ns3PortRangeTlvValuePortRange_methods(root_module, root_module['ns3::PortRangeTlvValue::PortRange'])
    register_Ns3PriorityUlJob_methods(root_module, root_module['ns3::PriorityUlJob'])
    register_Ns3PropagationLossModel_methods(root_module, root_module['ns3::PropagationLossModel'])
    register_Ns3ProtocolTlvValue_methods(root_module, root_module['ns3::ProtocolTlvValue'])
    register_Ns3RandomPropagationLossModel_methods(root_module, root_module['ns3::RandomPropagationLossModel'])
    register_Ns3RangePropagationLossModel_methods(root_module, root_module['ns3::RangePropagationLossModel'])
    register_Ns3RngReq_methods(root_module, root_module['ns3::RngReq'])
    register_Ns3RngRsp_methods(root_module, root_module['ns3::RngRsp'])
    register_Ns3SSManager_methods(root_module, root_module['ns3::SSManager'])
    register_Ns3ServiceFlowManager_methods(root_module, root_module['ns3::ServiceFlowManager'])
    register_Ns3SfVectorTlvValue_methods(root_module, root_module['ns3::SfVectorTlvValue'])
    register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    register_Ns3SimpleRefCount__Ns3OutputStreamWrapper_Ns3Empty_Ns3DefaultDeleter__lt__ns3OutputStreamWrapper__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >'])
    register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    register_Ns3SsServiceFlowManager_methods(root_module, root_module['ns3::SsServiceFlowManager'])
    register_Ns3ThreeLogDistancePropagationLossModel_methods(root_module, root_module['ns3::ThreeLogDistancePropagationLossModel'])
    register_Ns3Time_methods(root_module, root_module['ns3::Time'])
    register_Ns3Tlv_methods(root_module, root_module['ns3::Tlv'])
    register_Ns3TraceSourceAccessor_methods(root_module, root_module['ns3::TraceSourceAccessor'])
    register_Ns3Trailer_methods(root_module, root_module['ns3::Trailer'])
    register_Ns3TwoRayGroundPropagationLossModel_methods(root_module, root_module['ns3::TwoRayGroundPropagationLossModel'])
    register_Ns3Ucd_methods(root_module, root_module['ns3::Ucd'])
    register_Ns3UlJob_methods(root_module, root_module['ns3::UlJob'])
    register_Ns3UlMap_methods(root_module, root_module['ns3::UlMap'])
    register_Ns3UplinkScheduler_methods(root_module, root_module['ns3::UplinkScheduler'])
    register_Ns3UplinkSchedulerMBQoS_methods(root_module, root_module['ns3::UplinkSchedulerMBQoS'])
    register_Ns3UplinkSchedulerRtps_methods(root_module, root_module['ns3::UplinkSchedulerRtps'])
    register_Ns3UplinkSchedulerSimple_methods(root_module, root_module['ns3::UplinkSchedulerSimple'])
    register_Ns3WimaxConnection_methods(root_module, root_module['ns3::WimaxConnection'])
    register_Ns3WimaxMacQueue_methods(root_module, root_module['ns3::WimaxMacQueue'])
    register_Ns3WimaxMacToMacHeader_methods(root_module, root_module['ns3::WimaxMacToMacHeader'])
    register_Ns3WimaxPhy_methods(root_module, root_module['ns3::WimaxPhy'])
    register_Ns3AttributeAccessor_methods(root_module, root_module['ns3::AttributeAccessor'])
    register_Ns3AttributeChecker_methods(root_module, root_module['ns3::AttributeChecker'])
    register_Ns3AttributeValue_methods(root_module, root_module['ns3::AttributeValue'])
    register_Ns3BSScheduler_methods(root_module, root_module['ns3::BSScheduler'])
    register_Ns3BSSchedulerRtps_methods(root_module, root_module['ns3::BSSchedulerRtps'])
    register_Ns3BSSchedulerSimple_methods(root_module, root_module['ns3::BSSchedulerSimple'])
    register_Ns3BandwidthRequestHeader_methods(root_module, root_module['ns3::BandwidthRequestHeader'])
    register_Ns3BsServiceFlowManager_methods(root_module, root_module['ns3::BsServiceFlowManager'])
    register_Ns3CallbackChecker_methods(root_module, root_module['ns3::CallbackChecker'])
    register_Ns3CallbackImplBase_methods(root_module, root_module['ns3::CallbackImplBase'])
    register_Ns3CallbackValue_methods(root_module, root_module['ns3::CallbackValue'])
    register_Ns3Channel_methods(root_module, root_module['ns3::Channel'])
    register_Ns3ConnectionManager_methods(root_module, root_module['ns3::ConnectionManager'])
    register_Ns3Dcd_methods(root_module, root_module['ns3::Dcd'])
    register_Ns3DlMap_methods(root_module, root_module['ns3::DlMap'])
    register_Ns3DsaAck_methods(root_module, root_module['ns3::DsaAck'])
    register_Ns3DsaReq_methods(root_module, root_module['ns3::DsaReq'])
    register_Ns3DsaRsp_methods(root_module, root_module['ns3::DsaRsp'])
    register_Ns3EmptyAttributeValue_methods(root_module, root_module['ns3::EmptyAttributeValue'])
    register_Ns3EventImpl_methods(root_module, root_module['ns3::EventImpl'])
    register_Ns3FixedRssLossModel_methods(root_module, root_module['ns3::FixedRssLossModel'])
    register_Ns3FragmentationSubheader_methods(root_module, root_module['ns3::FragmentationSubheader'])
    register_Ns3FriisPropagationLossModel_methods(root_module, root_module['ns3::FriisPropagationLossModel'])
    register_Ns3GenericMacHeader_methods(root_module, root_module['ns3::GenericMacHeader'])
    register_Ns3GrantManagementSubheader_methods(root_module, root_module['ns3::GrantManagementSubheader'])
    register_Ns3IpcsClassifier_methods(root_module, root_module['ns3::IpcsClassifier'])
    register_Ns3Ipv4AddressChecker_methods(root_module, root_module['ns3::Ipv4AddressChecker'])
    register_Ns3Ipv4AddressValue_methods(root_module, root_module['ns3::Ipv4AddressValue'])
    register_Ns3Ipv4MaskChecker_methods(root_module, root_module['ns3::Ipv4MaskChecker'])
    register_Ns3Ipv4MaskValue_methods(root_module, root_module['ns3::Ipv4MaskValue'])
    register_Ns3Ipv6AddressChecker_methods(root_module, root_module['ns3::Ipv6AddressChecker'])
    register_Ns3Ipv6AddressValue_methods(root_module, root_module['ns3::Ipv6AddressValue'])
    register_Ns3Ipv6PrefixChecker_methods(root_module, root_module['ns3::Ipv6PrefixChecker'])
    register_Ns3Ipv6PrefixValue_methods(root_module, root_module['ns3::Ipv6PrefixValue'])
    register_Ns3LogDistancePropagationLossModel_methods(root_module, root_module['ns3::LogDistancePropagationLossModel'])
    register_Ns3Mac48AddressChecker_methods(root_module, root_module['ns3::Mac48AddressChecker'])
    register_Ns3Mac48AddressValue_methods(root_module, root_module['ns3::Mac48AddressValue'])
    register_Ns3MatrixPropagationLossModel_methods(root_module, root_module['ns3::MatrixPropagationLossModel'])
    register_Ns3NakagamiPropagationLossModel_methods(root_module, root_module['ns3::NakagamiPropagationLossModel'])
    register_Ns3NetDevice_methods(root_module, root_module['ns3::NetDevice'])
    register_Ns3NixVector_methods(root_module, root_module['ns3::NixVector'])
    register_Ns3Node_methods(root_module, root_module['ns3::Node'])
    register_Ns3ObjectFactoryChecker_methods(root_module, root_module['ns3::ObjectFactoryChecker'])
    register_Ns3ObjectFactoryValue_methods(root_module, root_module['ns3::ObjectFactoryValue'])
    register_Ns3OutputStreamWrapper_methods(root_module, root_module['ns3::OutputStreamWrapper'])
    register_Ns3Packet_methods(root_module, root_module['ns3::Packet'])
    register_Ns3RandomVariableChecker_methods(root_module, root_module['ns3::RandomVariableChecker'])
    register_Ns3RandomVariableValue_methods(root_module, root_module['ns3::RandomVariableValue'])
    register_Ns3SimpleOfdmWimaxPhy_methods(root_module, root_module['ns3::SimpleOfdmWimaxPhy'])
    register_Ns3TimeChecker_methods(root_module, root_module['ns3::TimeChecker'])
    register_Ns3TimeValue_methods(root_module, root_module['ns3::TimeValue'])
    register_Ns3TypeIdChecker_methods(root_module, root_module['ns3::TypeIdChecker'])
    register_Ns3TypeIdValue_methods(root_module, root_module['ns3::TypeIdValue'])
    register_Ns3UintegerValue_methods(root_module, root_module['ns3::UintegerValue'])
    register_Ns3WimaxChannel_methods(root_module, root_module['ns3::WimaxChannel'])
    register_Ns3WimaxNetDevice_methods(root_module, root_module['ns3::WimaxNetDevice'])
    register_Ns3AddressChecker_methods(root_module, root_module['ns3::AddressChecker'])
    register_Ns3AddressValue_methods(root_module, root_module['ns3::AddressValue'])
    register_Ns3BaseStationNetDevice_methods(root_module, root_module['ns3::BaseStationNetDevice'])
    register_Ns3SimpleOfdmWimaxChannel_methods(root_module, root_module['ns3::SimpleOfdmWimaxChannel'])
    register_Ns3SubscriberStationNetDevice_methods(root_module, root_module['ns3::SubscriberStationNetDevice'])
    return

def register_Ns3Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint8_t', 'type'), param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    
    cls.add_constructor([param('ns3::Address const &', 'address')])
    
    cls.add_method('CheckCompatible', 
                   'bool', 
                   [param('uint8_t', 'type'), param('uint8_t', 'len')], 
                   is_const=True)
    
    cls.add_method('CopyAllFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    
    cls.add_method('CopyAllTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint8_t', 'len')], 
                   is_const=True)
    
    cls.add_method('CopyFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    
    cls.add_method('CopyTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')])
    
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsInvalid', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('uint8_t', 'type')], 
                   is_const=True)
    
    cls.add_method('Register', 
                   'uint8_t', 
                   [], 
                   is_static=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')], 
                   is_const=True)
    return

def register_Ns3AsciiTraceHelper_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::AsciiTraceHelper const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('CreateFileStream', 
                   'ns3::Ptr< ns3::OutputStreamWrapper >', 
                   [param('std::string', 'filename'), param('std::_Ios_Openmode', 'filemode', default_value='std::ios_base::out')])
    
    cls.add_method('DefaultDequeueSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('DefaultDequeueSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('DefaultDropSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('DefaultDropSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('DefaultEnqueueSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('DefaultEnqueueSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('DefaultReceiveSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('DefaultReceiveSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    
    cls.add_method('GetFilenameFromDevice', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'useObjectNames', default_value='true')])
    
    cls.add_method('GetFilenameFromInterfacePair', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::Object >', 'object'), param('uint32_t', 'interface'), param('bool', 'useObjectNames', default_value='true')])
    return

def register_Ns3AsciiTraceHelperForDevice_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::AsciiTraceHelperForDevice const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'explicitFilename', default_value='false')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('ns3::Ptr< ns3::NetDevice >', 'nd')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('std::string', 'ndName'), param('bool', 'explicitFilename', default_value='false')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('std::string', 'ndName')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NetDeviceContainer', 'd')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('ns3::NetDeviceContainer', 'd')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NodeContainer', 'n')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('ns3::NodeContainer', 'n')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('uint32_t', 'nodeid'), param('uint32_t', 'deviceid'), param('bool', 'explicitFilename')])
    
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('uint32_t', 'nodeid'), param('uint32_t', 'deviceid')])
    
    cls.add_method('EnableAsciiAll', 
                   'void', 
                   [param('std::string', 'prefix')])
    
    cls.add_method('EnableAsciiAll', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream')])
    
    cls.add_method('EnableAsciiInternal', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'explicitFilename')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3AttributeConstructionList_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::AttributeConstructionList const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker'), param('ns3::Ptr< ns3::AttributeValue >', 'value')])
    
    cls.add_method('Begin', 
                   'std::_List_const_iterator< ns3::AttributeConstructionList::Item >', 
                   [], 
                   is_const=True)
    
    cls.add_method('End', 
                   'std::_List_const_iterator< ns3::AttributeConstructionList::Item >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Find', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True)
    return

def register_Ns3AttributeConstructionListItem_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::AttributeConstructionList::Item const &', 'arg0')])
    
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    
    cls.add_instance_attribute('value', 'ns3::Ptr< ns3::AttributeValue >', is_const=False)
    return

def register_Ns3Buffer_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint32_t', 'dataSize')])
    
    cls.add_constructor([param('uint32_t', 'dataSize'), param('bool', 'initialize')])
    
    cls.add_constructor([param('ns3::Buffer const &', 'o')])
    
    cls.add_method('AddAtEnd', 
                   'bool', 
                   [param('uint32_t', 'end')])
    
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Buffer const &', 'o')])
    
    cls.add_method('AddAtStart', 
                   'bool', 
                   [param('uint32_t', 'start')])
    
    cls.add_method('Begin', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    
    cls.add_method('CreateFragment', 
                   'ns3::Buffer', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    
    cls.add_method('CreateFullCopy', 
                   'ns3::Buffer', 
                   [], 
                   is_const=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('End', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetCurrentEndOffset', 
                   'int32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetCurrentStartOffset', 
                   'int32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('PeekData', 
                   'uint8_t const *', 
                   [], 
                   is_const=True)
    
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3BufferIterator_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Buffer::Iterator const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size')])
    
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size'), param('uint32_t', 'initialChecksum')])
    
    cls.add_method('GetDistanceFrom', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator const &', 'o')], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsEnd', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsStart', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Next', 
                   'void', 
                   [])
    
    cls.add_method('Next', 
                   'void', 
                   [param('uint32_t', 'delta')])
    
    cls.add_method('Prev', 
                   'void', 
                   [])
    
    cls.add_method('Prev', 
                   'void', 
                   [param('uint32_t', 'delta')])
    
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('ReadLsbtohU16', 
                   'uint16_t', 
                   [])
    
    cls.add_method('ReadLsbtohU32', 
                   'uint32_t', 
                   [])
    
    cls.add_method('ReadLsbtohU64', 
                   'uint64_t', 
                   [])
    
    cls.add_method('ReadNtohU16', 
                   'uint16_t', 
                   [])
    
    cls.add_method('ReadNtohU32', 
                   'uint32_t', 
                   [])
    
    cls.add_method('ReadNtohU64', 
                   'uint64_t', 
                   [])
    
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start'), param('ns3::Buffer::Iterator', 'end')])
    
    cls.add_method('WriteHtolsbU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    
    cls.add_method('WriteHtolsbU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    
    cls.add_method('WriteHtolsbU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    
    cls.add_method('WriteHtonU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    
    cls.add_method('WriteHtonU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    
    cls.add_method('WriteHtonU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data')])
    
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data'), param('uint32_t', 'len')])
    return

def register_Ns3ByteTagIterator_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ByteTagIterator const &', 'arg0')])
    
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Next', 
                   'ns3::ByteTagIterator::Item', 
                   [])
    return

def register_Ns3ByteTagIteratorItem_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ByteTagIterator::Item const &', 'arg0')])
    
    cls.add_method('GetEnd', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3ByteTagList_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::ByteTagList const &', 'o')])
    
    cls.add_method('Add', 
                   'ns3::TagBuffer', 
                   [param('ns3::TypeId', 'tid'), param('uint32_t', 'bufferSize'), param('int32_t', 'start'), param('int32_t', 'end')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::ByteTagList const &', 'o')])
    
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('int32_t', 'adjustment'), param('int32_t', 'appendOffset')])
    
    cls.add_method('AddAtStart', 
                   'void', 
                   [param('int32_t', 'adjustment'), param('int32_t', 'prependOffset')])
    
    cls.add_method('Begin', 
                   'ns3::ByteTagList::Iterator', 
                   [param('int32_t', 'offsetStart'), param('int32_t', 'offsetEnd')], 
                   is_const=True)
    
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    return

def register_Ns3ByteTagListIterator_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ByteTagList::Iterator const &', 'arg0')])
    
    cls.add_method('GetOffsetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Next', 
                   'ns3::ByteTagList::Iterator::Item', 
                   [])
    return

def register_Ns3ByteTagListIteratorItem_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ByteTagList::Iterator::Item const &', 'arg0')])
    
    cls.add_constructor([param('ns3::TagBuffer', 'buf')])
    
    cls.add_instance_attribute('buf', 'ns3::TagBuffer', is_const=False)
    
    cls.add_instance_attribute('end', 'int32_t', is_const=False)
    
    cls.add_instance_attribute('size', 'uint32_t', is_const=False)
    
    cls.add_instance_attribute('start', 'int32_t', is_const=False)
    
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3CallbackBase_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::CallbackBase const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetImpl', 
                   'ns3::Ptr< ns3::CallbackImplBase >', 
                   [], 
                   is_const=True)
    
    cls.add_constructor([param('ns3::Ptr< ns3::CallbackImplBase >', 'impl')], 
                        visibility='protected')
    
    cls.add_method('Demangle', 
                   'std::string', 
                   [param('std::string const &', 'mangled')], 
                   is_static=True, visibility='protected')
    return

def register_Ns3Cid_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([param('ns3::Cid const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint16_t', 'cid')])
    
    cls.add_method('Broadcast', 
                   'ns3::Cid', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetIdentifier', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('InitialRanging', 
                   'ns3::Cid', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsInitialRanging', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsPadding', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Padding', 
                   'ns3::Cid', 
                   [], 
                   is_static=True)
    return

def register_Ns3CidFactory_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::CidFactory const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Allocate', 
                   'ns3::Cid', 
                   [param('ns3::Cid::Type', 'type')])
    
    cls.add_method('AllocateBasic', 
                   'ns3::Cid', 
                   [])
    
    cls.add_method('AllocateMulticast', 
                   'ns3::Cid', 
                   [])
    
    cls.add_method('AllocatePrimary', 
                   'ns3::Cid', 
                   [])
    
    cls.add_method('AllocateTransportOrSecondary', 
                   'ns3::Cid', 
                   [])
    
    cls.add_method('FreeCid', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('IsBasic', 
                   'bool', 
                   [param('ns3::Cid', 'cid')], 
                   is_const=True)
    
    cls.add_method('IsPrimary', 
                   'bool', 
                   [param('ns3::Cid', 'cid')], 
                   is_const=True)
    
    cls.add_method('IsTransport', 
                   'bool', 
                   [param('ns3::Cid', 'cid')], 
                   is_const=True)
    return

def register_Ns3CsParameters_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::CsParameters const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Tlv', 'tlv')])
    
    cls.add_constructor([param('ns3::CsParameters::Action', 'classifierDscAction'), param('ns3::IpcsClassifierRecord', 'classifier')])
    
    cls.add_method('GetClassifierDscAction', 
                   'ns3::CsParameters::Action', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPacketClassifierRule', 
                   'ns3::IpcsClassifierRecord', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetClassifierDscAction', 
                   'void', 
                   [param('ns3::CsParameters::Action', 'action')])
    
    cls.add_method('SetPacketClassifierRule', 
                   'void', 
                   [param('ns3::IpcsClassifierRecord', 'packetClassifierRule')])
    
    cls.add_method('ToTlv', 
                   'ns3::Tlv', 
                   [], 
                   is_const=True)
    return

def register_Ns3DcdChannelEncodings_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::DcdChannelEncodings const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetBsEirp', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetEirxPIrMax', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrequency', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Read', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('SetBsEirp', 
                   'void', 
                   [param('uint16_t', 'bs_eirp')])
    
    cls.add_method('SetEirxPIrMax', 
                   'void', 
                   [param('uint16_t', 'rss_ir_max')])
    
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('uint32_t', 'frequency')])
    
    cls.add_method('Write', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    
    cls.add_method('DoRead', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoWrite', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3DlFramePrefixIe_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::DlFramePrefixIe const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetDiuc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLength', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPreamblePresent', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRateId', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetStartTime', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Read', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('SetDiuc', 
                   'void', 
                   [param('uint8_t', 'diuc')])
    
    cls.add_method('SetLength', 
                   'void', 
                   [param('uint16_t', 'length')])
    
    cls.add_method('SetPreamblePresent', 
                   'void', 
                   [param('uint8_t', 'preamblePresent')])
    
    cls.add_method('SetRateId', 
                   'void', 
                   [param('uint8_t', 'rateId')])
    
    cls.add_method('SetStartTime', 
                   'void', 
                   [param('uint16_t', 'startTime')])
    
    cls.add_method('Write', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    return

def register_Ns3EventId_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([param('ns3::EventId const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::EventImpl > const &', 'impl'), param('uint64_t', 'ts'), param('uint32_t', 'context'), param('uint32_t', 'uid')])
    
    cls.add_method('Cancel', 
                   'void', 
                   [])
    
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTs', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsExpired', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsRunning', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('PeekEventImpl', 
                   'ns3::EventImpl *', 
                   [], 
                   is_const=True)
    return

def register_Ns3IpcsClassifierRecord_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::IpcsClassifierRecord const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv4Address', 'srcAddress'), param('ns3::Ipv4Mask', 'srcMask'), param('ns3::Ipv4Address', 'dstAddress'), param('ns3::Ipv4Mask', 'dstMask'), param('uint16_t', 'srcPortLow'), param('uint16_t', 'srcPortHigh'), param('uint16_t', 'dstPortLow'), param('uint16_t', 'dstPortHigh'), param('uint8_t', 'protocol'), param('uint8_t', 'priority')])
    
    cls.add_constructor([param('ns3::Tlv', 'tlv')])
    
    cls.add_method('AddDstAddr', 
                   'void', 
                   [param('ns3::Ipv4Address', 'dstAddress'), param('ns3::Ipv4Mask', 'dstMask')])
    
    cls.add_method('AddDstPortRange', 
                   'void', 
                   [param('uint16_t', 'dstPortLow'), param('uint16_t', 'dstPortHigh')])
    
    cls.add_method('AddProtocol', 
                   'void', 
                   [param('uint8_t', 'proto')])
    
    cls.add_method('AddSrcAddr', 
                   'void', 
                   [param('ns3::Ipv4Address', 'srcAddress'), param('ns3::Ipv4Mask', 'srcMask')])
    
    cls.add_method('AddSrcPortRange', 
                   'void', 
                   [param('uint16_t', 'srcPortLow'), param('uint16_t', 'srcPortHigh')])
    
    cls.add_method('CheckMatch', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'srcAddress'), param('ns3::Ipv4Address', 'dstAddress'), param('uint16_t', 'srcPort'), param('uint16_t', 'dstPort'), param('uint8_t', 'proto')], 
                   is_const=True)
    
    cls.add_method('GetCid', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetIndex', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPriority', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetCid', 
                   'void', 
                   [param('uint16_t', 'cid')])
    
    cls.add_method('SetIndex', 
                   'void', 
                   [param('uint16_t', 'index')])
    
    cls.add_method('SetPriority', 
                   'void', 
                   [param('uint8_t', 'prio')])
    
    cls.add_method('ToTlv', 
                   'ns3::Tlv', 
                   [], 
                   is_const=True)
    return

def register_Ns3Ipv4Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([param('ns3::Ipv4Address const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint32_t', 'address')])
    
    cls.add_constructor([param('char const *', 'address')])
    
    cls.add_method('CombineMask', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    
    cls.add_method('Deserialize', 
                   'ns3::Ipv4Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetAny', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetBroadcast', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetSubnetDirectedBroadcast', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    
    cls.add_method('GetZero', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Address const &', 'other')], 
                   is_const=True)
    
    cls.add_method('IsLocalMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsSubnetDirectedBroadcast', 
                   'bool', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'address')])
    
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    return

def register_Ns3Ipv4Mask_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint32_t', 'mask')])
    
    cls.add_constructor([param('char const *', 'mask')])
    
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInverse', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetOnes', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetPrefixLength', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetZero', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Mask', 'other')], 
                   is_const=True)
    
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'a'), param('ns3::Ipv4Address', 'b')], 
                   is_const=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'mask')])
    return

def register_Ns3Ipv6Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([])
    
    cls.add_constructor([param('char const *', 'address')])
    
    cls.add_constructor([param('uint8_t *', 'address')])
    
    cls.add_constructor([param('ns3::Ipv6Address const &', 'addr')])
    
    cls.add_constructor([param('ns3::Ipv6Address const *', 'addr')])
    
    cls.add_method('CombinePrefix', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Prefix const &', 'prefix')])
    
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    
    cls.add_method('Deserialize', 
                   'ns3::Ipv6Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    
    cls.add_method('GetAllHostsMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetAllNodesMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetAllRoutersMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetAny', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetZero', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsAllHostsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsAllNodesMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsAllRoutersMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsAny', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Address const &', 'other')], 
                   is_const=True)
    
    cls.add_method('IsLinkLocal', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsLocalhost', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsSolicitedMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'mac')], 
                   is_static=True)
    
    cls.add_method('MakeSolicitedAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    
    cls.add_method('Set', 
                   'void', 
                   [param('uint8_t *', 'address')])
    return

def register_Ns3Ipv6Prefix_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint8_t *', 'prefix')])
    
    cls.add_constructor([param('char const *', 'prefix')])
    
    cls.add_constructor([param('uint8_t', 'prefix')])
    
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'prefix')])
    
    cls.add_constructor([param('ns3::Ipv6Prefix const *', 'prefix')])
    
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetPrefixLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetZero', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Prefix const &', 'other')], 
                   is_const=True)
    
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv6Address', 'a'), param('ns3::Ipv6Address', 'b')], 
                   is_const=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    return

def register_Ns3LogComponent_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::LogComponent const &', 'arg0')])
    
    cls.add_constructor([param('char const *', 'name')])
    
    cls.add_method('Disable', 
                   'void', 
                   [param('ns3::LogLevel', 'level')])
    
    cls.add_method('Enable', 
                   'void', 
                   [param('ns3::LogLevel', 'level')])
    
    cls.add_method('EnvVarCheck', 
                   'void', 
                   [param('char const *', 'name')])
    
    cls.add_method('IsEnabled', 
                   'bool', 
                   [param('ns3::LogLevel', 'level')], 
                   is_const=True)
    
    cls.add_method('IsNoneEnabled', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Name', 
                   'char const *', 
                   [], 
                   is_const=True)
    return

def register_Ns3Mac48Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([param('ns3::Mac48Address const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('char const *', 'str')])
    
    cls.add_method('Allocate', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('ConvertFrom', 
                   'ns3::Mac48Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('uint8_t const *', 'buffer')])
    
    cls.add_method('CopyTo', 
                   'void', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    
    cls.add_method('GetBroadcast', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv4Address', 'address')], 
                   is_static=True)
    
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv6Address', 'address')], 
                   is_static=True)
    
    cls.add_method('GetMulticast6Prefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetMulticastPrefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsGroup', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    return

def register_Ns3NetDeviceContainer_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::NetDeviceContainer const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::NetDevice >', 'dev')])
    
    cls.add_constructor([param('std::string', 'devName')])
    
    cls.add_constructor([param('ns3::NetDeviceContainer const &', 'a'), param('ns3::NetDeviceContainer const &', 'b')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::NetDeviceContainer', 'other')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'deviceName')])
    
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::NetDevice > const, std::vector< ns3::Ptr< ns3::NetDevice > > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::NetDevice > const, std::vector< ns3::Ptr< ns3::NetDevice > > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3NodeContainer_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::NodeContainer const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::Node >', 'node')])
    
    cls.add_constructor([param('std::string', 'nodeName')])
    
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b')])
    
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c')])
    
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd')])
    
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd'), param('ns3::NodeContainer const &', 'e')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::NodeContainer', 'other')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'nodeName')])
    
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n')])
    
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n'), param('uint32_t', 'systemId')])
    
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Node >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    
    cls.add_method('GetGlobal', 
                   'ns3::NodeContainer', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3ObjectBase_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::ObjectBase const &', 'arg0')])
    
    cls.add_method('GetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    
    cls.add_method('GetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'attribute')], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('SetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    
    cls.add_method('SetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    
    cls.add_method('TraceConnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    
    cls.add_method('TraceConnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    
    cls.add_method('TraceDisconnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    
    cls.add_method('TraceDisconnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    
    cls.add_method('ConstructSelf', 
                   'void', 
                   [param('ns3::AttributeConstructionList const &', 'attributes')], 
                   visibility='protected')
    
    cls.add_method('NotifyConstructionCompleted', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectDeleter_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::ObjectDeleter const &', 'arg0')])
    
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::Object *', 'object')], 
                   is_static=True)
    return

def register_Ns3ObjectFactory_methods(root_module, cls):
    cls.add_output_stream_operator()
    
    cls.add_constructor([param('ns3::ObjectFactory const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('std::string', 'typeId')])
    
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::Object >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('ns3::TypeId', 'tid')])
    
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('char const *', 'tid')])
    
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('std::string', 'tid')])
    return

def register_Ns3OfdmDcdChannelEncodings_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmDcdChannelEncodings const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetBaseStationId', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetChannelNr', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrameDurationCode', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrameNumber', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRtg', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTtg', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetBaseStationId', 
                   'void', 
                   [param('ns3::Mac48Address', 'baseStationId')])
    
    cls.add_method('SetChannelNr', 
                   'void', 
                   [param('uint8_t', 'channelNr')])
    
    cls.add_method('SetFrameDurationCode', 
                   'void', 
                   [param('uint8_t', 'frameDurationCode')])
    
    cls.add_method('SetFrameNumber', 
                   'void', 
                   [param('uint32_t', 'frameNumber')])
    
    cls.add_method('SetRtg', 
                   'void', 
                   [param('uint8_t', 'rtg')])
    
    cls.add_method('SetTtg', 
                   'void', 
                   [param('uint8_t', 'ttg')])
    
    cls.add_method('DoRead', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoWrite', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3OfdmDlBurstProfile_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmDlBurstProfile const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetDiuc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFecCodeType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Read', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('SetDiuc', 
                   'void', 
                   [param('uint8_t', 'diuc')])
    
    cls.add_method('SetFecCodeType', 
                   'void', 
                   [param('uint8_t', 'fecCodeType')])
    
    cls.add_method('SetLength', 
                   'void', 
                   [param('uint8_t', 'length')])
    
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    
    cls.add_method('Write', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    return

def register_Ns3OfdmDlMapIe_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmDlMapIe const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDiuc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPreamblePresent', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetStartTime', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Read', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('SetCid', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('SetDiuc', 
                   'void', 
                   [param('uint8_t', 'diuc')])
    
    cls.add_method('SetPreamblePresent', 
                   'void', 
                   [param('uint8_t', 'preamblePresent')])
    
    cls.add_method('SetStartTime', 
                   'void', 
                   [param('uint16_t', 'startTime')])
    
    cls.add_method('Write', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    return

def register_Ns3OfdmUlBurstProfile_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmUlBurstProfile const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetFecCodeType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUiuc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Read', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('SetFecCodeType', 
                   'void', 
                   [param('uint8_t', 'fecCodeType')])
    
    cls.add_method('SetLength', 
                   'void', 
                   [param('uint8_t', 'length')])
    
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    
    cls.add_method('SetUiuc', 
                   'void', 
                   [param('uint8_t', 'uiuc')])
    
    cls.add_method('Write', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    return

def register_Ns3OfdmUlMapIe_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmUlMapIe const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDuration', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMidambleRepetitionInterval', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetStartTime', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSubchannelIndex', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUiuc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Read', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('SetCid', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('SetDuration', 
                   'void', 
                   [param('uint16_t', 'duration')])
    
    cls.add_method('SetMidambleRepetitionInterval', 
                   'void', 
                   [param('uint8_t', 'midambleRepetitionInterval')])
    
    cls.add_method('SetStartTime', 
                   'void', 
                   [param('uint16_t', 'startTime')])
    
    cls.add_method('SetSubchannelIndex', 
                   'void', 
                   [param('uint8_t', 'subchannelIndex')])
    
    cls.add_method('SetUiuc', 
                   'void', 
                   [param('uint8_t', 'uiuc')])
    
    cls.add_method('Write', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    return

def register_Ns3PacketMetadata_methods(root_module, cls):
    
    cls.add_constructor([param('uint64_t', 'uid'), param('uint32_t', 'size')])
    
    cls.add_constructor([param('ns3::PacketMetadata const &', 'o')])
    
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::PacketMetadata const &', 'o')])
    
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [param('ns3::Buffer', 'buffer')], 
                   is_const=True)
    
    cls.add_method('CreateFragment', 
                   'ns3::PacketMetadata', 
                   [param('uint32_t', 'start'), param('uint32_t', 'end')], 
                   is_const=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('Enable', 
                   'void', 
                   [], 
                   is_static=True)
    
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    
    cls.add_method('RemoveHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    
    cls.add_method('RemoveTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3PacketMetadataItem_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::PacketMetadata::Item const &', 'arg0')])
    
    cls.add_instance_attribute('current', 'ns3::Buffer::Iterator', is_const=False)
    
    cls.add_instance_attribute('currentSize', 'uint32_t', is_const=False)
    
    cls.add_instance_attribute('currentTrimedFromEnd', 'uint32_t', is_const=False)
    
    cls.add_instance_attribute('currentTrimedFromStart', 'uint32_t', is_const=False)
    
    cls.add_instance_attribute('isFragment', 'bool', is_const=False)
    
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3PacketMetadataItemIterator_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PacketMetadata::ItemIterator const &', 'arg0')])
    
    cls.add_constructor([param('ns3::PacketMetadata const *', 'metadata'), param('ns3::Buffer', 'buffer')])
    
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Next', 
                   'ns3::PacketMetadata::Item', 
                   [])
    return

def register_Ns3PacketTagIterator_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PacketTagIterator const &', 'arg0')])
    
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Next', 
                   'ns3::PacketTagIterator::Item', 
                   [])
    return

def register_Ns3PacketTagIteratorItem_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PacketTagIterator::Item const &', 'arg0')])
    
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3PacketTagList_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::PacketTagList const &', 'o')])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    
    cls.add_method('Head', 
                   'ns3::PacketTagList::TagData const *', 
                   [], 
                   is_const=True)
    
    cls.add_method('Peek', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    
    cls.add_method('Remove', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    return

def register_Ns3PacketTagListTagData_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::PacketTagList::TagData const &', 'arg0')])
    
    cls.add_instance_attribute('count', 'uint32_t', is_const=False)
    
    cls.add_instance_attribute('data', 'uint8_t [ 20 ]', is_const=False)
    
    cls.add_instance_attribute('next', 'ns3::PacketTagList::TagData *', is_const=False)
    
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3PcapFile_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_method('Clear', 
                   'void', 
                   [])
    
    cls.add_method('Close', 
                   'void', 
                   [])
    
    cls.add_method('Diff', 
                   'bool', 
                   [param('std::string const &', 'f1'), param('std::string const &', 'f2'), param('uint32_t &', 'sec'), param('uint32_t &', 'usec'), param('uint32_t', 'snapLen', default_value='ns3::PcapFile::SNAPLEN_DEFAULT')], 
                   is_static=True)
    
    cls.add_method('Eof', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Fail', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDataLinkType', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetMagic', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetSigFigs', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetSnapLen', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetSwapMode', 
                   'bool', 
                   [])
    
    cls.add_method('GetTimeZoneOffset', 
                   'int32_t', 
                   [])
    
    cls.add_method('GetVersionMajor', 
                   'uint16_t', 
                   [])
    
    cls.add_method('GetVersionMinor', 
                   'uint16_t', 
                   [])
    
    cls.add_method('Init', 
                   'void', 
                   [param('uint32_t', 'dataLinkType'), param('uint32_t', 'snapLen', default_value='ns3::PcapFile::SNAPLEN_DEFAULT'), param('int32_t', 'timeZoneCorrection', default_value='ns3::PcapFile::ZONE_DEFAULT'), param('bool', 'swapMode', default_value='false')])
    
    cls.add_method('Open', 
                   'void', 
                   [param('std::string const &', 'filename'), param('std::_Ios_Openmode', 'mode')])
    
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t * const', 'data'), param('uint32_t', 'maxBytes'), param('uint32_t &', 'tsSec'), param('uint32_t &', 'tsUsec'), param('uint32_t &', 'inclLen'), param('uint32_t &', 'origLen'), param('uint32_t &', 'readLen')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('uint32_t', 'tsSec'), param('uint32_t', 'tsUsec'), param('uint8_t const * const', 'data'), param('uint32_t', 'totalLen')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('uint32_t', 'tsSec'), param('uint32_t', 'tsUsec'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('uint32_t', 'tsSec'), param('uint32_t', 'tsUsec'), param('ns3::Header &', 'header'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    
    cls.add_static_attribute('SNAPLEN_DEFAULT', 'uint32_t const', is_const=True)
    
    cls.add_static_attribute('ZONE_DEFAULT', 'int32_t const', is_const=True)
    return

def register_Ns3PcapHelper_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PcapHelper const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('CreateFile', 
                   'ns3::Ptr< ns3::PcapFileWrapper >', 
                   [param('std::string', 'filename'), param('std::_Ios_Openmode', 'filemode'), param('uint32_t', 'dataLinkType'), param('uint32_t', 'snapLen', default_value='65535'), param('int32_t', 'tzCorrection', default_value='0')])
    
    cls.add_method('GetFilenameFromDevice', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'useObjectNames', default_value='true')])
    
    cls.add_method('GetFilenameFromInterfacePair', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::Object >', 'object'), param('uint32_t', 'interface'), param('bool', 'useObjectNames', default_value='true')])
    return

def register_Ns3PcapHelperForDevice_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PcapHelperForDevice const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'promiscuous', default_value='false'), param('bool', 'explicitFilename', default_value='false')])
    
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('std::string', 'ndName'), param('bool', 'promiscuous', default_value='false'), param('bool', 'explicitFilename', default_value='false')])
    
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NetDeviceContainer', 'd'), param('bool', 'promiscuous', default_value='false')])
    
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NodeContainer', 'n'), param('bool', 'promiscuous', default_value='false')])
    
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('uint32_t', 'nodeid'), param('uint32_t', 'deviceid'), param('bool', 'promiscuous', default_value='false')])
    
    cls.add_method('EnablePcapAll', 
                   'void', 
                   [param('std::string', 'prefix'), param('bool', 'promiscuous', default_value='false')])
    
    cls.add_method('EnablePcapInternal', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'promiscuous'), param('bool', 'explicitFilename')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3RandomVariable_methods(root_module, cls):
    cls.add_output_stream_operator()
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::RandomVariable const &', 'o')])
    
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_const=True)
    return

def register_Ns3SNRToBlockErrorRateManager_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SNRToBlockErrorRateManager const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('ActivateLoss', 
                   'void', 
                   [param('bool', 'loss')])
    
    cls.add_method('GetBlockErrorRate', 
                   'double', 
                   [param('double', 'SNR'), param('uint8_t', 'modulation')])
    
    cls.add_method('GetSNRToBlockErrorRateRecord', 
                   'ns3::SNRToBlockErrorRateRecord *', 
                   [param('double', 'SNR'), param('uint8_t', 'modulation')])
    
    cls.add_method('GetTraceFilePath', 
                   'std::string', 
                   [])
    
    cls.add_method('LoadDefaultTraces', 
                   'void', 
                   [])
    
    cls.add_method('LoadTraces', 
                   'void', 
                   [])
    
    cls.add_method('ReLoadTraces', 
                   'void', 
                   [])
    
    cls.add_method('SetTraceFilePath', 
                   'void', 
                   [param('char *', 'traceFilePath')])
    return

def register_Ns3SNRToBlockErrorRateRecord_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SNRToBlockErrorRateRecord const &', 'arg0')])
    
    cls.add_constructor([param('double', 'snrValue'), param('double', 'bitErrorRate'), param('double', 'BlockErrorRate'), param('double', 'sigma2'), param('double', 'I1'), param('double', 'I2')])
    
    cls.add_method('Copy', 
                   'ns3::SNRToBlockErrorRateRecord *', 
                   [])
    
    cls.add_method('GetBitErrorRate', 
                   'double', 
                   [])
    
    cls.add_method('GetBlockErrorRate', 
                   'double', 
                   [])
    
    cls.add_method('GetI1', 
                   'double', 
                   [])
    
    cls.add_method('GetI2', 
                   'double', 
                   [])
    
    cls.add_method('GetSNRValue', 
                   'double', 
                   [])
    
    cls.add_method('GetSigma2', 
                   'double', 
                   [])
    
    cls.add_method('SetBitErrorRate', 
                   'void', 
                   [param('double', 'arg0')])
    
    cls.add_method('SetBlockErrorRate', 
                   'void', 
                   [param('double', 'arg0')])
    
    cls.add_method('SetI1', 
                   'void', 
                   [param('double', 'arg0')])
    
    cls.add_method('SetI2', 
                   'void', 
                   [param('double', 'arg0')])
    
    cls.add_method('SetSNRValue', 
                   'void', 
                   [param('double', 'arg0')])
    return

def register_Ns3SSRecord_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SSRecord const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Mac48Address', 'macAddress')])
    
    cls.add_constructor([param('ns3::Mac48Address', 'macAddress'), param('ns3::Ipv4Address', 'IPaddress')])
    
    cls.add_method('AddServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('DisablePollForRanging', 
                   'void', 
                   [])
    
    cls.add_method('EnablePollForRanging', 
                   'void', 
                   [])
    
    cls.add_method('GetAreServiceFlowsAllocated', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetBasicCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDsaRsp', 
                   'ns3::DsaRsp', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDsaRspRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHasServiceFlowBe', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHasServiceFlowNrtps', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHasServiceFlowRtps', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHasServiceFlowUgs', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetIPAddress', 
                   'ns3::Ipv4Address', 
                   [])
    
    cls.add_method('GetInvitedRangRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetIsBroadcastSS', 
                   'bool', 
                   [])
    
    cls.add_method('GetMacAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetModulationType', 
                   'ns3::WimaxPhy::ModulationType', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPollForRanging', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPollMeBit', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPrimaryCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangingCorrectionRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangingStatus', 
                   'ns3::WimaxNetDevice::RangingStatus', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetServiceFlows', 
                   'std::vector< ns3::ServiceFlow * >', 
                   [param('ns3::ServiceFlow::SchedulingType', 'schedulingType')], 
                   is_const=True)
    
    cls.add_method('GetSfTransactionId', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('IncrementDsaRspRetries', 
                   'void', 
                   [])
    
    cls.add_method('IncrementInvitedRangingRetries', 
                   'void', 
                   [])
    
    cls.add_method('IncrementRangingCorrectionRetries', 
                   'void', 
                   [])
    
    cls.add_method('ResetInvitedRangingRetries', 
                   'void', 
                   [])
    
    cls.add_method('ResetRangingCorrectionRetries', 
                   'void', 
                   [])
    
    cls.add_method('SetAreServiceFlowsAllocated', 
                   'void', 
                   [param('bool', 'val')])
    
    cls.add_method('SetBasicCid', 
                   'void', 
                   [param('ns3::Cid', 'basicCid')])
    
    cls.add_method('SetDsaRsp', 
                   'void', 
                   [param('ns3::DsaRsp', 'dsaRsp')])
    
    cls.add_method('SetDsaRspRetries', 
                   'void', 
                   [param('uint8_t', 'dsaRspRetries')])
    
    cls.add_method('SetIPAddress', 
                   'void', 
                   [param('ns3::Ipv4Address', 'IPaddress')])
    
    cls.add_method('SetIsBroadcastSS', 
                   'void', 
                   [param('bool', 'arg0')])
    
    cls.add_method('SetMacAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'macAddress')])
    
    cls.add_method('SetModulationType', 
                   'void', 
                   [param('ns3::WimaxPhy::ModulationType', 'modulationType')])
    
    cls.add_method('SetPollMeBit', 
                   'void', 
                   [param('bool', 'pollMeBit')])
    
    cls.add_method('SetPrimaryCid', 
                   'void', 
                   [param('ns3::Cid', 'primaryCid')])
    
    cls.add_method('SetRangingStatus', 
                   'void', 
                   [param('ns3::WimaxNetDevice::RangingStatus', 'rangingStatus')])
    
    cls.add_method('SetSfTransactionId', 
                   'void', 
                   [param('uint16_t', 'sfTransactionId')])
    return

def register_Ns3SeedManager_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SeedManager const &', 'arg0')])
    
    cls.add_method('CheckSeed', 
                   'bool', 
                   [param('uint32_t', 'seed')], 
                   is_static=True)
    
    cls.add_method('GetRun', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetSeed', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    
    cls.add_method('SetRun', 
                   'void', 
                   [param('uint32_t', 'run')], 
                   is_static=True)
    
    cls.add_method('SetSeed', 
                   'void', 
                   [param('uint32_t', 'seed')], 
                   is_static=True)
    return

def register_Ns3SendParams_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SendParams const &', 'arg0')])
    
    cls.add_constructor([])
    return

def register_Ns3SequentialVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SequentialVariable const &', 'arg0')])
    
    cls.add_constructor([param('double', 'f'), param('double', 'l'), param('double', 'i', default_value='1'), param('uint32_t', 'c', default_value='1')])
    
    cls.add_constructor([param('double', 'f'), param('double', 'l'), param('ns3::RandomVariable const &', 'i'), param('uint32_t', 'c', default_value='1')])
    return

def register_Ns3ServiceFlow_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Tlv', 'tlv')])
    
    cls.add_constructor([param('ns3::ServiceFlow::Direction', 'direction')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::ServiceFlow const &', 'sf')])
    
    cls.add_constructor([param('uint32_t', 'sfid'), param('ns3::ServiceFlow::Direction', 'direction'), param('ns3::Ptr< ns3::WimaxConnection >', 'connection')])
    
    cls.add_method('CheckClassifierMatch', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'srcAddress'), param('ns3::Ipv4Address', 'dstAddress'), param('uint16_t', 'srcPort'), param('uint16_t', 'dstPort'), param('uint8_t', 'proto')], 
                   is_const=True)
    
    cls.add_method('CleanUpQueue', 
                   'void', 
                   [])
    
    cls.add_method('CopyParametersFrom', 
                   'void', 
                   [param('ns3::ServiceFlow', 'sf')])
    
    cls.add_method('GetArqBlockLifeTime', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqBlockSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqDeliverInOrder', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqEnable', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqPurgeTimeout', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqRetryTimeoutRx', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqRetryTimeoutTx', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqSyncLoss', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetArqWindowSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetCid', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConvergenceSublayerParam', 
                   'ns3::CsParameters', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetCsSpecification', 
                   'ns3::ServiceFlow::CsSpecification', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDirection', 
                   'ns3::ServiceFlow::Direction', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFixedversusVariableSduIndicator', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetIsEnabled', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetIsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMaxSustainedTrafficRate', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMaxTrafficBurst', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMaximumLatency', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMinReservedTrafficRate', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMinTolerableTrafficRate', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetModulation', 
                   'ns3::WimaxPhy::ModulationType', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetQosParamSetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetQueue', 
                   'ns3::Ptr< ns3::WimaxMacQueue >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRecord', 
                   'ns3::ServiceFlowRecord *', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRequestTransmissionPolicy', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSchedulingType', 
                   'ns3::ServiceFlow::SchedulingType', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSchedulingTypeStr', 
                   'char *', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSduSize', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetServiceClassName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetServiceSchedulingType', 
                   'ns3::ServiceFlow::SchedulingType', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSfid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTargetSAID', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetToleratedJitter', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTrafficPriority', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetType', 
                   'ns3::ServiceFlow::Type', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUnsolicitedGrantInterval', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUnsolicitedPollingInterval', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('HasPackets', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('HasPackets', 
                   'bool', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')], 
                   is_const=True)
    
    cls.add_method('InitValues', 
                   'void', 
                   [])
    
    cls.add_method('PrintQoSParameters', 
                   'void', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetArqBlockLifeTime', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetArqBlockSize', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetArqDeliverInOrder', 
                   'void', 
                   [param('uint8_t', 'arg0')])
    
    cls.add_method('SetArqEnable', 
                   'void', 
                   [param('uint8_t', 'arg0')])
    
    cls.add_method('SetArqPurgeTimeout', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetArqRetryTimeoutRx', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetArqRetryTimeoutTx', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetArqSyncLoss', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetArqWindowSize', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetConnection', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxConnection >', 'connection')])
    
    cls.add_method('SetConvergenceSublayerParam', 
                   'void', 
                   [param('ns3::CsParameters', 'arg0')])
    
    cls.add_method('SetCsSpecification', 
                   'void', 
                   [param('ns3::ServiceFlow::CsSpecification', 'arg0')])
    
    cls.add_method('SetDirection', 
                   'void', 
                   [param('ns3::ServiceFlow::Direction', 'direction')])
    
    cls.add_method('SetFixedversusVariableSduIndicator', 
                   'void', 
                   [param('uint8_t', 'arg0')])
    
    cls.add_method('SetIsEnabled', 
                   'void', 
                   [param('bool', 'isEnabled')])
    
    cls.add_method('SetIsMulticast', 
                   'void', 
                   [param('bool', 'isMulticast')])
    
    cls.add_method('SetMaxSustainedTrafficRate', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetMaxTrafficBurst', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetMaximumLatency', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetMinReservedTrafficRate', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetMinTolerableTrafficRate', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetModulation', 
                   'void', 
                   [param('ns3::WimaxPhy::ModulationType', 'modulationType')])
    
    cls.add_method('SetQosParamSetType', 
                   'void', 
                   [param('uint8_t', 'arg0')])
    
    cls.add_method('SetRecord', 
                   'void', 
                   [param('ns3::ServiceFlowRecord *', 'record')])
    
    cls.add_method('SetRequestTransmissionPolicy', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetSduSize', 
                   'void', 
                   [param('uint8_t', 'arg0')])
    
    cls.add_method('SetServiceClassName', 
                   'void', 
                   [param('std::string', 'arg0')])
    
    cls.add_method('SetServiceSchedulingType', 
                   'void', 
                   [param('ns3::ServiceFlow::SchedulingType', 'arg0')])
    
    cls.add_method('SetSfid', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetTargetSAID', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetToleratedJitter', 
                   'void', 
                   [param('uint32_t', 'arg0')])
    
    cls.add_method('SetTrafficPriority', 
                   'void', 
                   [param('uint8_t', 'arg0')])
    
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::ServiceFlow::Type', 'type')])
    
    cls.add_method('SetUnsolicitedGrantInterval', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('SetUnsolicitedPollingInterval', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    
    cls.add_method('ToTlv', 
                   'ns3::Tlv', 
                   [], 
                   is_const=True)
    return

def register_Ns3ServiceFlowRecord_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ServiceFlowRecord const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetBacklogged', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetBackloggedTemp', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetBwSinceLastExpiry', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetBytesRcvd', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetBytesSent', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDlTimeStamp', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetGrantSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetGrantTimeStamp', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetGrantedBandwidth', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetGrantedBandwidthTemp', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetLastGrantTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPktsRcvd', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPktsSent', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRequestedBandwidth', 
                   'uint32_t', 
                   [])
    
    cls.add_method('IncreaseBacklogged', 
                   'void', 
                   [param('uint32_t', 'backlogged')])
    
    cls.add_method('IncreaseBackloggedTemp', 
                   'void', 
                   [param('uint32_t', 'backloggedTemp')])
    
    cls.add_method('SetBacklogged', 
                   'void', 
                   [param('uint32_t', 'backlogged')])
    
    cls.add_method('SetBackloggedTemp', 
                   'void', 
                   [param('uint32_t', 'backloggedTemp')])
    
    cls.add_method('SetBwSinceLastExpiry', 
                   'void', 
                   [param('uint32_t', 'bwSinceLastExpiry')])
    
    cls.add_method('SetBytesRcvd', 
                   'void', 
                   [param('uint32_t', 'bytesRcvd')])
    
    cls.add_method('SetBytesSent', 
                   'void', 
                   [param('uint32_t', 'bytesSent')])
    
    cls.add_method('SetDlTimeStamp', 
                   'void', 
                   [param('ns3::Time', 'dlTimeStamp')])
    
    cls.add_method('SetGrantSize', 
                   'void', 
                   [param('uint32_t', 'grantSize')])
    
    cls.add_method('SetGrantTimeStamp', 
                   'void', 
                   [param('ns3::Time', 'grantTimeStamp')])
    
    cls.add_method('SetGrantedBandwidth', 
                   'void', 
                   [param('uint32_t', 'grantedBandwidth')])
    
    cls.add_method('SetGrantedBandwidthTemp', 
                   'void', 
                   [param('uint32_t', 'grantedBandwidthTemp')])
    
    cls.add_method('SetLastGrantTime', 
                   'void', 
                   [param('ns3::Time', 'grantTime')])
    
    cls.add_method('SetPktsRcvd', 
                   'void', 
                   [param('uint32_t', 'pktsRcvd')])
    
    cls.add_method('SetPktsSent', 
                   'void', 
                   [param('uint32_t', 'pktsSent')])
    
    cls.add_method('SetRequestedBandwidth', 
                   'void', 
                   [param('uint32_t', 'requestedBandwidth')])
    
    cls.add_method('UpdateBwSinceLastExpiry', 
                   'void', 
                   [param('uint32_t', 'bwSinceLastExpiry')])
    
    cls.add_method('UpdateBytesRcvd', 
                   'void', 
                   [param('uint32_t', 'bytesRcvd')])
    
    cls.add_method('UpdateBytesSent', 
                   'void', 
                   [param('uint32_t', 'bytesSent')])
    
    cls.add_method('UpdateGrantedBandwidth', 
                   'void', 
                   [param('uint32_t', 'grantedBandwidth')])
    
    cls.add_method('UpdateGrantedBandwidthTemp', 
                   'void', 
                   [param('uint32_t', 'grantedBandwidthTemp')])
    
    cls.add_method('UpdatePktsRcvd', 
                   'void', 
                   [param('uint32_t', 'pktsRcvd')])
    
    cls.add_method('UpdatePktsSent', 
                   'void', 
                   [param('uint32_t', 'pktsSent')])
    
    cls.add_method('UpdateRequestedBandwidth', 
                   'void', 
                   [param('uint32_t', 'requestedBandwidth')])
    return

def register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3Simulator_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Simulator const &', 'arg0')])
    
    cls.add_method('Cancel', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    
    cls.add_method('Destroy', 
                   'void', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    
    cls.add_method('GetImplementation', 
                   'ns3::Ptr< ns3::SimulatorImpl >', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetMaximumSimulationTime', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsExpired', 
                   'bool', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    
    cls.add_method('IsFinished', 
                   'bool', 
                   [], 
                   is_static=True)
    
    cls.add_method('Next', 
                   'ns3::Time', 
                   [], 
                   is_static=True, deprecated=True)
    
    cls.add_method('Now', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    
    cls.add_method('RunOneEvent', 
                   'void', 
                   [], 
                   is_static=True, deprecated=True)
    
    cls.add_method('SetImplementation', 
                   'void', 
                   [param('ns3::Ptr< ns3::SimulatorImpl >', 'impl')], 
                   is_static=True)
    
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::ObjectFactory', 'schedulerFactory')], 
                   is_static=True)
    
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_static=True)
    
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time const &', 'time')], 
                   is_static=True)
    return

def register_Ns3Tag_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Tag const &', 'arg0')])
    
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TagBuffer_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::TagBuffer const &', 'arg0')])
    
    cls.add_constructor([param('uint8_t *', 'start'), param('uint8_t *', 'end')])
    
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('ns3::TagBuffer', 'o')])
    
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('ReadDouble', 
                   'double', 
                   [])
    
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    
    cls.add_method('TrimAtEnd', 
                   'void', 
                   [param('uint32_t', 'trim')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('WriteDouble', 
                   'void', 
                   [param('double', 'v')])
    
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'v')])
    
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'v')])
    return

def register_Ns3TlvValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TlvValue const &', 'arg0')])
    
    cls.add_method('Copy', 
                   'ns3::TlvValue *', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLen')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TosTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::TosTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint8_t', 'arg0'), param('uint8_t', 'arg1'), param('uint8_t', 'arg2')])
    
    cls.add_method('Copy', 
                   'ns3::TosTlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_virtual=True)
    
    cls.add_method('GetHigh', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLow', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMask', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3TriangularVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::TriangularVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 's'), param('double', 'l'), param('double', 'mean')])
    return

def register_Ns3TypeId_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([param('char const *', 'name')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TypeId const &', 'o')])
    
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')])
    
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('uint32_t', 'flags'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')])
    
    cls.add_method('AddTraceSource', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::Ptr< ns3::TraceSourceAccessor const >', 'accessor')])
    
    cls.add_method('GetAttribute', 
                   'ns3::TypeId::AttributeInformation', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    
    cls.add_method('GetAttributeFullName', 
                   'std::string', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    
    cls.add_method('GetAttributeN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConstructor', 
                   'ns3::Callback< ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetGroupName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetParent', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRegistered', 
                   'ns3::TypeId', 
                   [param('uint32_t', 'i')], 
                   is_static=True)
    
    cls.add_method('GetRegisteredN', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetTraceSource', 
                   'ns3::TypeId::TraceSourceInformation', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    
    cls.add_method('GetTraceSourceN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUid', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('HasConstructor', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('HasParent', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('HideFromDocumentation', 
                   'ns3::TypeId', 
                   [])
    
    cls.add_method('IsChildOf', 
                   'bool', 
                   [param('ns3::TypeId', 'other')], 
                   is_const=True)
    
    cls.add_method('LookupAttributeByName', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::TypeId::AttributeInformation *', 'info')], 
                   is_const=True)
    
    cls.add_method('LookupByName', 
                   'ns3::TypeId', 
                   [param('std::string', 'name')], 
                   is_static=True)
    
    cls.add_method('LookupTraceSourceByName', 
                   'ns3::Ptr< ns3::TraceSourceAccessor const >', 
                   [param('std::string', 'name')], 
                   is_const=True)
    
    cls.add_method('MustHideFromDocumentation', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetAttributeInitialValue', 
                   'bool', 
                   [param('uint32_t', 'i'), param('ns3::Ptr< ns3::AttributeValue const >', 'initialValue')])
    
    cls.add_method('SetGroupName', 
                   'ns3::TypeId', 
                   [param('std::string', 'groupName')])
    
    cls.add_method('SetParent', 
                   'ns3::TypeId', 
                   [param('ns3::TypeId', 'tid')])
    
    cls.add_method('SetUid', 
                   'void', 
                   [param('uint16_t', 'tid')])
    return

def register_Ns3TypeIdAttributeInformation_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TypeId::AttributeInformation const &', 'arg0')])
    
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::AttributeAccessor const >', is_const=False)
    
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    
    cls.add_instance_attribute('flags', 'uint32_t', is_const=False)
    
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    
    cls.add_instance_attribute('initialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    
    cls.add_instance_attribute('originalInitialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    return

def register_Ns3TypeIdTraceSourceInformation_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TypeId::TraceSourceInformation const &', 'arg0')])
    
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::TraceSourceAccessor const >', is_const=False)
    
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    return

def register_Ns3U16TlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::U16TlvValue const &', 'arg0')])
    
    cls.add_constructor([param('uint16_t', 'value')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::U16TlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLen')], 
                   is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetValue', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3U32TlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::U32TlvValue const &', 'arg0')])
    
    cls.add_constructor([param('uint32_t', 'value')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::U32TlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLen')], 
                   is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetValue', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3U8TlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::U8TlvValue const &', 'arg0')])
    
    cls.add_constructor([param('uint8_t', 'value')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::U8TlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLen')], 
                   is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetValue', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3UcdChannelEncodings_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::UcdChannelEncodings const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetBwReqOppSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrequency', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangReqOppSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Read', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    
    cls.add_method('SetBwReqOppSize', 
                   'void', 
                   [param('uint16_t', 'bwReqOppSize')])
    
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('uint32_t', 'frequency')])
    
    cls.add_method('SetRangReqOppSize', 
                   'void', 
                   [param('uint16_t', 'rangReqOppSize')])
    
    cls.add_method('Write', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    
    cls.add_method('DoRead', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoWrite', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3UniformVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::UniformVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 's'), param('double', 'l')])
    
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 's'), param('uint32_t', 'l')])
    
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 's'), param('double', 'l')])
    return

def register_Ns3VectorTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::VectorTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Tlv const &', 'val')])
    
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Tlv * const *, std::vector< ns3::Tlv * > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Copy', 
                   'ns3::VectorTlvValue *', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Tlv * const *, std::vector< ns3::Tlv * > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3WeibullVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::WeibullVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 'm')])
    
    cls.add_constructor([param('double', 'm'), param('double', 's')])
    
    cls.add_constructor([param('double', 'm'), param('double', 's'), param('double', 'b')])
    return

def register_Ns3WimaxHelper_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::WimaxHelper const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('CreateBSScheduler', 
                   'ns3::Ptr< ns3::BSScheduler >', 
                   [param('ns3::WimaxHelper::SchedulerType', 'schedulerType')])
    
    cls.add_method('CreatePhy', 
                   'ns3::Ptr< ns3::WimaxPhy >', 
                   [param('ns3::WimaxHelper::PhyType', 'phyType')])
    
    cls.add_method('CreatePhy', 
                   'ns3::Ptr< ns3::WimaxPhy >', 
                   [param('ns3::WimaxHelper::PhyType', 'phyType'), param('char *', 'SNRTraceFilePath'), param('bool', 'activateLoss')])
    
    cls.add_method('CreatePhyWithoutChannel', 
                   'ns3::Ptr< ns3::WimaxPhy >', 
                   [param('ns3::WimaxHelper::PhyType', 'phyType')])
    
    cls.add_method('CreatePhyWithoutChannel', 
                   'ns3::Ptr< ns3::WimaxPhy >', 
                   [param('ns3::WimaxHelper::PhyType', 'phyType'), param('char *', 'SNRTraceFilePath'), param('bool', 'activateLoss')])
    
    cls.add_method('CreateServiceFlow', 
                   'ns3::ServiceFlow', 
                   [param('ns3::ServiceFlow::Direction', 'direction'), param('ns3::ServiceFlow::SchedulingType', 'schedulinType'), param('ns3::IpcsClassifierRecord', 'classifier')])
    
    cls.add_method('CreateUplinkScheduler', 
                   'ns3::Ptr< ns3::UplinkScheduler >', 
                   [param('ns3::WimaxHelper::SchedulerType', 'schedulerType')])
    
    cls.add_method('EnableAsciiForConnection', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'oss'), param('uint32_t', 'nodeid'), param('uint32_t', 'deviceid'), param('char *', 'netdevice'), param('char *', 'connection')], 
                   is_static=True)
    
    cls.add_method('EnableLogComponents', 
                   'void', 
                   [], 
                   is_static=True)
    
    cls.add_method('Install', 
                   'ns3::NetDeviceContainer', 
                   [param('ns3::NodeContainer', 'c'), param('ns3::WimaxHelper::NetDeviceType', 'type'), param('ns3::WimaxHelper::PhyType', 'phyType'), param('ns3::WimaxHelper::SchedulerType', 'schedulerType')])
    
    cls.add_method('Install', 
                   'ns3::NetDeviceContainer', 
                   [param('ns3::NodeContainer', 'c'), param('ns3::WimaxHelper::NetDeviceType', 'deviceType'), param('ns3::WimaxHelper::PhyType', 'phyType'), param('ns3::Ptr< ns3::WimaxChannel >', 'channel'), param('ns3::WimaxHelper::SchedulerType', 'schedulerType')])
    
    cls.add_method('Install', 
                   'ns3::NetDeviceContainer', 
                   [param('ns3::NodeContainer', 'c'), param('ns3::WimaxHelper::NetDeviceType', 'deviceType'), param('ns3::WimaxHelper::PhyType', 'phyType'), param('ns3::WimaxHelper::SchedulerType', 'schedulerType'), param('double', 'frameDuration')])
    
    cls.add_method('Install', 
                   'ns3::Ptr< ns3::WimaxNetDevice >', 
                   [param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::WimaxHelper::NetDeviceType', 'deviceType'), param('ns3::WimaxHelper::PhyType', 'phyType'), param('ns3::Ptr< ns3::WimaxChannel >', 'channel'), param('ns3::WimaxHelper::SchedulerType', 'schedulerType')])
    
    cls.add_method('SetPropagationLossModel', 
                   'void', 
                   [param('ns3::SimpleOfdmWimaxChannel::PropModel', 'propagationModel')])
    
    cls.add_method('EnableAsciiInternal', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'explicitFilename')], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('EnablePcapInternal', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'explicitFilename'), param('bool', 'promiscuous')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3ZetaVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ZetaVariable const &', 'arg0')])
    
    cls.add_constructor([param('double', 'alpha')])
    
    cls.add_constructor([])
    return

def register_Ns3ZipfVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ZipfVariable const &', 'arg0')])
    
    cls.add_constructor([param('long int', 'N'), param('double', 'alpha')])
    
    cls.add_constructor([])
    return

def register_Ns3Empty_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::empty const &', 'arg0')])
    return

def register_Ns3Int64x64_t_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_inplace_numeric_operator('+=', param('ns3::int64x64_t const &', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short unsigned int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned char const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short int const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('signed char const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('double const', 'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short unsigned int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned char const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short int const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('signed char const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('double const', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short unsigned int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned char const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short int const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('signed char const', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('double const', 'right'))
    cls.add_unary_numeric_operator('-')
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long unsigned int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short unsigned int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('unsigned char const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long long int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('long int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('short int const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('signed char const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('double const', 'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', 'right'))
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_inplace_numeric_operator('*=', param('ns3::int64x64_t const &', 'right'))
    cls.add_inplace_numeric_operator('-=', param('ns3::int64x64_t const &', 'right'))
    cls.add_inplace_numeric_operator('/=', param('ns3::int64x64_t const &', 'right'))
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('>=')
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 'v')])
    
    cls.add_constructor([param('int', 'v')])
    
    cls.add_constructor([param('long int', 'v')])
    
    cls.add_constructor([param('long long int', 'v')])
    
    cls.add_constructor([param('unsigned int', 'v')])
    
    cls.add_constructor([param('long unsigned int', 'v')])
    
    cls.add_constructor([param('long long unsigned int', 'v')])
    
    cls.add_constructor([param('int64_t', 'hi'), param('uint64_t', 'lo')])
    
    cls.add_constructor([param('ns3::int64x64_t const &', 'o')])
    
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHigh', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLow', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Invert', 
                   'ns3::int64x64_t', 
                   [param('uint64_t', 'v')], 
                   is_static=True)
    
    cls.add_method('MulByInvert', 
                   'void', 
                   [param('ns3::int64x64_t const &', 'o')])
    return

def register_Ns3SimpleOfdmSendParam_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::simpleOfdmSendParam const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::bvec const &', 'fecBlock'), param('uint32_t', 'burstSize'), param('bool', 'isFirstBlock'), param('uint64_t', 'Frequency'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint8_t', 'direction'), param('double', 'rxPowerDbm')])
    
    cls.add_constructor([param('uint32_t', 'burstSize'), param('bool', 'isFirstBlock'), param('uint64_t', 'Frequency'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint8_t', 'direction'), param('double', 'rxPowerDbm'), param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('GetBurst', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [])
    
    cls.add_method('GetBurstSize', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetDirection', 
                   'uint8_t', 
                   [])
    
    cls.add_method('GetFecBlock', 
                   'ns3::bvec', 
                   [])
    
    cls.add_method('GetFrequency', 
                   'uint64_t', 
                   [])
    
    cls.add_method('GetIsFirstBlock', 
                   'bool', 
                   [])
    
    cls.add_method('GetModulationType', 
                   'ns3::WimaxPhy::ModulationType', 
                   [])
    
    cls.add_method('GetRxPowerDbm', 
                   'double', 
                   [])
    
    cls.add_method('SetBurstSize', 
                   'void', 
                   [param('uint32_t', 'burstSize')])
    
    cls.add_method('SetDirection', 
                   'void', 
                   [param('uint8_t', 'direction')])
    
    cls.add_method('SetFecBlock', 
                   'void', 
                   [param('ns3::bvec const &', 'fecBlock')])
    
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('uint64_t', 'Frequency')])
    
    cls.add_method('SetIsFirstBlock', 
                   'void', 
                   [param('bool', 'isFirstBlock')])
    
    cls.add_method('SetModulationType', 
                   'void', 
                   [param('ns3::WimaxPhy::ModulationType', 'modulationType')])
    
    cls.add_method('SetRxPowerDbm', 
                   'void', 
                   [param('double', 'rxPowerDbm')])
    return

def register_Ns3Chunk_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Chunk const &', 'arg0')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3ClassificationRuleVectorTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ClassificationRuleVectorTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::ClassificationRuleVectorTlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_virtual=True)
    return

def register_Ns3ConstantVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ConstantVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 'c')])
    
    cls.add_method('SetConstant', 
                   'void', 
                   [param('double', 'c')])
    return

def register_Ns3CsParamVectorTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::CsParamVectorTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::CsParamVectorTlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_virtual=True)
    return

def register_Ns3DeterministicVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::DeterministicVariable const &', 'arg0')])
    
    cls.add_constructor([param('double *', 'd'), param('uint32_t', 'c')])
    return

def register_Ns3EmpiricalVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::EmpiricalVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('CDF', 
                   'void', 
                   [param('double', 'v'), param('double', 'c')])
    return

def register_Ns3ErlangVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ErlangVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('unsigned int', 'k'), param('double', 'lambda')])
    
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetValue', 
                   'double', 
                   [param('unsigned int', 'k'), param('double', 'lambda')], 
                   is_const=True)
    return

def register_Ns3ExponentialVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ExponentialVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 'm')])
    
    cls.add_constructor([param('double', 'm'), param('double', 'b')])
    return

def register_Ns3GammaVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::GammaVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 'alpha'), param('double', 'beta')])
    
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'alpha'), param('double', 'beta')], 
                   is_const=True)
    return

def register_Ns3Header_methods(root_module, cls):
    cls.add_output_stream_operator()
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Header const &', 'arg0')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3IntEmpiricalVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::IntEmpiricalVariable const &', 'arg0')])
    
    cls.add_constructor([])
    return

def register_Ns3Ipv4AddressTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Ipv4AddressTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ipv4Address', 'address'), param('ns3::Ipv4Mask', 'Mask')])
    
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ipv4AddressTlvValue::ipv4Addr const *, std::vector< ns3::Ipv4AddressTlvValue::ipv4Addr > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Copy', 
                   'ns3::Ipv4AddressTlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_virtual=True)
    
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ipv4AddressTlvValue::ipv4Addr const *, std::vector< ns3::Ipv4AddressTlvValue::ipv4Addr > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3Ipv4AddressTlvValueIpv4Addr_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv4AddressTlvValue::ipv4Addr const &', 'arg0')])
    
    cls.add_instance_attribute('Address', 'ns3::Ipv4Address', is_const=False)
    
    cls.add_instance_attribute('Mask', 'ns3::Ipv4Mask', is_const=False)
    return

def register_Ns3LogNormalVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::LogNormalVariable const &', 'arg0')])
    
    cls.add_constructor([param('double', 'mu'), param('double', 'sigma')])
    return

def register_Ns3MacHeaderType_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::MacHeaderType const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint8_t', 'type')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    return

def register_Ns3ManagementMessageType_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ManagementMessageType const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint8_t', 'type')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    return

def register_Ns3NormalVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::NormalVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 'm'), param('double', 'v')])
    
    cls.add_constructor([param('double', 'm'), param('double', 'v'), param('double', 'b')])
    return

def register_Ns3Object_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_method('AggregateObject', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'other')])
    
    cls.add_method('Dispose', 
                   'void', 
                   [])
    
    cls.add_method('GetAggregateIterator', 
                   'ns3::Object::AggregateIterator', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Start', 
                   'void', 
                   [])
    
    cls.add_constructor([param('ns3::Object const &', 'o')], 
                        visibility='protected')
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    
    cls.add_method('DoStart', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectAggregateIterator_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Object::AggregateIterator const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Next', 
                   'ns3::Ptr< ns3::Object const >', 
                   [])
    return

def register_Ns3OfdmDownlinkFramePrefix_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmDownlinkFramePrefix const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddDlFramePrefixElement', 
                   'void', 
                   [param('ns3::DlFramePrefixIe', 'dlFramePrefixElement')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetBaseStationId', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConfigurationChangeCount', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDlFramePrefixElements', 
                   'std::vector< ns3::DlFramePrefixIe >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrameNumber', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHcs', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetBaseStationId', 
                   'void', 
                   [param('ns3::Mac48Address', 'baseStationId')])
    
    cls.add_method('SetConfigurationChangeCount', 
                   'void', 
                   [param('uint8_t', 'configurationChangeCount')])
    
    cls.add_method('SetFrameNumber', 
                   'void', 
                   [param('uint32_t', 'frameNumber')])
    
    cls.add_method('SetHcs', 
                   'void', 
                   [param('uint8_t', 'hcs')])
    return

def register_Ns3OfdmSendParams_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmSendParams const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Ptr< ns3::PacketBurst >', 'burst'), param('uint8_t', 'modulationType'), param('uint8_t', 'direction')])
    
    cls.add_method('GetBurst', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDirection', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetModulationType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3OfdmUcdChannelEncodings_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OfdmUcdChannelEncodings const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetSbchnlFocContCodes', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSbchnlReqRegionFullParams', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetSbchnlFocContCodes', 
                   'void', 
                   [param('uint8_t', 'sbchnlFocContCodes')])
    
    cls.add_method('SetSbchnlReqRegionFullParams', 
                   'void', 
                   [param('uint8_t', 'sbchnlReqRegionFullParams')])
    
    cls.add_method('DoRead', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoWrite', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3PacketBurst_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PacketBurst const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')])
    
    cls.add_method('Begin', 
                   'std::_List_const_iterator< ns3::Ptr< ns3::Packet > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [], 
                   is_const=True)
    
    cls.add_method('End', 
                   'std::_List_const_iterator< ns3::Ptr< ns3::Packet > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNPackets', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPackets', 
                   'std::list< ns3::Ptr< ns3::Packet > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3ParetoVariable_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ParetoVariable const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('double', 'm')])
    
    cls.add_constructor([param('double', 'm'), param('double', 's')])
    
    cls.add_constructor([param('double', 'm'), param('double', 's'), param('double', 'b')])
    
    cls.add_constructor([param('std::pair< double, double >', 'params')])
    
    cls.add_constructor([param('std::pair< double, double >', 'params'), param('double', 'b')])
    return

def register_Ns3PcapFileWrapper_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('Fail', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Eof', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Clear', 
                   'void', 
                   [])
    
    cls.add_method('Open', 
                   'void', 
                   [param('std::string const &', 'filename'), param('std::_Ios_Openmode', 'mode')])
    
    cls.add_method('Close', 
                   'void', 
                   [])
    
    cls.add_method('Init', 
                   'void', 
                   [param('uint32_t', 'dataLinkType'), param('uint32_t', 'snapLen', default_value='std::numeric_limits<unsigned int>::max()'), param('int32_t', 'tzCorrection', default_value='ns3::PcapFile::ZONE_DEFAULT')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Time', 't'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Time', 't'), param('ns3::Header &', 'header'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Time', 't'), param('uint8_t const *', 'buffer'), param('uint32_t', 'length')])
    
    cls.add_method('GetMagic', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetVersionMajor', 
                   'uint16_t', 
                   [])
    
    cls.add_method('GetVersionMinor', 
                   'uint16_t', 
                   [])
    
    cls.add_method('GetTimeZoneOffset', 
                   'int32_t', 
                   [])
    
    cls.add_method('GetSigFigs', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetSnapLen', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetDataLinkType', 
                   'uint32_t', 
                   [])
    return

def register_Ns3PortRangeTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PortRangeTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Add', 
                   'void', 
                   [param('uint16_t', 'portLow'), param('uint16_t', 'portHigh')])
    
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::PortRangeTlvValue::PortRange const *, std::vector< ns3::PortRangeTlvValue::PortRange > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Copy', 
                   'ns3::PortRangeTlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_virtual=True)
    
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::PortRangeTlvValue::PortRange const *, std::vector< ns3::PortRangeTlvValue::PortRange > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3PortRangeTlvValuePortRange_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::PortRangeTlvValue::PortRange const &', 'arg0')])
    
    cls.add_instance_attribute('PortHigh', 'uint16_t', is_const=False)
    
    cls.add_instance_attribute('PortLow', 'uint16_t', is_const=False)
    return

def register_Ns3PriorityUlJob_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::PriorityUlJob const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetPriority', 
                   'int', 
                   [])
    
    cls.add_method('GetUlJob', 
                   'ns3::Ptr< ns3::UlJob >', 
                   [])
    
    cls.add_method('SetPriority', 
                   'void', 
                   [param('int', 'priority')])
    
    cls.add_method('SetUlJob', 
                   'void', 
                   [param('ns3::Ptr< ns3::UlJob >', 'job')])
    return

def register_Ns3PropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('SetNext', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationLossModel >', 'next')])
    
    cls.add_method('CalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True)
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3ProtocolTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ProtocolTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Add', 
                   'void', 
                   [param('uint8_t', 'protiocol')])
    
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< unsigned char const *, std::vector< unsigned char > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Copy', 
                   'ns3::ProtocolTlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_virtual=True)
    
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< unsigned char const *, std::vector< unsigned char > >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3RandomPropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3RangePropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3RngReq_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::RngReq const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetMacAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangingAnomalies', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetReqDlBurstProfile', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('PrintDebug', 
                   'void', 
                   [], 
                   is_const=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetMacAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'macAddress')])
    
    cls.add_method('SetRangingAnomalies', 
                   'void', 
                   [param('uint8_t', 'rangingAnomalies')])
    
    cls.add_method('SetReqDlBurstProfile', 
                   'void', 
                   [param('uint8_t', 'reqDlBurstProfile')])
    return

def register_Ns3RngRsp_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::RngRsp const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetAasBdcastPermission', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetBasicCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDlFreqOverride', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDlOperBurstProfile', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrameNumber', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInitRangOppNumber', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetMacAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetOffsetFreqAdjust', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPowerLevelAdjust', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPrimaryCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangStatus', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangSubchnl', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTimingAdjust', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetUlChnlIdOverride', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetAasBdcastPermission', 
                   'void', 
                   [param('uint8_t', 'aasBdcastPermission')])
    
    cls.add_method('SetBasicCid', 
                   'void', 
                   [param('ns3::Cid', 'basicCid')])
    
    cls.add_method('SetDlFreqOverride', 
                   'void', 
                   [param('uint32_t', 'dlFreqOverride')])
    
    cls.add_method('SetDlOperBurstProfile', 
                   'void', 
                   [param('uint16_t', 'dlOperBurstProfile')])
    
    cls.add_method('SetFrameNumber', 
                   'void', 
                   [param('uint32_t', 'frameNumber')])
    
    cls.add_method('SetInitRangOppNumber', 
                   'void', 
                   [param('uint8_t', 'initRangOppNumber')])
    
    cls.add_method('SetMacAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'macAddress')])
    
    cls.add_method('SetOffsetFreqAdjust', 
                   'void', 
                   [param('uint32_t', 'offsetFreqAdjust')])
    
    cls.add_method('SetPowerLevelAdjust', 
                   'void', 
                   [param('uint8_t', 'powerLevelAdjust')])
    
    cls.add_method('SetPrimaryCid', 
                   'void', 
                   [param('ns3::Cid', 'primaryCid')])
    
    cls.add_method('SetRangStatus', 
                   'void', 
                   [param('uint8_t', 'rangStatus')])
    
    cls.add_method('SetRangSubchnl', 
                   'void', 
                   [param('uint8_t', 'rangSubchnl')])
    
    cls.add_method('SetTimingAdjust', 
                   'void', 
                   [param('uint32_t', 'timingAdjust')])
    
    cls.add_method('SetUlChnlIdOverride', 
                   'void', 
                   [param('uint8_t', 'ulChnlIdOverride')])
    return

def register_Ns3SSManager_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SSManager const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('CreateSSRecord', 
                   'ns3::SSRecord *', 
                   [param('ns3::Mac48Address const &', 'macAddress')])
    
    cls.add_method('DeleteSSRecord', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('GetMacAddress', 
                   'ns3::Mac48Address', 
                   [param('ns3::Cid', 'cid')], 
                   is_const=True)
    
    cls.add_method('GetNRegisteredSSs', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNSSs', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSSRecord', 
                   'ns3::SSRecord *', 
                   [param('ns3::Mac48Address const &', 'macAddress')], 
                   is_const=True)
    
    cls.add_method('GetSSRecord', 
                   'ns3::SSRecord *', 
                   [param('ns3::Cid', 'cid')], 
                   is_const=True)
    
    cls.add_method('GetSSRecords', 
                   'std::vector< ns3::SSRecord * > *', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsInRecord', 
                   'bool', 
                   [param('ns3::Mac48Address const &', 'macAddress')], 
                   is_const=True)
    
    cls.add_method('IsRegistered', 
                   'bool', 
                   [param('ns3::Mac48Address const &', 'macAddress')], 
                   is_const=True)
    return

def register_Ns3ServiceFlowManager_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ServiceFlowManager const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('AreServiceFlowsAllocated', 
                   'bool', 
                   [])
    
    cls.add_method('AreServiceFlowsAllocated', 
                   'bool', 
                   [param('std::vector< ns3::ServiceFlow * > *', 'serviceFlows')])
    
    cls.add_method('AreServiceFlowsAllocated', 
                   'bool', 
                   [param('std::vector< ns3::ServiceFlow * >', 'serviceFlows')])
    
    cls.add_method('DoClassify', 
                   'ns3::ServiceFlow *', 
                   [param('ns3::Ipv4Address', 'SrcAddress'), param('ns3::Ipv4Address', 'DstAddress'), param('uint16_t', 'SrcPort'), param('uint16_t', 'DstPort'), param('uint8_t', 'Proto'), param('ns3::ServiceFlow::Direction', 'dir')], 
                   is_const=True)
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetNextServiceFlowToAllocate', 
                   'ns3::ServiceFlow *', 
                   [])
    
    cls.add_method('GetNrServiceFlows', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow *', 
                   [param('uint32_t', 'sfid')], 
                   is_const=True)
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow *', 
                   [param('ns3::Cid', 'cid')], 
                   is_const=True)
    
    cls.add_method('GetServiceFlows', 
                   'std::vector< ns3::ServiceFlow * >', 
                   [param('ns3::ServiceFlow::SchedulingType', 'schedulingType')], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3SfVectorTlvValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SfVectorTlvValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::SfVectorTlvValue *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint64_t', 'valueLength')], 
                   is_virtual=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter< ns3::AttributeAccessor > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter< ns3::AttributeChecker > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter< ns3::AttributeValue > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter< ns3::CallbackImplBase > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter< ns3::EventImpl > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter< ns3::NixVector > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3OutputStreamWrapper_Ns3Empty_Ns3DefaultDeleter__lt__ns3OutputStreamWrapper__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter< ns3::OutputStreamWrapper > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter< ns3::Packet > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter< ns3::TraceSourceAccessor > > const &', 'o')])
    
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SsServiceFlowManager_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SsServiceFlowManager const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Ptr< ns3::SubscriberStationNetDevice >', 'device')])
    
    cls.add_method('AddServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('AddServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow', 'serviceFlow')])
    
    cls.add_method('CreateDsaAck', 
                   'ns3::Ptr< ns3::Packet >', 
                   [])
    
    cls.add_method('CreateDsaReq', 
                   'ns3::DsaReq', 
                   [param('ns3::ServiceFlow const *', 'serviceFlow')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetDsaAckTimeoutEvent', 
                   'ns3::EventId', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDsaRspTimeoutEvent', 
                   'ns3::EventId', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMaxDsaReqRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('InitiateServiceFlows', 
                   'void', 
                   [])
    
    cls.add_method('ProcessDsaRsp', 
                   'void', 
                   [param('ns3::DsaRsp const &', 'dsaRsp')])
    
    cls.add_method('ScheduleDsaReq', 
                   'void', 
                   [param('ns3::ServiceFlow const *', 'serviceFlow')])
    
    cls.add_method('SetMaxDsaReqRetries', 
                   'void', 
                   [param('uint8_t', 'maxDsaReqRetries')])
    return

def register_Ns3ThreeLogDistancePropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3Time_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_inplace_numeric_operator('+=', param('ns3::Time const &', 'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', 'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', 'right'))
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_inplace_numeric_operator('-=', param('ns3::Time const &', 'right'))
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('>=')
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Time const &', 'o')])
    
    cls.add_constructor([param('double', 'v')])
    
    cls.add_constructor([param('int', 'v')])
    
    cls.add_constructor([param('long int', 'v')])
    
    cls.add_constructor([param('long long int', 'v')])
    
    cls.add_constructor([param('unsigned int', 'v')])
    
    cls.add_constructor([param('long unsigned int', 'v')])
    
    cls.add_constructor([param('long long unsigned int', 'v')])
    
    cls.add_constructor([param('std::string const &', 's')])
    
    cls.add_constructor([param('ns3::int64x64_t const &', 'value')])
    
    cls.add_method('Compare', 
                   'int', 
                   [param('ns3::Time const &', 'o')], 
                   is_const=True)
    
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'from'), param('ns3::Time::Unit', 'timeUnit')], 
                   is_static=True)
    
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'value')], 
                   is_static=True)
    
    cls.add_method('FromDouble', 
                   'ns3::Time', 
                   [param('double', 'value'), param('ns3::Time::Unit', 'timeUnit')], 
                   is_static=True)
    
    cls.add_method('FromInteger', 
                   'ns3::Time', 
                   [param('uint64_t', 'value'), param('ns3::Time::Unit', 'timeUnit')], 
                   is_static=True)
    
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFemtoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInteger', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMicroSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMilliSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNanoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPicoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetResolution', 
                   'ns3::Time::Unit', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetSeconds', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTimeStep', 
                   'int64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsStrictlyNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsStrictlyPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsZero', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetResolution', 
                   'void', 
                   [param('ns3::Time::Unit', 'resolution')], 
                   is_static=True)
    
    cls.add_method('To', 
                   'ns3::int64x64_t', 
                   [param('ns3::Time::Unit', 'timeUnit')], 
                   is_const=True)
    
    cls.add_method('ToDouble', 
                   'double', 
                   [param('ns3::Time::Unit', 'timeUnit')], 
                   is_const=True)
    
    cls.add_method('ToInteger', 
                   'int64_t', 
                   [param('ns3::Time::Unit', 'timeUnit')], 
                   is_const=True)
    return

def register_Ns3Tlv_methods(root_module, cls):
    
    cls.add_constructor([param('uint8_t', 'type'), param('uint64_t', 'length'), param('ns3::TlvValue const &', 'value')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Tlv const &', 'tlv')])
    
    cls.add_method('Copy', 
                   'ns3::Tlv *', 
                   [], 
                   is_const=True)
    
    cls.add_method('CopyValue', 
                   'ns3::TlvValue *', 
                   [], 
                   is_const=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetLength', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetSizeOfLen', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('PeekValue', 
                   'ns3::TlvValue *', 
                   [])
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3TraceSourceAccessor_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::TraceSourceAccessor const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Connect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('ConnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Disconnect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('DisconnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Trailer_methods(root_module, cls):
    cls.add_output_stream_operator()
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Trailer const &', 'arg0')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'end')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TwoRayGroundPropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('SetLambda', 
                   'void', 
                   [param('double', 'frequency'), param('double', 'speed')])
    
    cls.add_method('SetLambda', 
                   'void', 
                   [param('double', 'lambda')])
    
    cls.add_method('SetSystemLoss', 
                   'void', 
                   [param('double', 'systemLoss')])
    
    cls.add_method('SetMinDistance', 
                   'void', 
                   [param('double', 'minDistance')])
    
    cls.add_method('GetMinDistance', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLambda', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSystemLoss', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetHeightAboveZ', 
                   'void', 
                   [param('double', 'heightAboveZ')])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3Ucd_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Ucd const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddUlBurstProfile', 
                   'void', 
                   [param('ns3::OfdmUlBurstProfile', 'ulBurstProfile')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetChannelEncodings', 
                   'ns3::OfdmUcdChannelEncodings', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConfigurationChangeCount', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNrUlBurstProfiles', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangingBackoffEnd', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangingBackoffStart', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRequestBackoffEnd', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRequestBackoffStart', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetUlBurstProfiles', 
                   'std::vector< ns3::OfdmUlBurstProfile >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetChannelEncodings', 
                   'void', 
                   [param('ns3::OfdmUcdChannelEncodings', 'channelEncodings')])
    
    cls.add_method('SetConfigurationChangeCount', 
                   'void', 
                   [param('uint8_t', 'ucdCount')])
    
    cls.add_method('SetNrUlBurstProfiles', 
                   'void', 
                   [param('uint8_t', 'nrUlBurstProfiles')])
    
    cls.add_method('SetRangingBackoffEnd', 
                   'void', 
                   [param('uint8_t', 'rangingBackoffEnd')])
    
    cls.add_method('SetRangingBackoffStart', 
                   'void', 
                   [param('uint8_t', 'rangingBackoffStart')])
    
    cls.add_method('SetRequestBackoffEnd', 
                   'void', 
                   [param('uint8_t', 'requestBackoffEnd')])
    
    cls.add_method('SetRequestBackoffStart', 
                   'void', 
                   [param('uint8_t', 'requestBackoffStart')])
    return

def register_Ns3UlJob_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    
    cls.add_constructor([param('ns3::UlJob const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetDeadline', 
                   'ns3::Time', 
                   [])
    
    cls.add_method('GetPeriod', 
                   'ns3::Time', 
                   [])
    
    cls.add_method('GetReleaseTime', 
                   'ns3::Time', 
                   [])
    
    cls.add_method('GetSchedulingType', 
                   'ns3::ServiceFlow::SchedulingType', 
                   [])
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow *', 
                   [])
    
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetSsRecord', 
                   'ns3::SSRecord *', 
                   [])
    
    cls.add_method('GetType', 
                   'ns3::ReqType', 
                   [])
    
    cls.add_method('SetDeadline', 
                   'void', 
                   [param('ns3::Time', 'deadline')])
    
    cls.add_method('SetPeriod', 
                   'void', 
                   [param('ns3::Time', 'period')])
    
    cls.add_method('SetReleaseTime', 
                   'void', 
                   [param('ns3::Time', 'releaseTime')])
    
    cls.add_method('SetSchedulingType', 
                   'void', 
                   [param('ns3::ServiceFlow::SchedulingType', 'schedulingType')])
    
    cls.add_method('SetServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('SetSize', 
                   'void', 
                   [param('uint32_t', 'size')])
    
    cls.add_method('SetSsRecord', 
                   'void', 
                   [param('ns3::SSRecord *', 'ssRecord')])
    
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::ReqType', 'type')])
    return

def register_Ns3UlMap_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::UlMap const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddUlMapElement', 
                   'void', 
                   [param('ns3::OfdmUlMapIe', 'ulMapElement')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetAllocationStartTime', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetUcdCount', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUlMapElements', 
                   'std::list< ns3::OfdmUlMapIe >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetAllocationStartTime', 
                   'void', 
                   [param('uint32_t', 'allocationStartTime')])
    
    cls.add_method('SetUcdCount', 
                   'void', 
                   [param('uint8_t', 'ucdCount')])
    return

def register_Ns3UplinkScheduler_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::UplinkScheduler const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')])
    
    cls.add_method('AddUplinkAllocation', 
                   'void', 
                   [param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('uint32_t const &', 'allocationSize'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('AllocateInitialRangingInterval', 
                   'void', 
                   [param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('CalculateAllocationStartTime', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetBs', 
                   'ns3::Ptr< ns3::BaseStationNetDevice >', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetChannelDescriptorsToUpdate', 
                   'void', 
                   [param('bool &', 'arg0'), param('bool &', 'arg1'), param('bool &', 'arg2'), param('bool &', 'arg3')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetDcdTimeStamp', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetIsInvIrIntrvlAllocated', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetIsIrIntrvlAllocated', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetNrIrOppsAllocated', 
                   'uint8_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTimeStampIrInterval', 
                   'ns3::Time', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetUcdTimeStamp', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetUplinkAllocations', 
                   'std::list< ns3::OfdmUlMapIe >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('InitOnce', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('OnSetRequestedBandwidth', 
                   'void', 
                   [param('ns3::ServiceFlowRecord *', 'sfr')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('ProcessBandwidthRequest', 
                   'void', 
                   [param('ns3::BandwidthRequestHeader const &', 'bwRequestHdr')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('Schedule', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'bool', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('ServiceUnsolicitedGrants', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetBs', 
                   'void', 
                   [param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')], 
                   is_virtual=True)
    
    cls.add_method('SetDcdTimeStamp', 
                   'void', 
                   [param('ns3::Time', 'dcdTimeStamp')], 
                   is_virtual=True)
    
    cls.add_method('SetIsInvIrIntrvlAllocated', 
                   'void', 
                   [param('bool', 'isInvIrIntrvlAllocated')], 
                   is_virtual=True)
    
    cls.add_method('SetIsIrIntrvlAllocated', 
                   'void', 
                   [param('bool', 'isIrIntrvlAllocated')], 
                   is_virtual=True)
    
    cls.add_method('SetNrIrOppsAllocated', 
                   'void', 
                   [param('uint8_t', 'nrIrOppsAllocated')], 
                   is_virtual=True)
    
    cls.add_method('SetTimeStampIrInterval', 
                   'void', 
                   [param('ns3::Time', 'timeStampIrInterval')], 
                   is_virtual=True)
    
    cls.add_method('SetUcdTimeStamp', 
                   'void', 
                   [param('ns3::Time', 'ucdTimeStamp')], 
                   is_virtual=True)
    
    cls.add_method('SetupServiceFlow', 
                   'void', 
                   [param('ns3::SSRecord *', 'ssRecord'), param('ns3::ServiceFlow *', 'serviceFlow')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3UplinkSchedulerMBQoS_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::UplinkSchedulerMBQoS const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Time', 'time')])
    
    cls.add_method('AddUplinkAllocation', 
                   'void', 
                   [param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('uint32_t const &', 'allocationSize'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('AllocateInitialRangingInterval', 
                   'void', 
                   [param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('CalculateAllocationStartTime', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('CheckDeadline', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('CheckMinimumBandwidth', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('CountSymbolsJobs', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::UlJob >', 'job')])
    
    cls.add_method('CountSymbolsQueue', 
                   'uint32_t', 
                   [param('std::list< ns3::Ptr< ns3::UlJob > >', 'jobs')])
    
    cls.add_method('CreateUlJob', 
                   'ns3::Ptr< ns3::UlJob >', 
                   [param('ns3::SSRecord *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedType'), param('ns3::ReqType', 'reqType')])
    
    cls.add_method('DequeueJob', 
                   'ns3::Ptr< ns3::UlJob >', 
                   [param('ns3::UlJob::JobPriority', 'priority')])
    
    cls.add_method('DetermineDeadline', 
                   'ns3::Time', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('EnqueueJob', 
                   'void', 
                   [param('ns3::UlJob::JobPriority', 'priority'), param('ns3::Ptr< ns3::UlJob >', 'job')])
    
    cls.add_method('GetChannelDescriptorsToUpdate', 
                   'void', 
                   [param('bool &', 'arg0'), param('bool &', 'arg1'), param('bool &', 'arg2'), param('bool &', 'arg3')], 
                   is_virtual=True)
    
    cls.add_method('GetPendingSize', 
                   'uint32_t', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetUplinkAllocations', 
                   'std::list< ns3::OfdmUlMapIe >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('InitOnce', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('OnSetRequestedBandwidth', 
                   'void', 
                   [param('ns3::ServiceFlowRecord *', 'sfr')], 
                   is_virtual=True)
    
    cls.add_method('ProcessBandwidthRequest', 
                   'void', 
                   [param('ns3::BandwidthRequestHeader const &', 'bwRequestHdr')], 
                   is_virtual=True)
    
    cls.add_method('Schedule', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'bool', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequestsBytes', 
                   'bool', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols'), param('uint32_t', 'allocationSizeBytes')])
    
    cls.add_method('ServiceUnsolicitedGrants', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('SetupServiceFlow', 
                   'void', 
                   [param('ns3::SSRecord *', 'ssRecord'), param('ns3::ServiceFlow *', 'serviceFlow')], 
                   is_virtual=True)
    
    cls.add_method('UplinkSchedWindowTimer', 
                   'void', 
                   [])
    return

def register_Ns3UplinkSchedulerRtps_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::UplinkSchedulerRtps const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')])
    
    cls.add_method('AddUplinkAllocation', 
                   'void', 
                   [param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('uint32_t const &', 'allocationSize'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('AllocateInitialRangingInterval', 
                   'void', 
                   [param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('CalculateAllocationStartTime', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetChannelDescriptorsToUpdate', 
                   'void', 
                   [param('bool &', 'arg0'), param('bool &', 'arg1'), param('bool &', 'arg2'), param('bool &', 'arg3')], 
                   is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetUplinkAllocations', 
                   'std::list< ns3::OfdmUlMapIe >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('InitOnce', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('OnSetRequestedBandwidth', 
                   'void', 
                   [param('ns3::ServiceFlowRecord *', 'sfr')], 
                   is_virtual=True)
    
    cls.add_method('ProcessBandwidthRequest', 
                   'void', 
                   [param('ns3::BandwidthRequestHeader const &', 'bwRequestHdr')], 
                   is_virtual=True)
    
    cls.add_method('Schedule', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'bool', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('ServiceUnsolicitedGrants', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('SetupServiceFlow', 
                   'void', 
                   [param('ns3::SSRecord *', 'ssRecord'), param('ns3::ServiceFlow *', 'serviceFlow')], 
                   is_virtual=True)
    
    cls.add_method('ULSchedulerRTPSConnection', 
                   'void', 
                   [param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')])
    return

def register_Ns3UplinkSchedulerSimple_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::UplinkSchedulerSimple const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')])
    
    cls.add_method('AddUplinkAllocation', 
                   'void', 
                   [param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('uint32_t const &', 'allocationSize'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('AllocateInitialRangingInterval', 
                   'void', 
                   [param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('CalculateAllocationStartTime', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetChannelDescriptorsToUpdate', 
                   'void', 
                   [param('bool &', 'arg0'), param('bool &', 'arg1'), param('bool &', 'arg2'), param('bool &', 'arg3')], 
                   is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetUplinkAllocations', 
                   'std::list< ns3::OfdmUlMapIe >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('InitOnce', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('OnSetRequestedBandwidth', 
                   'void', 
                   [param('ns3::ServiceFlowRecord *', 'sfr')], 
                   is_virtual=True)
    
    cls.add_method('ProcessBandwidthRequest', 
                   'void', 
                   [param('ns3::BandwidthRequestHeader const &', 'bwRequestHdr')], 
                   is_virtual=True)
    
    cls.add_method('Schedule', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('ServiceBandwidthRequests', 
                   'bool', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('ServiceUnsolicitedGrants', 
                   'void', 
                   [param('ns3::SSRecord const *', 'ssRecord'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType'), param('ns3::OfdmUlMapIe &', 'ulMapIe'), param('ns3::WimaxPhy::ModulationType const', 'modulationType'), param('uint32_t &', 'symbolsToAllocation'), param('uint32_t &', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('SetupServiceFlow', 
                   'void', 
                   [param('ns3::SSRecord *', 'ssRecord'), param('ns3::ServiceFlow *', 'serviceFlow')], 
                   is_virtual=True)
    return

def register_Ns3WimaxConnection_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::WimaxConnection const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Cid', 'cid'), param('ns3::Cid::Type', 'type')])
    
    cls.add_method('ClearFragmentsQueue', 
                   'void', 
                   [])
    
    cls.add_method('Dequeue', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType', default_value='::ns3::MacHeaderType::HEADER_TYPE_GENERIC')])
    
    cls.add_method('Dequeue', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType'), param('uint32_t', 'availableByte')])
    
    cls.add_method('Enqueue', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::MacHeaderType const &', 'hdrType'), param('ns3::GenericMacHeader const &', 'hdr')])
    
    cls.add_method('FragmentEnqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'fragment')])
    
    cls.add_method('GetCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFragmentsQueue', 
                   'std::list< ns3::Ptr< ns3::Packet const > > const', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetQueue', 
                   'ns3::Ptr< ns3::WimaxMacQueue >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSchedulingType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow *', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetType', 
                   'ns3::Cid::Type', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetTypeStr', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('HasPackets', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('HasPackets', 
                   'bool', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')], 
                   is_const=True)
    
    cls.add_method('SetServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3WimaxMacQueue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::WimaxMacQueue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint32_t', 'maxSize')])
    
    cls.add_method('CheckForFragmentation', 
                   'bool', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')])
    
    cls.add_method('Dequeue', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')])
    
    cls.add_method('Dequeue', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType'), param('uint32_t', 'availableByte')])
    
    cls.add_method('Enqueue', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::MacHeaderType const &', 'hdrType'), param('ns3::GenericMacHeader const &', 'hdr')])
    
    cls.add_method('GetFirstPacketHdrSize', 
                   'uint32_t', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')])
    
    cls.add_method('GetFirstPacketPayloadSize', 
                   'uint32_t', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')])
    
    cls.add_method('GetFirstPacketRequiredByte', 
                   'uint32_t', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')])
    
    cls.add_method('GetMaxSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNBytes', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPacketQueue', 
                   'std::deque< ns3::WimaxMacQueue::QueueElement > const &', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetQueueLengthWithMACOverhead', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsEmpty', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('IsEmpty', 
                   'bool', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')], 
                   is_const=True)
    
    cls.add_method('Peek', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::GenericMacHeader &', 'hdr')], 
                   is_const=True)
    
    cls.add_method('Peek', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::GenericMacHeader &', 'hdr'), param('ns3::Time &', 'timeStamp')], 
                   is_const=True)
    
    cls.add_method('Peek', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')], 
                   is_const=True)
    
    cls.add_method('Peek', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType'), param('ns3::Time &', 'timeStamp')], 
                   is_const=True)
    
    cls.add_method('SetFragmentNumber', 
                   'void', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')])
    
    cls.add_method('SetFragmentOffset', 
                   'void', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType'), param('uint32_t', 'offset')])
    
    cls.add_method('SetFragmentation', 
                   'void', 
                   [param('ns3::MacHeaderType::HeaderType', 'packetType')])
    
    cls.add_method('SetMaxSize', 
                   'void', 
                   [param('uint32_t', 'maxSize')])
    return

def register_Ns3WimaxMacToMacHeader_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::WimaxMacToMacHeader const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint32_t', 'len')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetSizeOfLen', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3WimaxPhy_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::WimaxPhy const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Attach', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxChannel >', 'channel')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::WimaxChannel >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetChannelBandwidth', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetChnlSrchTimeoutEvent', 
                   'ns3::EventId', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDataRate', 
                   'uint32_t', 
                   [param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True)
    
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrameDuration', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrameDuration', 
                   'ns3::Time', 
                   [param('uint8_t', 'frameDurationCode')], 
                   is_const=True)
    
    cls.add_method('GetFrameDurationCode', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrameDurationSec', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFrequency', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetGValue', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetMobility', 
                   'ns3::Ptr< ns3::Object >', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetNfft', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNrBytes', 
                   'uint64_t', 
                   [param('uint32_t', 'symbols'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True)
    
    cls.add_method('GetNrCarriers', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNrSymbols', 
                   'uint64_t', 
                   [param('uint32_t', 'size'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True)
    
    cls.add_method('GetPhyType', 
                   'ns3::WimaxPhy::PhyType', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetPsDuration', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPsPerFrame', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPsPerSymbol', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetReceiveCallback', 
                   'ns3::Callback< void, ns3::Ptr< ns3::PacketBurst const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRtg', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRxFrequency', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSamplingFactor', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSamplingFrequency', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetScanningFrequency', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetState', 
                   'ns3::WimaxPhy::PhyState', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSymbolDuration', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSymbolsPerFrame', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTransmissionTime', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True)
    
    cls.add_method('GetTtg', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTxFrequency', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsDuplex', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::SendParams *', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetChannelBandwidth', 
                   'void', 
                   [param('uint32_t', 'channelBandwidth')])
    
    cls.add_method('SetDataRates', 
                   'void', 
                   [])
    
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxNetDevice >', 'device')])
    
    cls.add_method('SetDuplex', 
                   'void', 
                   [param('uint64_t', 'rxFrequency'), param('uint64_t', 'txFrequency')])
    
    cls.add_method('SetFrameDuration', 
                   'void', 
                   [param('ns3::Time', 'frameDuration')])
    
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('uint32_t', 'frequency')])
    
    cls.add_method('SetMobility', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'mobility')], 
                   is_virtual=True)
    
    cls.add_method('SetNrCarriers', 
                   'void', 
                   [param('uint8_t', 'nrCarriers')])
    
    cls.add_method('SetPhyParameters', 
                   'void', 
                   [])
    
    cls.add_method('SetPsDuration', 
                   'void', 
                   [param('ns3::Time', 'psDuration')])
    
    cls.add_method('SetPsPerFrame', 
                   'void', 
                   [param('uint16_t', 'psPerFrame')])
    
    cls.add_method('SetPsPerSymbol', 
                   'void', 
                   [param('uint16_t', 'psPerSymbol')])
    
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::PacketBurst const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    
    cls.add_method('SetScanningCallback', 
                   'void', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetSimplex', 
                   'void', 
                   [param('uint64_t', 'frequency')])
    
    cls.add_method('SetState', 
                   'void', 
                   [param('ns3::WimaxPhy::PhyState', 'state')])
    
    cls.add_method('SetSymbolDuration', 
                   'void', 
                   [param('ns3::Time', 'symbolDuration')])
    
    cls.add_method('SetSymbolsPerFrame', 
                   'void', 
                   [param('uint32_t', 'symbolsPerFrame')])
    
    cls.add_method('StartScanning', 
                   'void', 
                   [param('uint64_t', 'frequency'), param('ns3::Time', 'timeout'), param('ns3::Callback< void, bool, unsigned long long, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    
    cls.add_method('DoAttach', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxChannel >', 'channel')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetDataRate', 
                   'uint32_t', 
                   [param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetFrameDuration', 
                   'ns3::Time', 
                   [param('uint8_t', 'frameDurationCode')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetFrameDurationCode', 
                   'uint8_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetGValue', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNfft', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNrBytes', 
                   'uint64_t', 
                   [param('uint32_t', 'symbols'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNrSymbols', 
                   'uint64_t', 
                   [param('uint32_t', 'size'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetRtg', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetSamplingFactor', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetSamplingFrequency', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetTransmissionTime', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetTtg', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoSetDataRates', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoSetPhyParameters', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3AttributeAccessor_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::AttributeAccessor const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Get', 
                   'bool', 
                   [param('ns3::ObjectBase const *', 'object'), param('ns3::AttributeValue &', 'attribute')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('HasGetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('HasSetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'object', transfer_ownership=False), param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeChecker_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::AttributeChecker const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Check', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Copy', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'source'), param('ns3::AttributeValue &', 'destination')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('CreateValidValue', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_const=True)
    
    cls.add_method('GetUnderlyingTypeInformation', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetValueTypeName', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('HasUnderlyingTypeInformation', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::AttributeValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3BSScheduler_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::BSScheduler const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')])
    
    cls.add_method('AddDownlinkBurst', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxConnection const >', 'connection'), param('uint8_t', 'diuc'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('ns3::Ptr< ns3::PacketBurst >', 'burst')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('CheckForFragmentation', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection >', 'connection'), param('int', 'availableSymbols'), param('ns3::WimaxPhy::ModulationType', 'modulationType')])
    
    cls.add_method('CreateUgsBurst', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint32_t', 'availableSymbols')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetBs', 
                   'ns3::Ptr< ns3::BaseStationNetDevice >', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetDownlinkBursts', 
                   'std::list< std::pair< ns3::OfdmDlMapIe *, ns3::Ptr< ns3::PacketBurst > > > *', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Schedule', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SelectConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetBs', 
                   'void', 
                   [param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')], 
                   is_virtual=True)
    return

def register_Ns3BSSchedulerRtps_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::BSSchedulerRtps const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')])
    
    cls.add_method('AddDownlinkBurst', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxConnection const >', 'connection'), param('uint8_t', 'diuc'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('ns3::Ptr< ns3::PacketBurst >', 'burst')], 
                   is_virtual=True)
    
    cls.add_method('BSSchedulerBEConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('BSSchedulerBasicConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('BSSchedulerBroadcastConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('BSSchedulerInitialRangingConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('BSSchedulerNRTPSConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('BSSchedulerPrimaryConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('BSSchedulerRTPSConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('BSSchedulerUGSConnection', 
                   'void', 
                   [param('uint32_t &', 'availableSymbols')])
    
    cls.add_method('CreateUgsBurst', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint32_t', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('GetDownlinkBursts', 
                   'std::list< std::pair< ns3::OfdmDlMapIe *, ns3::Ptr< ns3::PacketBurst > > > *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Schedule', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('SelectBEConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')])
    
    cls.add_method('SelectConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')], 
                   is_virtual=True)
    
    cls.add_method('SelectIRandBCConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')])
    
    cls.add_method('SelectMenagementConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')])
    
    cls.add_method('SelectNRTPSConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')])
    
    cls.add_method('SelectRTPSConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')])
    
    cls.add_method('SelectUGSConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')])
    return

def register_Ns3BSSchedulerSimple_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::BSSchedulerSimple const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::BaseStationNetDevice >', 'bs')])
    
    cls.add_method('AddDownlinkBurst', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxConnection const >', 'connection'), param('uint8_t', 'diuc'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('ns3::Ptr< ns3::PacketBurst >', 'burst')], 
                   is_virtual=True)
    
    cls.add_method('CreateUgsBurst', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [param('ns3::ServiceFlow *', 'serviceFlow'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint32_t', 'availableSymbols')], 
                   is_virtual=True)
    
    cls.add_method('GetDownlinkBursts', 
                   'std::list< std::pair< ns3::OfdmDlMapIe *, ns3::Ptr< ns3::PacketBurst > > > *', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Schedule', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('SelectConnection', 
                   'bool', 
                   [param('ns3::Ptr< ns3::WimaxConnection > &', 'connection')], 
                   is_virtual=True)
    return

def register_Ns3BandwidthRequestHeader_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::BandwidthRequestHeader const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetBr', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetEc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHcs', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHt', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetBr', 
                   'void', 
                   [param('uint32_t', 'br')])
    
    cls.add_method('SetCid', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('SetEc', 
                   'void', 
                   [param('uint8_t', 'ec')])
    
    cls.add_method('SetHcs', 
                   'void', 
                   [param('uint8_t', 'hcs')])
    
    cls.add_method('SetHt', 
                   'void', 
                   [param('uint8_t', 'HT')])
    
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    
    cls.add_method('check_hcs', 
                   'bool', 
                   [], 
                   is_const=True)
    return

def register_Ns3BsServiceFlowManager_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::BsServiceFlowManager const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Ptr< ns3::BaseStationNetDevice >', 'device')])
    
    cls.add_method('AddMulticastServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow', 'sf'), param('ns3::WimaxPhy::ModulationType', 'modulation')])
    
    cls.add_method('AddServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow *', 'serviceFlow')])
    
    cls.add_method('AllocateServiceFlows', 
                   'void', 
                   [param('ns3::DsaReq const &', 'dsaReq'), param('ns3::Cid', 'cid')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetDsaAckTimeoutEvent', 
                   'ns3::EventId', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow *', 
                   [param('uint32_t', 'sfid')], 
                   is_const=True)
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow *', 
                   [param('ns3::Cid', 'cid')], 
                   is_const=True)
    
    cls.add_method('GetServiceFlows', 
                   'std::vector< ns3::ServiceFlow * >', 
                   [param('ns3::ServiceFlow::SchedulingType', 'schedulingType')], 
                   is_const=True)
    
    cls.add_method('ProcessDsaAck', 
                   'void', 
                   [param('ns3::DsaAck const &', 'dsaAck'), param('ns3::Cid', 'cid')])
    
    cls.add_method('ProcessDsaReq', 
                   'ns3::ServiceFlow *', 
                   [param('ns3::DsaReq const &', 'dsaReq'), param('ns3::Cid', 'cid')])
    
    cls.add_method('SetMaxDsaRspRetries', 
                   'void', 
                   [param('uint8_t', 'maxDsaRspRetries')])
    return

def register_Ns3CallbackChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::CallbackChecker const &', 'arg0')])
    return

def register_Ns3CallbackImplBase_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::CallbackImplBase const &', 'arg0')])
    
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ptr< ns3::CallbackImplBase const >', 'other')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3CallbackValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::CallbackValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::CallbackBase const &', 'base')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::CallbackBase', 'base')])
    return

def register_Ns3Channel_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Channel const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3ConnectionManager_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::ConnectionManager const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddConnection', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxConnection >', 'connection'), param('ns3::Cid::Type', 'type')])
    
    cls.add_method('AllocateManagementConnections', 
                   'void', 
                   [param('ns3::SSRecord *', 'ssRecord'), param('ns3::RngRsp *', 'rngrsp')])
    
    cls.add_method('CreateConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [param('ns3::Cid::Type', 'type')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('GetConnections', 
                   'std::vector< ns3::Ptr< ns3::WimaxConnection > >', 
                   [param('ns3::Cid::Type', 'type')], 
                   is_const=True)
    
    cls.add_method('GetNPackets', 
                   'uint32_t', 
                   [param('ns3::Cid::Type', 'type'), param('ns3::ServiceFlow::SchedulingType', 'schedulingType')], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('HasPackets', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetCidFactory', 
                   'void', 
                   [param('ns3::CidFactory *', 'cidFactory')])
    return

def register_Ns3Dcd_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Dcd const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddDlBurstProfile', 
                   'void', 
                   [param('ns3::OfdmDlBurstProfile', 'dlBurstProfile')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetChannelEncodings', 
                   'ns3::OfdmDcdChannelEncodings', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConfigurationChangeCount', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDlBurstProfiles', 
                   'std::vector< ns3::OfdmDlBurstProfile >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNrDlBurstProfiles', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetChannelEncodings', 
                   'void', 
                   [param('ns3::OfdmDcdChannelEncodings', 'channelEncodings')])
    
    cls.add_method('SetConfigurationChangeCount', 
                   'void', 
                   [param('uint8_t', 'configurationChangeCount')])
    
    cls.add_method('SetNrDlBurstProfiles', 
                   'void', 
                   [param('uint8_t', 'nrDlBurstProfiles')])
    return

def register_Ns3DlMap_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::DlMap const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('AddDlMapElement', 
                   'void', 
                   [param('ns3::OfdmDlMapIe', 'dlMapElement')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetBaseStationId', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDcdCount', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDlMapElements', 
                   'std::list< ns3::OfdmDlMapIe >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetBaseStationId', 
                   'void', 
                   [param('ns3::Mac48Address', 'baseStationID')])
    
    cls.add_method('SetDcdCount', 
                   'void', 
                   [param('uint8_t', 'dcdCount')])
    return

def register_Ns3DsaAck_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::DsaAck const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetConfirmationCode', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTransactionId', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetConfirmationCode', 
                   'void', 
                   [param('uint16_t', 'confirmationCode')])
    
    cls.add_method('SetTransactionId', 
                   'void', 
                   [param('uint16_t', 'transactionId')])
    return

def register_Ns3DsaReq_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::DsaReq const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::ServiceFlow', 'sf')])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSfid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTransactionId', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetCid', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('SetServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow', 'sf')])
    
    cls.add_method('SetSfid', 
                   'void', 
                   [param('uint32_t', 'sfid')])
    
    cls.add_method('SetTransactionId', 
                   'void', 
                   [param('uint16_t', 'transactionId')])
    return

def register_Ns3DsaRsp_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::DsaRsp const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConfirmationCode', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetServiceFlow', 
                   'ns3::ServiceFlow', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSfid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTransactionId', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetCid', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('SetConfirmationCode', 
                   'void', 
                   [param('uint16_t', 'confirmationCode')])
    
    cls.add_method('SetServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow', 'sf')])
    
    cls.add_method('SetSfid', 
                   'void', 
                   [param('uint32_t', 'sfid')])
    
    cls.add_method('SetTransactionId', 
                   'void', 
                   [param('uint16_t', 'transactionId')])
    return

def register_Ns3EmptyAttributeValue_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::EmptyAttributeValue const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3EventImpl_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::EventImpl const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Cancel', 
                   'void', 
                   [])
    
    cls.add_method('Invoke', 
                   'void', 
                   [])
    
    cls.add_method('IsCancelled', 
                   'bool', 
                   [])
    
    cls.add_method('Notify', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    return

def register_Ns3FixedRssLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('SetRss', 
                   'void', 
                   [param('double', 'rss')])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3FragmentationSubheader_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::FragmentationSubheader const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetFc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetFsn', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetFc', 
                   'void', 
                   [param('uint8_t', 'fc')])
    
    cls.add_method('SetFsn', 
                   'void', 
                   [param('uint8_t', 'fsn')])
    return

def register_Ns3FriisPropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('SetLambda', 
                   'void', 
                   [param('double', 'frequency'), param('double', 'speed')])
    
    cls.add_method('SetLambda', 
                   'void', 
                   [param('double', 'lambda')])
    
    cls.add_method('SetSystemLoss', 
                   'void', 
                   [param('double', 'systemLoss')])
    
    cls.add_method('SetMinDistance', 
                   'void', 
                   [param('double', 'minDistance')])
    
    cls.add_method('GetMinDistance', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetLambda', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSystemLoss', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3GenericMacHeader_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::GenericMacHeader const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetCi', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetEc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetEks', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHcs', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetHt', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetLen', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetCi', 
                   'void', 
                   [param('uint8_t', 'ci')])
    
    cls.add_method('SetCid', 
                   'void', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('SetEc', 
                   'void', 
                   [param('uint8_t', 'ec')])
    
    cls.add_method('SetEks', 
                   'void', 
                   [param('uint8_t', 'eks')])
    
    cls.add_method('SetHcs', 
                   'void', 
                   [param('uint8_t', 'hcs')])
    
    cls.add_method('SetHt', 
                   'void', 
                   [param('uint8_t', 'HT')])
    
    cls.add_method('SetLen', 
                   'void', 
                   [param('uint16_t', 'len')])
    
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    
    cls.add_method('check_hcs', 
                   'bool', 
                   [], 
                   is_const=True)
    return

def register_Ns3GrantManagementSubheader_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::GrantManagementSubheader const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPbr', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPm', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetSi', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetPbr', 
                   'void', 
                   [param('uint16_t', 'pbr')])
    
    cls.add_method('SetPm', 
                   'void', 
                   [param('uint8_t', 'pm')])
    
    cls.add_method('SetSi', 
                   'void', 
                   [param('uint8_t', 'si')])
    return

def register_Ns3IpcsClassifier_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::IpcsClassifier const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Classify', 
                   'ns3::ServiceFlow *', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Ptr< ns3::ServiceFlowManager >', 'sfm'), param('ns3::ServiceFlow::Direction', 'dir')])
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3Ipv4AddressChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv4AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv4AddressValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv4AddressValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Ipv4Address const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Address const &', 'value')])
    return

def register_Ns3Ipv4MaskChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv4MaskChecker const &', 'arg0')])
    return

def register_Ns3Ipv4MaskValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv4MaskValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Mask const &', 'value')])
    return

def register_Ns3Ipv6AddressChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv6AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv6AddressValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv6AddressValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Ipv6Address const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Address const &', 'value')])
    return

def register_Ns3Ipv6PrefixChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv6PrefixChecker const &', 'arg0')])
    return

def register_Ns3Ipv6PrefixValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ipv6PrefixValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Prefix const &', 'value')])
    return

def register_Ns3LogDistancePropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('SetPathLossExponent', 
                   'void', 
                   [param('double', 'n')])
    
    cls.add_method('GetPathLossExponent', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetReference', 
                   'void', 
                   [param('double', 'referenceDistance'), param('double', 'referenceLoss')])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3Mac48AddressChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Mac48AddressChecker const &', 'arg0')])
    return

def register_Ns3Mac48AddressValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Mac48AddressValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Mac48Address const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Mac48Address const &', 'value')])
    return

def register_Ns3MatrixPropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('SetLoss', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b'), param('double', 'loss'), param('bool', 'symmetric', default_value='true')])
    
    cls.add_method('SetDefaultLoss', 
                   'void', 
                   [param('double', 'arg0')])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3NakagamiPropagationLossModel_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3NetDevice_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::NetDevice const &', 'arg0')])
    
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'multicastGroup')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3NixVector_methods(root_module, cls):
    cls.add_output_stream_operator()
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::NixVector const &', 'o')])
    
    cls.add_method('AddNeighborIndex', 
                   'void', 
                   [param('uint32_t', 'newBits'), param('uint32_t', 'numberOfBits')])
    
    cls.add_method('BitCount', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfNeighbors')], 
                   is_const=True)
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint32_t const *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('ExtractNeighborIndex', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfBits')])
    
    cls.add_method('GetRemainingBits', 
                   'uint32_t', 
                   [])
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint32_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3Node_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::Node const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('uint32_t', 'systemId')])
    
    cls.add_method('AddApplication', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::Application >', 'application')])
    
    cls.add_method('AddDevice', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')])
    
    cls.add_method('ChecksumEnabled', 
                   'bool', 
                   [], 
                   is_static=True)
    
    cls.add_method('GetApplication', 
                   'ns3::Ptr< ns3::Application >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    
    cls.add_method('GetId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNApplications', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('RegisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    
    cls.add_method('RegisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler'), param('uint16_t', 'protocolType'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'promiscuous', default_value='false')])
    
    cls.add_method('UnregisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    
    cls.add_method('UnregisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    
    cls.add_method('DoStart', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectFactoryChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::ObjectFactoryChecker const &', 'arg0')])
    return

def register_Ns3ObjectFactoryValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::ObjectFactoryValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::ObjectFactory const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::ObjectFactory', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::ObjectFactory const &', 'value')])
    return

def register_Ns3OutputStreamWrapper_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::OutputStreamWrapper const &', 'arg0')])
    
    cls.add_constructor([param('std::string', 'filename'), param('std::_Ios_Openmode', 'filemode')])
    
    cls.add_constructor([param('std::ostream *', 'os')])
    
    cls.add_method('GetStream', 
                   'std::ostream *', 
                   [])
    return

def register_Ns3Packet_methods(root_module, cls):
    cls.add_output_stream_operator()
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Packet const &', 'o')])
    
    cls.add_constructor([param('uint32_t', 'size')])
    
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size'), param('bool', 'magic')])
    
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    
    cls.add_method('AddByteTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header')])
    
    cls.add_method('AddPacketTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer')])
    
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [], 
                   is_const=True)
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    
    cls.add_method('CreateFragment', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    
    cls.add_method('EnablePrinting', 
                   'void', 
                   [], 
                   is_static=True)
    
    cls.add_method('FindFirstMatchingByteTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    
    cls.add_method('GetByteTagIterator', 
                   'ns3::ByteTagIterator', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNixVector', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPacketTagIterator', 
                   'ns3::PacketTagIterator', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('PeekData', 
                   'uint8_t const *', 
                   [], 
                   deprecated=True, is_const=True)
    
    cls.add_method('PeekHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')], 
                   is_const=True)
    
    cls.add_method('PeekPacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    
    cls.add_method('PeekTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    
    cls.add_method('PrintByteTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    
    cls.add_method('PrintPacketTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    
    cls.add_method('RemoveAllByteTags', 
                   'void', 
                   [])
    
    cls.add_method('RemoveAllPacketTags', 
                   'void', 
                   [])
    
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'size')])
    
    cls.add_method('RemoveHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')])
    
    cls.add_method('RemovePacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    
    cls.add_method('RemoveTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    
    cls.add_method('SetNixVector', 
                   'void', 
                   [param('ns3::Ptr< ns3::NixVector >', 'arg0')])
    return

def register_Ns3RandomVariableChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::RandomVariableChecker const &', 'arg0')])
    return

def register_Ns3RandomVariableValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::RandomVariableValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::RandomVariable const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::RandomVariable', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::RandomVariable const &', 'value')])
    return

def register_Ns3SimpleOfdmWimaxPhy_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SimpleOfdmWimaxPhy const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('char *', 'tracesPath')])
    
    cls.add_method('ActivateLoss', 
                   'void', 
                   [param('bool', 'loss')])
    
    cls.add_method('DoAttach', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxChannel >', 'channel')], 
                   is_virtual=True)
    
    cls.add_method('GetBandwidth', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNoiseFigure', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPhyType', 
                   'ns3::WimaxPhy::PhyType', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTxPower', 
                   'double', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('NotifyRxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('NotifyRxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('NotifyRxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('NotifyTxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('NotifyTxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('NotifyTxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint8_t', 'direction')])
    
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::SendParams *', 'params')], 
                   is_virtual=True)
    
    cls.add_method('SetBandwidth', 
                   'void', 
                   [param('uint32_t', 'BW')])
    
    cls.add_method('SetNoiseFigure', 
                   'void', 
                   [param('double', 'nf')])
    
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::PacketBurst >, ns3::Ptr< ns3::WimaxConnection >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    
    cls.add_method('SetSNRToBlockErrorRateTracesPath', 
                   'void', 
                   [param('char *', 'tracesPath')])
    
    cls.add_method('SetTxPower', 
                   'void', 
                   [param('double', 'txPower')])
    
    cls.add_method('StartReceive', 
                   'void', 
                   [param('uint32_t', 'burstSize'), param('bool', 'isFirstBlock'), param('uint64_t', 'frequency'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint8_t', 'direction'), param('double', 'rxPower'), param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoGetDataRate', 
                   'uint32_t', 
                   [param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetFrameDuration', 
                   'ns3::Time', 
                   [param('uint8_t', 'frameDurationCode')], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetFrameDurationCode', 
                   'uint8_t', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetGValue', 
                   'double', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNfft', 
                   'uint16_t', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNrBytes', 
                   'uint64_t', 
                   [param('uint32_t', 'symbols'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNrSymbols', 
                   'uint64_t', 
                   [param('uint32_t', 'size'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetRtg', 
                   'uint16_t', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetSamplingFactor', 
                   'double', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetSamplingFrequency', 
                   'double', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetTransmissionTime', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WimaxPhy::ModulationType', 'modulationType')], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetTtg', 
                   'uint16_t', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoSetDataRates', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoSetPhyParameters', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3TimeChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TimeChecker const &', 'arg0')])
    return

def register_Ns3TimeValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TimeValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Time const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Time const &', 'value')])
    return

def register_Ns3TypeIdChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TypeIdChecker const &', 'arg0')])
    return

def register_Ns3TypeIdValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::TypeIdValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::TypeId const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::TypeId const &', 'value')])
    return

def register_Ns3UintegerValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::UintegerValue const &', 'arg0')])
    
    cls.add_constructor([param('uint64_t const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('uint64_t const &', 'value')])
    return

def register_Ns3WimaxChannel_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::WimaxChannel const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_method('Attach', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxPhy >', 'phy')])
    
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_method('DoAttach', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxPhy >', 'phy')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNDevices', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3WimaxNetDevice_methods(root_module, cls):
    
    cls.add_static_attribute('m_direction', 'uint8_t', is_const=False)
    
    cls.add_static_attribute('m_frameStartTime', 'ns3::Time', is_const=False)
    
    cls.add_instance_attribute('m_traceRx', 'ns3::TracedCallback< ns3::Ptr< ns3::Packet const >, ns3::Mac48Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', is_const=False)
    
    cls.add_instance_attribute('m_traceTx', 'ns3::TracedCallback< ns3::Ptr< ns3::Packet const >, ns3::Mac48Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', is_const=False)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_method('SetTtg', 
                   'void', 
                   [param('uint16_t', 'ttg')])
    
    cls.add_method('GetTtg', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetRtg', 
                   'void', 
                   [param('uint16_t', 'rtg')])
    
    cls.add_method('GetRtg', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('Attach', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxChannel >', 'channel')])
    
    cls.add_method('SetPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxPhy >', 'phy')])
    
    cls.add_method('GetPhy', 
                   'ns3::Ptr< ns3::WimaxPhy >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxChannel >', 'wimaxChannel')])
    
    cls.add_method('GetChannel', 
                   'uint64_t', 
                   [param('uint8_t', 'index')], 
                   is_const=True)
    
    cls.add_method('SetNrFrames', 
                   'void', 
                   [param('uint32_t', 'nrFrames')])
    
    cls.add_method('GetNrFrames', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetMacAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    
    cls.add_method('GetMacAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetState', 
                   'void', 
                   [param('uint8_t', 'state')])
    
    cls.add_method('GetState', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetInitialRangingConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetBroadcastConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetCurrentDcd', 
                   'void', 
                   [param('ns3::Dcd', 'dcd')])
    
    cls.add_method('GetCurrentDcd', 
                   'ns3::Dcd', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetCurrentUcd', 
                   'void', 
                   [param('ns3::Ucd', 'ucd')])
    
    cls.add_method('GetCurrentUcd', 
                   'ns3::Ucd', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetConnectionManager', 
                   'ns3::Ptr< ns3::ConnectionManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetConnectionManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::ConnectionManager >', 'connectionManager')], 
                   is_virtual=True)
    
    cls.add_method('GetBurstProfileManager', 
                   'ns3::Ptr< ns3::BurstProfileManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetBurstProfileManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::BurstProfileManager >', 'burstProfileManager')])
    
    cls.add_method('GetBandwidthManager', 
                   'ns3::Ptr< ns3::BandwidthManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetBandwidthManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::BandwidthManager >', 'bandwidthManager')])
    
    cls.add_method('CreateDefaultConnections', 
                   'void', 
                   [])
    
    cls.add_method('Start', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [])
    
    cls.add_method('ForwardUp', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Mac48Address const &', 'source'), param('ns3::Mac48Address const &', 'dest')])
    
    cls.add_method('Enqueue', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::MacHeaderType const &', 'hdrType'), param('ns3::Ptr< ns3::WimaxConnection >', 'connection')], 
                   is_pure_virtual=True, is_virtual=True)
    
    cls.add_method('ForwardDown', 
                   'void', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'burst'), param('ns3::WimaxPhy::ModulationType', 'modulationType')])
    
    cls.add_method('SetName', 
                   'void', 
                   [param('std::string const', 'name')], 
                   is_virtual=True)
    
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_virtual=True)
    
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetPhyChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_virtual=True)
    
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_virtual=True)
    
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_virtual=True)
    
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('MakeMulticastAddress', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'multicastGroup')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_virtual=True)
    
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_virtual=True)
    
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    
    cls.add_method('GetPromiscReceiveCallback', 
                   'ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 
                   [])
    
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'multicastGroup')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('IsPromisc', 
                   'bool', 
                   [])
    
    cls.add_method('NotifyPromiscTrace', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    
    cls.add_method('DoSend', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Mac48Address const &', 'source'), param('ns3::Mac48Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoReceive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetChannel', 
                   'ns3::Ptr< ns3::WimaxChannel >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3AddressChecker_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::AddressChecker const &', 'arg0')])
    return

def register_Ns3AddressValue_methods(root_module, cls):
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::AddressValue const &', 'arg0')])
    
    cls.add_constructor([param('ns3::Address const &', 'value')])
    
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    
    cls.add_method('Get', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Address const &', 'value')])
    return

def register_Ns3BaseStationNetDevice_methods(root_module, cls):
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::Ptr< ns3::WimaxPhy >', 'phy')])
    
    cls.add_constructor([param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::Ptr< ns3::WimaxPhy >', 'phy'), param('ns3::Ptr< ns3::UplinkScheduler >', 'uplinkScheduler'), param('ns3::Ptr< ns3::BSScheduler >', 'bsScheduler')])
    
    cls.add_method('SetInitialRangingInterval', 
                   'void', 
                   [param('ns3::Time', 'initialRangInterval')])
    
    cls.add_method('InitBaseStationNetDevice', 
                   'void', 
                   [])
    
    cls.add_method('GetInitialRangingInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetDcdInterval', 
                   'void', 
                   [param('ns3::Time', 'dcdInterval')])
    
    cls.add_method('GetDcdInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetUcdInterval', 
                   'void', 
                   [param('ns3::Time', 'ucdInterval')])
    
    cls.add_method('GetUcdInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT8', 
                   'void', 
                   [param('ns3::Time', 'interval')])
    
    cls.add_method('GetIntervalT8', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetMaxRangingCorrectionRetries', 
                   'void', 
                   [param('uint8_t', 'maxRangCorrectionRetries')])
    
    cls.add_method('GetMaxRangingCorrectionRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetMaxInvitedRangRetries', 
                   'void', 
                   [param('uint8_t', 'maxInvitedRangRetries')])
    
    cls.add_method('GetMaxInvitedRangRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetRangReqOppSize', 
                   'void', 
                   [param('uint8_t', 'rangReqOppSize')])
    
    cls.add_method('GetRangReqOppSize', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetBwReqOppSize', 
                   'void', 
                   [param('uint8_t', 'bwReqOppSize')])
    
    cls.add_method('GetBwReqOppSize', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetNrDlSymbols', 
                   'void', 
                   [param('uint32_t', 'dlSymbols')])
    
    cls.add_method('GetNrDlSymbols', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetNrUlSymbols', 
                   'void', 
                   [param('uint32_t', 'ulSymbols')])
    
    cls.add_method('GetNrUlSymbols', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNrDcdSent', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetNrUcdSent', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetDlSubframeStartTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetUlSubframeStartTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetRangingOppNumber', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSSManager', 
                   'ns3::Ptr< ns3::SSManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetSSManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::SSManager >', 'ssManager')])
    
    cls.add_method('GetUplinkScheduler', 
                   'ns3::Ptr< ns3::UplinkScheduler >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetUplinkScheduler', 
                   'void', 
                   [param('ns3::Ptr< ns3::UplinkScheduler >', 'ulScheduler')])
    
    cls.add_method('GetLinkManager', 
                   'ns3::Ptr< ns3::BSLinkManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetBSScheduler', 
                   'void', 
                   [param('ns3::Ptr< ns3::BSScheduler >', 'bsSchedule')])
    
    cls.add_method('GetBSScheduler', 
                   'ns3::Ptr< ns3::BSScheduler >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetLinkManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::BSLinkManager >', 'linkManager')])
    
    cls.add_method('GetBsClassifier', 
                   'ns3::Ptr< ns3::IpcsClassifier >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetBsClassifier', 
                   'void', 
                   [param('ns3::Ptr< ns3::IpcsClassifier >', 'classifier')])
    
    cls.add_method('GetPsDuration', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetSymbolDuration', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('Start', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('Enqueue', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::MacHeaderType const &', 'hdrType'), param('ns3::Ptr< ns3::WimaxConnection >', 'connection')], 
                   is_virtual=True)
    
    cls.add_method('GetConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [param('ns3::Cid', 'cid')])
    
    cls.add_method('MarkUplinkAllocations', 
                   'void', 
                   [])
    
    cls.add_method('MarkRangingOppStart', 
                   'void', 
                   [param('ns3::Time', 'rangingOppStartTime')])
    
    cls.add_method('GetServiceFlowManager', 
                   'ns3::Ptr< ns3::BsServiceFlowManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetServiceFlowManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::BsServiceFlowManager >', 'arg0')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoSend', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Mac48Address const &', 'source'), param('ns3::Mac48Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoReceive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3SimpleOfdmWimaxChannel_methods(root_module, cls):
    
    cls.add_constructor([param('ns3::SimpleOfdmWimaxChannel const &', 'arg0')])
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::SimpleOfdmWimaxChannel::PropModel', 'propModel')])
    
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Time', 'BlockTime'), param('uint32_t', 'burstSize'), param('ns3::Ptr< ns3::WimaxPhy >', 'phy'), param('bool', 'isFirstBlock'), param('bool', 'isLastBlock'), param('uint64_t', 'frequency'), param('ns3::WimaxPhy::ModulationType', 'modulationType'), param('uint8_t', 'direction'), param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::PacketBurst >', 'burst')])
    
    cls.add_method('SetPropagationModel', 
                   'void', 
                   [param('ns3::SimpleOfdmWimaxChannel::PropModel', 'propModel')])
    
    cls.add_method('DoAttach', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxPhy >', 'phy')], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoGetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_const=True, visibility='private', is_virtual=True)
    
    cls.add_method('DoGetNDevices', 
                   'uint32_t', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3SubscriberStationNetDevice_methods(root_module, cls):
    
    cls.add_instance_attribute('m_linkManager', 'ns3::Ptr< ns3::SSLinkManager >', is_const=False)
    
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    
    cls.add_constructor([])
    
    cls.add_constructor([param('ns3::Ptr< ns3::Node >', 'arg0'), param('ns3::Ptr< ns3::WimaxPhy >', 'arg1')])
    
    cls.add_method('InitSubscriberStationNetDevice', 
                   'void', 
                   [])
    
    cls.add_method('SetLostDlMapInterval', 
                   'void', 
                   [param('ns3::Time', 'lostDlMapInterval')])
    
    cls.add_method('GetLostDlMapInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetLostUlMapInterval', 
                   'void', 
                   [param('ns3::Time', 'lostUlMapInterval')])
    
    cls.add_method('GetLostUlMapInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetMaxDcdInterval', 
                   'void', 
                   [param('ns3::Time', 'maxDcdInterval')])
    
    cls.add_method('GetMaxDcdInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetMaxUcdInterval', 
                   'void', 
                   [param('ns3::Time', 'maxUcdInterval')])
    
    cls.add_method('GetMaxUcdInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT1', 
                   'void', 
                   [param('ns3::Time', 'interval1')])
    
    cls.add_method('GetIntervalT1', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT2', 
                   'void', 
                   [param('ns3::Time', 'interval2')])
    
    cls.add_method('GetIntervalT2', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT3', 
                   'void', 
                   [param('ns3::Time', 'interval3')])
    
    cls.add_method('GetIntervalT3', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT7', 
                   'void', 
                   [param('ns3::Time', 'interval7')])
    
    cls.add_method('GetIntervalT7', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT12', 
                   'void', 
                   [param('ns3::Time', 'interval12')])
    
    cls.add_method('GetIntervalT12', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT20', 
                   'void', 
                   [param('ns3::Time', 'interval20')])
    
    cls.add_method('GetIntervalT20', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIntervalT21', 
                   'void', 
                   [param('ns3::Time', 'interval21')])
    
    cls.add_method('GetIntervalT21', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetMaxContentionRangingRetries', 
                   'void', 
                   [param('uint8_t', 'maxContentionRangingRetries')])
    
    cls.add_method('GetMaxContentionRangingRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetBasicConnection', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxConnection >', 'basicConnection')])
    
    cls.add_method('GetBasicConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetPrimaryConnection', 
                   'void', 
                   [param('ns3::Ptr< ns3::WimaxConnection >', 'primaryConnection')])
    
    cls.add_method('GetPrimaryConnection', 
                   'ns3::Ptr< ns3::WimaxConnection >', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetBasicCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetPrimaryCid', 
                   'ns3::Cid', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetModulationType', 
                   'void', 
                   [param('ns3::WimaxPhy::ModulationType', 'modulationType')])
    
    cls.add_method('GetModulationType', 
                   'ns3::WimaxPhy::ModulationType', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetAreManagementConnectionsAllocated', 
                   'void', 
                   [param('bool', 'areManagementConnectionsAllocated')])
    
    cls.add_method('GetAreManagementConnectionsAllocated', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetAreServiceFlowsAllocated', 
                   'void', 
                   [param('bool', 'areServiceFlowsAllocated')])
    
    cls.add_method('GetAreServiceFlowsAllocated', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetScheduler', 
                   'ns3::Ptr< ns3::SSScheduler >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::Ptr< ns3::SSScheduler >', 'ssScheduler')])
    
    cls.add_method('HasServiceFlows', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('Enqueue', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::MacHeaderType const &', 'hdrType'), param('ns3::Ptr< ns3::WimaxConnection >', 'connection')], 
                   is_virtual=True)
    
    cls.add_method('SendBurst', 
                   'void', 
                   [param('uint8_t', 'uiuc'), param('uint16_t', 'nrSymbols'), param('ns3::Ptr< ns3::WimaxConnection >', 'connection'), param('ns3::MacHeaderType::HeaderType', 'packetType', default_value='::ns3::MacHeaderType::HEADER_TYPE_GENERIC')])
    
    cls.add_method('Start', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_virtual=True)
    
    cls.add_method('AddServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow *', 'sf')])
    
    cls.add_method('AddServiceFlow', 
                   'void', 
                   [param('ns3::ServiceFlow', 'sf')])
    
    cls.add_method('SetTimer', 
                   'void', 
                   [param('ns3::EventId', 'eventId'), param('ns3::EventId &', 'event')])
    
    cls.add_method('IsRegistered', 
                   'bool', 
                   [], 
                   is_const=True)
    
    cls.add_method('GetTimeToAllocation', 
                   'ns3::Time', 
                   [param('ns3::Time', 'defferTime')])
    
    cls.add_method('GetIpcsClassifier', 
                   'ns3::Ptr< ns3::IpcsClassifier >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetIpcsPacketClassifier', 
                   'void', 
                   [param('ns3::Ptr< ns3::IpcsClassifier >', 'arg0')])
    
    cls.add_method('GetLinkManager', 
                   'ns3::Ptr< ns3::SSLinkManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetLinkManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::SSLinkManager >', 'arg0')])
    
    cls.add_method('GetServiceFlowManager', 
                   'ns3::Ptr< ns3::SsServiceFlowManager >', 
                   [], 
                   is_const=True)
    
    cls.add_method('SetServiceFlowManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::SsServiceFlowManager >', 'arg0')])
    
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoSend', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Mac48Address const &', 'source'), param('ns3::Mac48Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   visibility='private', is_virtual=True)
    
    cls.add_method('DoReceive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')], 
                   visibility='private', is_virtual=True)
    return

def register_functions(root_module):
    module = root_module
    
    module.add_function('CRC8Calculate', 
                        'uint8_t', 
                        [param('uint8_t const *', 'data'), param('int', 'length')])
    register_functions_ns3_FatalImpl(module.get_submodule('FatalImpl'), root_module)
    register_functions_ns3_internal(module.get_submodule('internal'), root_module)
    return

def register_functions_ns3_FatalImpl(module, root_module):
    return

def register_functions_ns3_internal(module, root_module):
    return

def main():
    out = FileCodeSink(sys.stdout)
    root_module = module_init()
    register_types(root_module)
    register_methods(root_module)
    register_functions(root_module)
    root_module.generate(out)

if __name__ == '__main__':
    main()

