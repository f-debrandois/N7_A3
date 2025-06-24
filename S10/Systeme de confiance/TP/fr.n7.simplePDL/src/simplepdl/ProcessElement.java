/**
 */
package simplepdl;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Process Element</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link simplepdl.ProcessElement#getProcess <em>Process</em>}</li>
 * </ul>
 *
 * @see simplepdl.SimplepdlPackage#getProcessElement()
 * @model abstract="true"
 * @generated
 */
public interface ProcessElement extends EObject {
	/**
	 * Returns the value of the '<em><b>Process</b></em>' container reference.
	 * It is bidirectional and its opposite is '{@link simplepdl.Process#getProcessElements <em>Process Elements</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Process</em>' container reference.
	 * @see #setProcess(simplepdl.Process)
	 * @see simplepdl.SimplepdlPackage#getProcessElement_Process()
	 * @see simplepdl.Process#getProcessElements
	 * @model opposite="processElements" required="true" transient="false"
	 * @generated
	 */
	simplepdl.Process getProcess();

	/**
	 * Sets the value of the '{@link simplepdl.ProcessElement#getProcess <em>Process</em>}' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Process</em>' container reference.
	 * @see #getProcess()
	 * @generated
	 */
	void setProcess(simplepdl.Process value);

} // ProcessElement
