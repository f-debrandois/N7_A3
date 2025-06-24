/**
 */
package simplepdl;

import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EEnum;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;

/**
 * <!-- begin-user-doc -->
 * The <b>Package</b> for the model.
 * It contains accessors for the meta objects to represent
 * <ul>
 *   <li>each class,</li>
 *   <li>each feature of each class,</li>
 *   <li>each operation of each class,</li>
 *   <li>each enum,</li>
 *   <li>and each data type</li>
 * </ul>
 * <!-- end-user-doc -->
 * @see simplepdl.SimplepdlFactory
 * @model kind="package"
 * @generated
 */
public interface SimplepdlPackage extends EPackage {
	/**
	 * The package name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNAME = "simplepdl";

	/**
	 * The package namespace URI.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_URI = "http://simplepdl";

	/**
	 * The package namespace name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_PREFIX = "simplepdl";

	/**
	 * The singleton instance of the package.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	SimplepdlPackage eINSTANCE = simplepdl.impl.SimplepdlPackageImpl.init();

	/**
	 * The meta object id for the '{@link simplepdl.impl.ProcessImpl <em>Process</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.impl.ProcessImpl
	 * @see simplepdl.impl.SimplepdlPackageImpl#getProcess()
	 * @generated
	 */
	int PROCESS = 0;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCESS__NAME = 0;

	/**
	 * The feature id for the '<em><b>Process Elements</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCESS__PROCESS_ELEMENTS = 1;

	/**
	 * The number of structural features of the '<em>Process</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCESS_FEATURE_COUNT = 2;

	/**
	 * The number of operations of the '<em>Process</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCESS_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link simplepdl.impl.ProcessElementImpl <em>Process Element</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.impl.ProcessElementImpl
	 * @see simplepdl.impl.SimplepdlPackageImpl#getProcessElement()
	 * @generated
	 */
	int PROCESS_ELEMENT = 3;

	/**
	 * The feature id for the '<em><b>Process</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCESS_ELEMENT__PROCESS = 0;

	/**
	 * The number of structural features of the '<em>Process Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCESS_ELEMENT_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Process Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCESS_ELEMENT_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link simplepdl.impl.WorkDefinitionImpl <em>Work Definition</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.impl.WorkDefinitionImpl
	 * @see simplepdl.impl.SimplepdlPackageImpl#getWorkDefinition()
	 * @generated
	 */
	int WORK_DEFINITION = 1;

	/**
	 * The feature id for the '<em><b>Process</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_DEFINITION__PROCESS = PROCESS_ELEMENT__PROCESS;

	/**
	 * The feature id for the '<em><b>Links To Predecessors</b></em>' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_DEFINITION__LINKS_TO_PREDECESSORS = PROCESS_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Links To Successors</b></em>' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_DEFINITION__LINKS_TO_SUCCESSORS = PROCESS_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_DEFINITION__NAME = PROCESS_ELEMENT_FEATURE_COUNT + 2;

	/**
	 * The feature id for the '<em><b>Need</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_DEFINITION__NEED = PROCESS_ELEMENT_FEATURE_COUNT + 3;

	/**
	 * The number of structural features of the '<em>Work Definition</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_DEFINITION_FEATURE_COUNT = PROCESS_ELEMENT_FEATURE_COUNT + 4;

	/**
	 * The number of operations of the '<em>Work Definition</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_DEFINITION_OPERATION_COUNT = PROCESS_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link simplepdl.impl.WorkSequenceImpl <em>Work Sequence</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.impl.WorkSequenceImpl
	 * @see simplepdl.impl.SimplepdlPackageImpl#getWorkSequence()
	 * @generated
	 */
	int WORK_SEQUENCE = 2;

	/**
	 * The feature id for the '<em><b>Process</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_SEQUENCE__PROCESS = PROCESS_ELEMENT__PROCESS;

	/**
	 * The feature id for the '<em><b>Link Type</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_SEQUENCE__LINK_TYPE = PROCESS_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Predecessor</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_SEQUENCE__PREDECESSOR = PROCESS_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The feature id for the '<em><b>Successor</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_SEQUENCE__SUCCESSOR = PROCESS_ELEMENT_FEATURE_COUNT + 2;

	/**
	 * The number of structural features of the '<em>Work Sequence</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_SEQUENCE_FEATURE_COUNT = PROCESS_ELEMENT_FEATURE_COUNT + 3;

	/**
	 * The number of operations of the '<em>Work Sequence</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORK_SEQUENCE_OPERATION_COUNT = PROCESS_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link simplepdl.impl.GuidanceImpl <em>Guidance</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.impl.GuidanceImpl
	 * @see simplepdl.impl.SimplepdlPackageImpl#getGuidance()
	 * @generated
	 */
	int GUIDANCE = 4;

