/**
 */
package simplepdl;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Resource</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link simplepdl.Resource#getName <em>Name</em>}</li>
 *   <li>{@link simplepdl.Resource#getNbAvailableResources <em>Nb Available Resources</em>}</li>
 *   <li>{@link simplepdl.Resource#getNeeds <em>Needs</em>}</li>
 * </ul>
 *
 * @see simplepdl.SimplepdlPackage#getResource()
 * @model
 * @generated
 */
public interface Resource extends ProcessElement {
	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see simplepdl.SimplepdlPackage#getResource_Name()
	 * @model required="true"
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link simplepdl.Resource#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Nb Available Resources</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Nb Available Resources</em>' attribute.
	 * @see #setNbAvailableResources(int)
	 * @see simplepdl.SimplepdlPackage#getResource_NbAvailableResources()
	 * @model required="true"
	 * @generated
	 */
	int getNbAvailableResources();

	/**
	 * Sets the value of the '{@link simplepdl.Resource#getNbAvailableResources <em>Nb Available Resources</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Nb Available Resources</em>' attribute.
	 * @see #getNbAvailableResources()
	 * @generated
	 */
	void setNbAvailableResources(int value);

	/**
	 * Returns the value of the '<em><b>Needs</b></em>' reference list.
	 * The list contents are of type {@link simplepdl.Need}.
	 * It is bidirectional and its opposite is '{@link simplepdl.Need#getResource <em>Resource</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Needs</em>' reference list.
	 * @see simplepdl.SimplepdlPackage#getResource_Needs()
	 * @see simplepdl.Need#getResource
	 * @model opposite="resource"
	 * @generated
	 */
	EList<Need> getNeeds();

} // Resource
