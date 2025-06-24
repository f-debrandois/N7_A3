package simplepdl.manip;

import java.io.IOException;
import java.util.Collections;
import java.util.Map;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;

import simplepdl.Process;
import simplepdl.WorkDefinition;
import simplepdl.WorkSequence;
import simplepdl.WorkSequenceType;
import simplepdl.SimplepdlFactory;
import simplepdl.SimplepdlPackage;

public class SimplePDLCreator {

	public static void main(String[] args) {
		
		// Charger le package SimplePDL afin de l'enregistrer dans le registre d'Eclipse.
		SimplepdlPackage packageInstance = SimplepdlPackage.eINSTANCE;
		
		// Enregistrer l'extension ".xmi" comme devant être ouverte à
		// l'aide d'un objet "XMIResourceFactoryImpl"
		Resource.Factory.Registry reg = Resource.Factory.Registry.INSTANCE;
		Map<String, Object> m = reg.getExtensionToFactoryMap();
		m.put("xmi", new XMIResourceFactoryImpl());
		
		// Créer un objet resourceSetImpl qui contiendra une ressource EMF (le modèle)
		ResourceSet resSet = new ResourceSetImpl();

		// Définir la ressource (le modèle)
		URI modelURI = URI.createURI("models/SimplePDLCreator_Created_Process.xmi");
		Resource resource = resSet.createResource(modelURI);
		
		// La fabrique pour fabriquer les éléments de SimplePDL
	    SimplepdlFactory myFactory = SimplepdlFactory.eINSTANCE;

		// Créer un élément Process
		Process process = myFactory.createProcess();
		process.setName("Mon premier processus");
		
		// Ajouter le Process dans le modèle
		resource.getContents().add(process);

		// Ajouter deux WorkDefinitions
	    WorkDefinition wd1 = myFactory.createWorkDefinition();
	    wd1.setName("Ma première WorkDefinition, quelle émotion");
	    
	    WorkDefinition wd2 = myFactory.createWorkDefinition();
	    wd2.setName("Ma deuxième WorkDefinition, toujours autant d'émotion");
	    
	    process.getProcessElements().add(wd1);
	    process.getProcessElements().add(wd2);
	    
		// Ajouter une WorkSequence entre les deux WorkDefinitions
	    WorkSequence seq = myFactory.createWorkSequence();
	    seq.setPredecessor(wd1);
	    seq.setSuccessor(wd2);
	    seq.setLinkType(WorkSequenceType.FINISH_TO_FINISH);
	    
	    process.getProcessElements().add(seq);
	    
		// Ajouter une deuxième WorkSequence entre les deux WorkDefinitions
	    WorkSequence seq2 = myFactory.createWorkSequence();
	    seq2.setPredecessor(wd1);
	    seq2.setSuccessor(wd2);
	    seq2.setLinkType(WorkSequenceType.START_TO_START);
	    
	    process.getProcessElements().add(seq2);
	    
		
		// Sauver la ressource
	    try {
	    	resource.save(Collections.EMPTY_MAP);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
