/**
 */
package petriNet;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Petri Net</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link petriNet.PetriNet#getPlaces <em>Places</em>}</li>
 *   <li>{@link petriNet.PetriNet#getTransitions <em>Transitions</em>}</li>
 *   <li>{@link petriNet.PetriNet#getArcs <em>Arcs</em>}</li>
 * </ul>
 *
 * @see petriNet.PetriNetPackage#getPetriNet()
 * @model
 * @generated
 */
public interface PetriNet extends EObject {
	/**
	 * Returns the value of the '<em><b>Places</b></em>' containment reference list.
	 * The list contents are of type {@link petriNet.Place}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Places</em>' containment reference list.
	 * @see petriNet.PetriNetPackage#getPetriNet_Places()
	 * @model containment="true"
	 * @generated
	 */
	EList<Place> getPlaces();

	/**
	 * Returns the value of the '<em><b>Transitions</b></em>' containment reference list.
	 * The list contents are of type {@link petriNet.Transition}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Transitions</em>' containment reference list.
	 * @see petriNet.PetriNetPackage#getPetriNet_Transitions()
	 * @model containment="true"
	 * @generated
	 */
	EList<Transition> getTransitions();

	/**
	 * Returns the value of the '<em><b>Arcs</b></em>' containment reference list.
	 * The list contents are of type {@link petriNet.Arc}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Arcs</em>' containment reference list.
	 * @see petriNet.PetriNetPackage#getPetriNet_Arcs()
	 * @model containment="true"
	 * @generated
	 */
	EList<Arc> getArcs();

	void setName(String string);

} // PetriNet