	/**
	 * The feature id for the '<em><b>Process</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int GUIDANCE__PROCESS = PROCESS_ELEMENT__PROCESS;

	/**
	 * The feature id for the '<em><b>Text</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int GUIDANCE__TEXT = PROCESS_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Elements</b></em>' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int GUIDANCE__ELEMENTS = PROCESS_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The number of structural features of the '<em>Guidance</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int GUIDANCE_FEATURE_COUNT = PROCESS_ELEMENT_FEATURE_COUNT + 2;

	/**
	 * The number of operations of the '<em>Guidance</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int GUIDANCE_OPERATION_COUNT = PROCESS_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link simplepdl.impl.ResourceImpl <em>Resource</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.impl.ResourceImpl
	 * @see simplepdl.impl.SimplepdlPackageImpl#getResource()
	 * @generated
	 */
	int RESOURCE = 5;

	/**
	 * The feature id for the '<em><b>Process</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RESOURCE__PROCESS = PROCESS_ELEMENT__PROCESS;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RESOURCE__NAME = PROCESS_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Nb Available Resources</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RESOURCE__NB_AVAILABLE_RESOURCES = PROCESS_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The feature id for the '<em><b>Needs</b></em>' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RESOURCE__NEEDS = PROCESS_ELEMENT_FEATURE_COUNT + 2;

	/**
	 * The number of structural features of the '<em>Resource</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RESOURCE_FEATURE_COUNT = PROCESS_ELEMENT_FEATURE_COUNT + 3;

	/**
	 * The number of operations of the '<em>Resource</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RESOURCE_OPERATION_COUNT = PROCESS_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link simplepdl.impl.NeedImpl <em>Need</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.impl.NeedImpl
	 * @see simplepdl.impl.SimplepdlPackageImpl#getNeed()
	 * @generated
	 */
	int NEED = 6;

	/**
	 * The feature id for the '<em><b>Nb Resources</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NEED__NB_RESOURCES = 0;

	/**
	 * The feature id for the '<em><b>Resource</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NEED__RESOURCE = 1;

	/**
	 * The feature id for the '<em><b>Workdefinition</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NEED__WORKDEFINITION = 2;

	/**
	 * The number of structural features of the '<em>Need</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NEED_FEATURE_COUNT = 3;

	/**
	 * The number of operations of the '<em>Need</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NEED_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link simplepdl.WorkSequenceType <em>Work Sequence Type</em>}' enum.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see simplepdl.WorkSequenceType
	 * @see simplepdl.impl.SimplepdlPackageImpl#getWorkSequenceType()
	 * @generated
	 */
	int WORK_SEQUENCE_TYPE = 7;


	/**
	 * Returns the meta object for class '{@link simplepdl.Process <em>Process</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Process</em>'.
	 * @see simplepdl.Process
	 * @generated
	 */
	EClass getProcess();

	/**
	 * Returns the meta object for the attribute '{@link simplepdl.Process#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see simplepdl.Process#getName()
	 * @see #getProcess()
	 * @generated
	 */
	EAttribute getProcess_Name();

	/**
	 * Returns the meta object for the containment reference list '{@link simplepdl.Process#getProcessElements <em>Process Elements</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Process Elements</em>'.
	 * @see simplepdl.Process#getProcessElements()
	 * @see #getProcess()
	 * @generated
	 */
	EReference getProcess_ProcessElements();

	/**
	 * Returns the meta object for class '{@link simplepdl.WorkDefinition <em>Work Definition</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Work Definition</em>'.
	 * @see simplepdl.WorkDefinition
	 * @generated
	 */
	EClass getWorkDefinition();

