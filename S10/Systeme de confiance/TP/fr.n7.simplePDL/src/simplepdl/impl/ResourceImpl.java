/**
 */
package simplepdl.impl;

import java.util.Collection;

import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.impl.ENotificationImpl;

import org.eclipse.emf.ecore.util.EObjectWithInverseResolvingEList;
import org.eclipse.emf.ecore.util.InternalEList;

import simplepdl.Need;
import simplepdl.Resource;
import simplepdl.SimplepdlPackage;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Resource</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link simplepdl.impl.ResourceImpl#getName <em>Name</em>}</li>
 *   <li>{@link simplepdl.impl.ResourceImpl#getNbAvailableResources <em>Nb Available Resources</em>}</li>
 *   <li>{@link simplepdl.impl.ResourceImpl#getNeeds <em>Needs</em>}</li>
 * </ul>
 *
 * @generated
 */
public class ResourceImpl extends ProcessElementImpl implements Resource {
	/**
	 * The default value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected static final String NAME_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected String name = NAME_EDEFAULT;

	/**
	 * The default value of the '{@link #getNbAvailableResources() <em>Nb Available Resources</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getNbAvailableResources()
	 * @generated
	 * @ordered
	 */
	protected static final int NB_AVAILABLE_RESOURCES_EDEFAULT = 0;

	/**
	 * The cached value of the '{@link #getNbAvailableResources() <em>Nb Available Resources</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getNbAvailableResources()
	 * @generated
	 * @ordered
	 */
	protected int nbAvailableResources = NB_AVAILABLE_RESOURCES_EDEFAULT;

	/**
	 * The cached value of the '{@link #getNeeds() <em>Needs</em>}' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getNeeds()
	 * @generated
	 * @ordered
	 */
	protected EList<Need> needs;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ResourceImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SimplepdlPackage.Literals.RESOURCE;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getName() {
		return name;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setName(String newName) {
		String oldName = name;
		name = newName;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, SimplepdlPackage.RESOURCE__NAME, oldName, name));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public int getNbAvailableResources() {
		return nbAvailableResources;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setNbAvailableResources(int newNbAvailableResources) {
		int oldNbAvailableResources = nbAvailableResources;
		nbAvailableResources = newNbAvailableResources;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, SimplepdlPackage.RESOURCE__NB_AVAILABLE_RESOURCES, oldNbAvailableResources, nbAvailableResources));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<Need> getNeeds() {
		if (needs == null) {
			needs = new EObjectWithInverseResolvingEList<Need>(Need.class, this, SimplepdlPackage.RESOURCE__NEEDS, SimplepdlPackage.NEED__RESOURCE);
		}
		return needs;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public NotificationChain eInverseAdd(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case SimplepdlPackage.RESOURCE__NEEDS:
				return ((InternalEList<InternalEObject>)(InternalEList<?>)getNeeds()).basicAdd(otherEnd, msgs);
		}
		return super.eInverseAdd(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case SimplepdlPackage.RESOURCE__NEEDS:
				return ((InternalEList<?>)getNeeds()).basicRemove(otherEnd, msgs);
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
			case SimplepdlPackage.RESOURCE__NAME:
				return getName();
			case SimplepdlPackage.RESOURCE__NB_AVAILABLE_RESOURCES:
				return getNbAvailableResources();
			case SimplepdlPackage.RESOURCE__NEEDS:
				return getNeeds();
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
			case SimplepdlPackage.RESOURCE__NAME:
				setName((String)newValue);
				return;
			case SimplepdlPackage.RESOURCE__NB_AVAILABLE_RESOURCES:
				setNbAvailableResources((Integer)newValue);
				return;
			case SimplepdlPackage.RESOURCE__NEEDS:
				getNeeds().clear();
				getNeeds().addAll((Collection<? extends Need>)newValue);
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
			case SimplepdlPackage.RESOURCE__NAME:
				setName(NAME_EDEFAULT);
				return;
			case SimplepdlPackage.RESOURCE__NB_AVAILABLE_RESOURCES:
				setNbAvailableResources(NB_AVAILABLE_RESOURCES_EDEFAULT);
				return;
			case SimplepdlPackage.RESOURCE__NEEDS:
				getNeeds().clear();
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
			case SimplepdlPackage.RESOURCE__NAME:
				return NAME_EDEFAULT == null ? name != null : !NAME_EDEFAULT.equals(name);
			case SimplepdlPackage.RESOURCE__NB_AVAILABLE_RESOURCES:
				return nbAvailableResources != NB_AVAILABLE_RESOURCES_EDEFAULT;
			case SimplepdlPackage.RESOURCE__NEEDS:
				return needs != null && !needs.isEmpty();
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
		result.append(" (name: ");
		result.append(name);
		result.append(", nbAvailableResources: ");
		result.append(nbAvailableResources);
		result.append(')');
		return result.toString();
	}

} //ResourceImpl
