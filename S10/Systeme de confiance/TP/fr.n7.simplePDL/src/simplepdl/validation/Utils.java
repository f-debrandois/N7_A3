package simplepdl.validation;

import java.util.Iterator;
import java.util.List;
import java.util.Set;

import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EObject;

/**
 * Classe utilitaire qui permet surtout de récupérer le nom d'un EObject pour
 * l'afficher de manière <i>user-friendly</i>.
 * 
 * @author Guillaume Dupont
 * @version 0.1
 */
public final class Utils {
	/**
	 * Classe utilitaire donc constructeur inaccessible.
	 */
	private Utils() {}
	
	/**
	 * Noms possibles pour un attribut qui représente un nom/une identification d'un
	 * EObject. Si l'EObject dont on veut le nom possède un attribut comme dans cet
	 * ensemble, alors on l'utilisera pour l'afficher (sinon on se contente de l'affichage
	 * par défaut offert par toString().
	 */
	private static final Set<String> NamingAttributes = Set.of(
			"name", "nom", "id"
		);

	/**
	 * "Devine" le nom d'un EObject en examinant ses attributs.
	 * Si l'objet a un attribut dont le nom fait partie des noms acceptés (de
	 * l'attribut static NamingAttributes) alors on utilise cette valeur, sinon on
	 * se contente de ce qui est retourné par toString().
	 * 
	 * Dans tous les cas, le nom affiché est le nom de l'object tel que deviné (ou 
	 * rien) suivi du retour de toString(), qui donne des informations intéressantes pour le
	 * débogage.
	 * 
	 * @param object objet dont on veut deviner le nom
	 * @return nom deviné de l'objet
	 */
	public static String guessName(EObject object) {
		List<EAttribute> attributes = object.eClass().getEAttributes();
		
		Iterator<EAttribute> it = attributes.iterator();
		String name = null;
		while (it.hasNext() && name == null) {
			EAttribute a = it.next();
			if (NamingAttributes.contains(a.getName())) {
				name = object.eGet(a).toString() + " [" + object.toString() + "]";
			}
		}
		
		if (name == null) {
			name = object.toString();
		}

		return name;
	}

}