	/**
	 * Returns the meta object for the reference list '{@link simplepdl.WorkDefinition#getLinksToPredecessors <em>Links To Predecessors</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference list '<em>Links To Predecessors</em>'.
	 * @see simplepdl.WorkDefinition#getLinksToPredecessors()
	 * @see #getWorkDefinition()
	 * @generated
	 */
	EReference getWorkDefinition_LinksToPredecessors();

	/**
	 * Returns the meta object for the reference list '{@link simplepdl.WorkDefinition#getLinksToSuccessors <em>Links To Successors</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference list '<em>Links To Successors</em>'.
	 * @see simplepdl.WorkDefinition#getLinksToSuccessors()
	 * @see #getWorkDefinition()
	 * @generated
	 */
	EReference getWorkDefinition_LinksToSuccessors();

	/**
	 * Returns the meta object for the attribute '{@link simplepdl.WorkDefinition#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see simplepdl.WorkDefinition#getName()
	 * @see #getWorkDefinition()
	 * @generated
	 */
	EAttribute getWorkDefinition_Name();

	/**
	 * Returns the meta object for the containment reference list '{@link simplepdl.WorkDefinition#getNeed <em>Need</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Need</em>'.
	 * @see simplepdl.WorkDefinition#getNeed()
	 * @see #getWorkDefinition()
	 * @generated
	 */
	EReference getWorkDefinition_Need();

	/**
	 * Returns the meta object for class '{@link simplepdl.WorkSequence <em>Work Sequence</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Work Sequence</em>'.
	 * @see simplepdl.WorkSequence
	 * @generated
	 */
	EClass getWorkSequence();

	/**
	 * Returns the meta object for the attribute '{@link simplepdl.WorkSequence#getLinkType <em>Link Type</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Link Type</em>'.
	 * @see simplepdl.WorkSequence#getLinkType()
	 * @see #getWorkSequence()
	 * @generated
	 */
	EAttribute getWorkSequence_LinkType();

	/**
	 * Returns the meta object for the reference '{@link simplepdl.WorkSequence#getPredecessor <em>Predecessor</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference '<em>Predecessor</em>'.
	 * @see simplepdl.WorkSequence#getPredecessor()
	 * @see #getWorkSequence()
	 * @generated
	 */
	EReference getWorkSequence_Predecessor();

	/**
	 * Returns the meta object for the reference '{@link simplepdl.WorkSequence#getSuccessor <em>Successor</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference '<em>Successor</em>'.
	 * @see simplepdl.WorkSequence#getSuccessor()
	 * @see #getWorkSequence()
	 * @generated
	 */
	EReference getWorkSequence_Successor();

	/**
	 * Returns the meta object for class '{@link simplepdl.ProcessElement <em>Process Element</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Process Element</em>'.
	 * @see simplepdl.ProcessElement
	 * @generated
	 */
	EClass getProcessElement();

	/**
	 * Returns the meta object for the container reference '{@link simplepdl.ProcessElement#getProcess <em>Process</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the container reference '<em>Process</em>'.
	 * @see simplepdl.ProcessElement#getProcess()
	 * @see #getProcessElement()
	 * @generated
	 */
	EReference getProcessElement_Process();

	/**
	 * Returns the meta object for class '{@link simplepdl.Guidance <em>Guidance</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Guidance</em>'.
	 * @see simplepdl.Guidance
	 * @generated
	 */
	EClass getGuidance();

	/**
	 * Returns the meta object for the attribute '{@link simplepdl.Guidance#getText <em>Text</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Text</em>'.
	 * @see simplepdl.Guidance#getText()
	 * @see #getGuidance()
	 * @generated
	 */
	EAttribute getGuidance_Text();

	/**
	 * Returns the meta object for the reference list '{@link simplepdl.Guidance#getElements <em>Elements</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference list '<em>Elements</em>'.
	 * @see simplepdl.Guidance#getElements()
	 * @see #getGuidance()
	 * @generated
	 */
	EReference getGuidance_Elements();

	/**
	 * Returns the meta object for class '{@link simplepdl.Resource <em>Resource</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Resource</em>'.
	 * @see simplepdl.Resource
	 * @generated
	 */
	EClass getResource();

	/**
	 * Returns the meta object for the attribute '{@link simplepdl.Resource#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see simplepdl.Resource#getName()
	 * @see #getResource()
	 * @generated
	 */
	EAttribute getResource_Name();

