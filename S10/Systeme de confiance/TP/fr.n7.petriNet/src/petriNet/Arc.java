/**
 */
package petriNet;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Arc</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link petriNet.Arc#getWeight <em>Weight</em>}</li>
 *   <li>{@link petriNet.Arc#getSourcePlace <em>Source Place</em>}</li>
 *   <li>{@link petriNet.Arc#getTargetTransition <em>Target Transition</em>}</li>
 *   <li>{@link petriNet.Arc#getSourceTransition <em>Source Transition</em>}</li>
 *   <li>{@link petriNet.Arc#getTargetPlace <em>Target Place</em>}</li>
 * </ul>
 *
 * @see petriNet.PetriNetPackage#getArc()
 * @model
 * @generated
 */
public interface Arc extends EObject {
	/**
	 * Returns the value of the '<em><b>Weight</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Weight</em>' attribute.
	 * @see #setWeight(int)
	 * @see petriNet.PetriNetPackage#getArc_Weight()
	 * @model required="true"
	 * @generated
	 */
	int getWeight();

	/**
	 * Sets the value of the '{@link petriNet.Arc#getWeight <em>Weight</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Weight</em>' attribute.
	 * @see #getWeight()
	 * @generated
	 */
	void setWeight(int value);

	/**
	 * Returns the value of the '<em><b>Source Place</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Source Place</em>' reference.
	 * @see #setSourcePlace(Place)
	 * @see petriNet.PetriNetPackage#getArc_SourcePlace()
	 * @model
	 * @generated
	 */
	Place getSourcePlace();

	/**
	 * Sets the value of the '{@link petriNet.Arc#getSourcePlace <em>Source Place</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Source Place</em>' reference.
	 * @see #getSourcePlace()
	 * @generated
	 */
	void setSourcePlace(Place value);

	/**
	 * Returns the value of the '<em><b>Target Transition</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Target Transition</em>' reference.
	 * @see #setTargetTransition(Transition)
	 * @see petriNet.PetriNetPackage#getArc_TargetTransition()
	 * @model
	 * @generated
	 */
	Transition getTargetTransition();

	/**
	 * Sets the value of the '{@link petriNet.Arc#getTargetTransition <em>Target Transition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Target Transition</em>' reference.
	 * @see #getTargetTransition()
	 * @generated
	 */
	void setTargetTransition(Transition value);

	/**
	 * Returns the value of the '<em><b>Source Transition</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Source Transition</em>' reference.
	 * @see #setSourceTransition(Transition)
	 * @see petriNet.PetriNetPackage#getArc_SourceTransition()
	 * @model
	 * @generated
	 */
	Transition getSourceTransition();

	/**
	 * Sets the value of the '{@link petriNet.Arc#getSourceTransition <em>Source Transition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Source Transition</em>' reference.
	 * @see #getSourceTransition()
	 * @generated
	 */
	void setSourceTransition(Transition value);

	/**
	 * Returns the value of the '<em><b>Target Place</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Target Place</em>' reference.
	 * @see #setTargetPlace(Place)
	 * @see petriNet.PetriNetPackage#getArc_TargetPlace()
	 * @model
	 * @generated
	 */
	Place getTargetPlace();

	/**
	 * Sets the value of the '{@link petriNet.Arc#getTargetPlace <em>Target Place</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Target Place</em>' reference.
	 * @see #getTargetPlace()
	 * @generated
	 */
	void setTargetPlace(Place value);

} // Arc
