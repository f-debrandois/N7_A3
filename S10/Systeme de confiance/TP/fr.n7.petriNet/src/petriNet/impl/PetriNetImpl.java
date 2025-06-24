/**
 */
package petriNet.impl;

import java.util.Collection;

import org.eclipse.emf.common.notify.NotificationChain;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.InternalEList;

import petriNet.Arc;
import petriNet.PetriNet;
import petriNet.PetriNetPackage;
import petriNet.Place;
import petriNet.Transition;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Petri Net</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link petriNet.impl.PetriNetImpl#getPlaces <em>Places</em>}</li>
 *   <li>{@link petriNet.impl.PetriNetImpl#getTransitions <em>Transitions</em>}</li>
 *   <li>{@link petriNet.impl.PetriNetImpl#getArcs <em>Arcs</em>}</li>
 * </ul>
 *
 * @generated
 */
public class PetriNetImpl extends MinimalEObjectImpl.Container implements PetriNet {
	/**
	 * The cached value of the '{@link #getPlaces() <em>Places</em>}' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getPlaces()
	 * @generated
	 * @ordered
	 */
	protected EList<Place> places;

	/**
	 * The cached value of the '{@link #getTransitions() <em>Transitions</em>}' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getTransitions()
	 * @generated
	 * @ordered
	 */
	protected EList<Transition> transitions;

	/**
	 * The cached value of the '{@link #getArcs() <em>Arcs</em>}' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getArcs()
	 * @generated
	 * @ordered
	 */
	protected EList<Arc> arcs;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected PetriNetImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return PetriNetPackage.Literals.PETRI_NET;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<Place> getPlaces() {
		if (places == null) {
			places = new EObjectContainmentEList<Place>(Place.class, this, PetriNetPackage.PETRI_NET__PLACES);
		}
		return places;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<Transition> getTransitions() {
		if (transitions == null) {
			transitions = new EObjectContainmentEList<Transition>(Transition.class, this, PetriNetPackage.PETRI_NET__TRANSITIONS);
		}
		return transitions;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<Arc> getArcs() {
		if (arcs == null) {
			arcs = new EObjectContainmentEList<Arc>(Arc.class, this, PetriNetPackage.PETRI_NET__ARCS);
		}
		return arcs;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case PetriNetPackage.PETRI_NET__PLACES:
				return ((InternalEList<?>)getPlaces()).basicRemove(otherEnd, msgs);
			case PetriNetPackage.PETRI_NET__TRANSITIONS:
				return ((InternalEList<?>)getTransitions()).basicRemove(otherEnd, msgs);
			case PetriNetPackage.PETRI_NET__ARCS:
				return ((InternalEList<?>)getArcs()).basicRemove(otherEnd, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case PetriNetPackage.PETRI_NET__PLACES:
				return getPlaces();
			case PetriNetPackage.PETRI_NET__TRANSITIONS:
				return getTransitions();
			case PetriNetPackage.PETRI_NET__ARCS:
				return getArcs();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case PetriNetPackage.PETRI_NET__PLACES:
				getPlaces().clear();
				getPlaces().addAll((Collection<? extends Place>)newValue);
				return;
			case PetriNetPackage.PETRI_NET__TRANSITIONS:
				getTransitions().clear();
				getTransitions().addAll((Collection<? extends Transition>)newValue);
				return;
			case PetriNetPackage.PETRI_NET__ARCS:
				getArcs().clear();
				getArcs().addAll((Collection<? extends Arc>)newValue);
				return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
			case PetriNetPackage.PETRI_NET__PLACES:
				getPlaces().clear();
				return;
			case PetriNetPackage.PETRI_NET__TRANSITIONS:
				getTransitions().clear();
				return;
			case PetriNetPackage.PETRI_NET__ARCS:
				getArcs().clear();
				return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
			case PetriNetPackage.PETRI_NET__PLACES:
				return places != null && !places.isEmpty();
			case PetriNetPackage.PETRI_NET__TRANSITIONS:
				return transitions != null && !transitions.isEmpty();
			case PetriNetPackage.PETRI_NET__ARCS:
				return arcs != null && !arcs.isEmpty();
		}
		return super.eIsSet(featureID);
	}

	@Override
	public void setName(String string) {
		// TODO Auto-generated method stub
		
	}

} //PetriNetImpl