	/**
	 * Returns the meta object for the attribute '{@link simplepdl.Resource#getNbAvailableResources <em>Nb Available Resources</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Nb Available Resources</em>'.
	 * @see simplepdl.Resource#getNbAvailableResources()
	 * @see #getResource()
	 * @generated
	 */
	EAttribute getResource_NbAvailableResources();

	/**
	 * Returns the meta object for the reference list '{@link simplepdl.Resource#getNeeds <em>Needs</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference list '<em>Needs</em>'.
	 * @see simplepdl.Resource#getNeeds()
	 * @see #getResource()
	 * @generated
	 */
	EReference getResource_Needs();

	/**
	 * Returns the meta object for class '{@link simplepdl.Need <em>Need</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Need</em>'.
	 * @see simplepdl.Need
	 * @generated
	 */
	EClass getNeed();

	/**
	 * Returns the meta object for the attribute '{@link simplepdl.Need#getNbResources <em>Nb Resources</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Nb Resources</em>'.
	 * @see simplepdl.Need#getNbResources()
	 * @see #getNeed()
	 * @generated
	 */
	EAttribute getNeed_NbResources();

	/**
	 * Returns the meta object for the reference '{@link simplepdl.Need#getResource <em>Resource</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference '<em>Resource</em>'.
	 * @see simplepdl.Need#getResource()
	 * @see #getNeed()
	 * @generated
	 */
	EReference getNeed_Resource();

	/**
	 * Returns the meta object for the container reference '{@link simplepdl.Need#getWorkdefinition <em>Workdefinition</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the container reference '<em>Workdefinition</em>'.
	 * @see simplepdl.Need#getWorkdefinition()
	 * @see #getNeed()
	 * @generated
	 */
	EReference getNeed_Workdefinition();

	/**
	 * Returns the meta object for enum '{@link simplepdl.WorkSequenceType <em>Work Sequence Type</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for enum '<em>Work Sequence Type</em>'.
	 * @see simplepdl.WorkSequenceType
	 * @generated
	 */
	EEnum getWorkSequenceType();

	/**
	 * Returns the factory that creates the instances of the model.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the factory that creates the instances of the model.
	 * @generated
	 */
	SimplepdlFactory getSimplepdlFactory();

	/**
	 * <!-- begin-user-doc -->
	 * Defines literals for the meta objects that represent
	 * <ul>
	 *   <li>each class,</li>
	 *   <li>each feature of each class,</li>
	 *   <li>each operation of each class,</li>
	 *   <li>each enum,</li>
	 *   <li>and each data type</li>
	 * </ul>
	 * <!-- end-user-doc -->
	 * @generated
	 */
	interface Literals {
		/**
		 * The meta object literal for the '{@link simplepdl.impl.ProcessImpl <em>Process</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.impl.ProcessImpl
		 * @see simplepdl.impl.SimplepdlPackageImpl#getProcess()
		 * @generated
		 */
		EClass PROCESS = eINSTANCE.getProcess();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute PROCESS__NAME = eINSTANCE.getProcess_Name();

		/**
		 * The meta object literal for the '<em><b>Process Elements</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference PROCESS__PROCESS_ELEMENTS = eINSTANCE.getProcess_ProcessElements();

		/**
		 * The meta object literal for the '{@link simplepdl.impl.WorkDefinitionImpl <em>Work Definition</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.impl.WorkDefinitionImpl
		 * @see simplepdl.impl.SimplepdlPackageImpl#getWorkDefinition()
		 * @generated
		 */
		EClass WORK_DEFINITION = eINSTANCE.getWorkDefinition();

		/**
		 * The meta object literal for the '<em><b>Links To Predecessors</b></em>' reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference WORK_DEFINITION__LINKS_TO_PREDECESSORS = eINSTANCE.getWorkDefinition_LinksToPredecessors();

		/**
		 * The meta object literal for the '<em><b>Links To Successors</b></em>' reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference WORK_DEFINITION__LINKS_TO_SUCCESSORS = eINSTANCE.getWorkDefinition_LinksToSuccessors();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute WORK_DEFINITION__NAME = eINSTANCE.getWorkDefinition_Name();

		/**
		 * The meta object literal for the '<em><b>Need</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference WORK_DEFINITION__NEED = eINSTANCE.getWorkDefinition_Need();

		/**
		 * The meta object literal for the '{@link simplepdl.impl.WorkSequenceImpl <em>Work Sequence</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.impl.WorkSequenceImpl
		 * @see simplepdl.impl.SimplepdlPackageImpl#getWorkSequence()
		 * @generated
		 */
		EClass WORK_SEQUENCE = eINSTANCE.getWorkSequence();

