/**
 */
package petriNet.impl;

import org.eclipse.emf.common.notify.Notification;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

import petriNet.Arc;
import petriNet.PetriNetPackage;
import petriNet.Place;
import petriNet.Transition;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Arc</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link petriNet.impl.ArcImpl#getWeight <em>Weight</em>}</li>
 *   <li>{@link petriNet.impl.ArcImpl#getSourcePlace <em>Source Place</em>}</li>
 *   <li>{@link petriNet.impl.ArcImpl#getTargetTransition <em>Target Transition</em>}</li>
 *   <li>{@link petriNet.impl.ArcImpl#getSourceTransition <em>Source Transition</em>}</li>
 *   <li>{@link petriNet.impl.ArcImpl#getTargetPlace <em>Target Place</em>}</li>
 * </ul>
 *
 * @generated
 */
public class ArcImpl extends MinimalEObjectImpl.Container implements Arc {
	/**
	 * The default value of the '{@link #getWeight() <em>Weight</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getWeight()
	 * @generated
	 * @ordered
	 */
	protected static final int WEIGHT_EDEFAULT = 0;

	/**
	 * The cached value of the '{@link #getWeight() <em>Weight</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getWeight()
	 * @generated
	 * @ordered
	 */
	protected int weight = WEIGHT_EDEFAULT;

	/**
	 * The cached value of the '{@link #getSourcePlace() <em>Source Place</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getSourcePlace()
	 * @generated
	 * @ordered
	 */
	protected Place sourcePlace;

	/**
	 * The cached value of the '{@link #getTargetTransition() <em>Target Transition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getTargetTransition()
	 * @generated
	 * @ordered
	 */
	protected Transition targetTransition;

	/**
	 * The cached value of the '{@link #getSourceTransition() <em>Source Transition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getSourceTransition()
	 * @generated
	 * @ordered
	 */
	protected Transition sourceTransition;

	/**
	 * The cached value of the '{@link #getTargetPlace() <em>Target Place</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getTargetPlace()
	 * @generated
	 * @ordered
	 */
	protected Place targetPlace;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ArcImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return PetriNetPackage.Literals.ARC;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public int getWeight() {
		return weight;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setWeight(int newWeight) {
		int oldWeight = weight;
		weight = newWeight;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, PetriNetPackage.ARC__WEIGHT, oldWeight, weight));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Place getSourcePlace() {
		if (sourcePlace != null && sourcePlace.eIsProxy()) {
			InternalEObject oldSourcePlace = (InternalEObject)sourcePlace;
			sourcePlace = (Place)eResolveProxy(oldSourcePlace);
			if (sourcePlace != oldSourcePlace) {
				if (eNotificationRequired())
					eNotify(new ENotificationImpl(this, Notification.RESOLVE, PetriNetPackage.ARC__SOURCE_PLACE, oldSourcePlace, sourcePlace));
			}
		}
		return sourcePlace;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Place basicGetSourcePlace() {
		return sourcePlace;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setSourcePlace(Place newSourcePlace) {
		Place oldSourcePlace = sourcePlace;
		sourcePlace = newSourcePlace;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, PetriNetPackage.ARC__SOURCE_PLACE, oldSourcePlace, sourcePlace));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Transition getTargetTransition() {
		if (targetTransition != null && targetTransition.eIsProxy()) {
			InternalEObject oldTargetTransition = (InternalEObject)targetTransition;
			targetTransition = (Transition)eResolveProxy(oldTargetTransition);
			if (targetTransition != oldTargetTransition) {
				if (eNotificationRequired())
					eNotify(new ENotificationImpl(this, Notification.RESOLVE, PetriNetPackage.ARC__TARGET_TRANSITION, oldTargetTransition, targetTransition));
			}
		}
		return targetTransition;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Transition basicGetTargetTransition() {
		return targetTransition;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setTargetTransition(Transition newTargetTransition) {
		Transition oldTargetTransition = targetTransition;
		targetTransition = newTargetTransition;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, PetriNetPackage.ARC__TARGET_TRANSITION, oldTargetTransition, targetTransition));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Transition getSourceTransition() {
		if (sourceTransition != null && sourceTransition.eIsProxy()) {
			InternalEObject oldSourceTransition = (InternalEObject)sourceTransition;
			sourceTransition = (Transition)eResolveProxy(oldSourceTransition);
			if (sourceTransition != oldSourceTransition) {
				if (eNotificationRequired())
					eNotify(new ENotificationImpl(this, Notification.RESOLVE, PetriNetPackage.ARC__SOURCE_TRANSITION, oldSourceTransition, sourceTransition));
			}
		}
		return sourceTransition;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Transition basicGetSourceTransition() {
		return sourceTransition;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setSourceTransition(Transition newSourceTransition) {
		Transition oldSourceTransition = sourceTransition;
		sourceTransition = newSourceTransition;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, PetriNetPackage.ARC__SOURCE_TRANSITION, oldSourceTransition, sourceTransition));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Place getTargetPlace() {
		if (targetPlace != null && targetPlace.eIsProxy()) {
			InternalEObject oldTargetPlace = (InternalEObject)targetPlace;
			targetPlace = (Place)eResolveProxy(oldTargetPlace);
			if (targetPlace != oldTargetPlace) {
				if (eNotificationRequired())
					eNotify(new ENotificationImpl(this, Notification.RESOLVE, PetriNetPackage.ARC__TARGET_PLACE, oldTargetPlace, targetPlace));
			}
		}
		return targetPlace;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Place basicGetTargetPlace() {
		return targetPlace;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setTargetPlace(Place newTargetPlace) {
		Place oldTargetPlace = targetPlace;
		targetPlace = newTargetPlace;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, PetriNetPackage.ARC__TARGET_PLACE, oldTargetPlace, targetPlace));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case PetriNetPackage.ARC__WEIGHT:
				return getWeight();
			case PetriNetPackage.ARC__SOURCE_PLACE:
				if (resolve) return getSourcePlace();
				return basicGetSourcePlace();
			case PetriNetPackage.ARC__TARGET_TRANSITION:
				if (resolve) return getTargetTransition();
				return basicGetTargetTransition();
			case PetriNetPackage.ARC__SOURCE_TRANSITION:
				if (resolve) return getSourceTransition();
				return basicGetSourceTransition();
			case PetriNetPackage.ARC__TARGET_PLACE:
				if (resolve) return getTargetPlace();
				return basicGetTargetPlace();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case PetriNetPackage.ARC__WEIGHT:
				setWeight((Integer)newValue);
				return;
			case PetriNetPackage.ARC__SOURCE_PLACE:
				setSourcePlace((Place)newValue);
				return;
			case PetriNetPackage.ARC__TARGET_TRANSITION:
				setTargetTransition((Transition)newValue);
				return;
			case PetriNetPackage.ARC__SOURCE_TRANSITION:
				setSourceTransition((Transition)newValue);
				return;
			case PetriNetPackage.ARC__TARGET_PLACE:
				setTargetPlace((Place)newValue);
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
			case PetriNetPackage.ARC__WEIGHT:
				setWeight(WEIGHT_EDEFAULT);
				return;
			case PetriNetPackage.ARC__SOURCE_PLACE:
				setSourcePlace((Place)null);
				return;
			case PetriNetPackage.ARC__TARGET_TRANSITION:
				setTargetTransition((Transition)null);
				return;
			case PetriNetPackage.ARC__SOURCE_TRANSITION:
				setSourceTransition((Transition)null);
				return;
			case PetriNetPackage.ARC__TARGET_PLACE:
				setTargetPlace((Place)null);
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
			case PetriNetPackage.ARC__WEIGHT:
				return weight != WEIGHT_EDEFAULT;
			case PetriNetPackage.ARC__SOURCE_PLACE:
				return sourcePlace != null;
			case PetriNetPackage.ARC__TARGET_TRANSITION:
				return targetTransition != null;
			case PetriNetPackage.ARC__SOURCE_TRANSITION:
				return sourceTransition != null;
			case PetriNetPackage.ARC__TARGET_PLACE:
				return targetPlace != null;
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy()) return super.toString();

		StringBuilder result = new StringBuilder(super.toString());
		result.append(" (weight: ");
		result.append(weight);
		result.append(')');
		return result.toString();
	}

} //ArcImpl