		/**
		 * The meta object literal for the '<em><b>Link Type</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute WORK_SEQUENCE__LINK_TYPE = eINSTANCE.getWorkSequence_LinkType();

		/**
		 * The meta object literal for the '<em><b>Predecessor</b></em>' reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference WORK_SEQUENCE__PREDECESSOR = eINSTANCE.getWorkSequence_Predecessor();

		/**
		 * The meta object literal for the '<em><b>Successor</b></em>' reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference WORK_SEQUENCE__SUCCESSOR = eINSTANCE.getWorkSequence_Successor();

		/**
		 * The meta object literal for the '{@link simplepdl.impl.ProcessElementImpl <em>Process Element</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.impl.ProcessElementImpl
		 * @see simplepdl.impl.SimplepdlPackageImpl#getProcessElement()
		 * @generated
		 */
		EClass PROCESS_ELEMENT = eINSTANCE.getProcessElement();

		/**
		 * The meta object literal for the '<em><b>Process</b></em>' container reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference PROCESS_ELEMENT__PROCESS = eINSTANCE.getProcessElement_Process();

		/**
		 * The meta object literal for the '{@link simplepdl.impl.GuidanceImpl <em>Guidance</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.impl.GuidanceImpl
		 * @see simplepdl.impl.SimplepdlPackageImpl#getGuidance()
		 * @generated
		 */
		EClass GUIDANCE = eINSTANCE.getGuidance();

		/**
		 * The meta object literal for the '<em><b>Text</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute GUIDANCE__TEXT = eINSTANCE.getGuidance_Text();

		/**
		 * The meta object literal for the '<em><b>Elements</b></em>' reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference GUIDANCE__ELEMENTS = eINSTANCE.getGuidance_Elements();

		/**
		 * The meta object literal for the '{@link simplepdl.impl.ResourceImpl <em>Resource</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.impl.ResourceImpl
		 * @see simplepdl.impl.SimplepdlPackageImpl#getResource()
		 * @generated
		 */
		EClass RESOURCE = eINSTANCE.getResource();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute RESOURCE__NAME = eINSTANCE.getResource_Name();

		/**
		 * The meta object literal for the '<em><b>Nb Available Resources</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute RESOURCE__NB_AVAILABLE_RESOURCES = eINSTANCE.getResource_NbAvailableResources();

		/**
		 * The meta object literal for the '<em><b>Needs</b></em>' reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference RESOURCE__NEEDS = eINSTANCE.getResource_Needs();

		/**
		 * The meta object literal for the '{@link simplepdl.impl.NeedImpl <em>Need</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.impl.NeedImpl
		 * @see simplepdl.impl.SimplepdlPackageImpl#getNeed()
		 * @generated
		 */
		EClass NEED = eINSTANCE.getNeed();

		/**
		 * The meta object literal for the '<em><b>Nb Resources</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute NEED__NB_RESOURCES = eINSTANCE.getNeed_NbResources();

		/**
		 * The meta object literal for the '<em><b>Resource</b></em>' reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference NEED__RESOURCE = eINSTANCE.getNeed_Resource();

		/**
		 * The meta object literal for the '<em><b>Workdefinition</b></em>' container reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference NEED__WORKDEFINITION = eINSTANCE.getNeed_Workdefinition();

		/**
		 * The meta object literal for the '{@link simplepdl.WorkSequenceType <em>Work Sequence Type</em>}' enum.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see simplepdl.WorkSequenceType
		 * @see simplepdl.impl.SimplepdlPackageImpl#getWorkSequenceType()
		 * @generated
		 */
		EEnum WORK_SEQUENCE_TYPE = eINSTANCE.getWorkSequenceType();

	}

} //SimplepdlPackage
