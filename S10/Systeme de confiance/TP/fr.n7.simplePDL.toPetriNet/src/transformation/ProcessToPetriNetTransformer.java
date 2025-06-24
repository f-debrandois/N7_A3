package transformation;

import java.util.HashMap;
import java.util.Map;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;

import petriNet.*;
import petriNet.impl.PetriNetFactoryImpl;
import simplepdl.*;
import simplepdl.Process;

public class ProcessToPetriNetTransformer {
    
    private final PetriNetFactory petriFactory = PetriNetFactoryImpl.init();
    private final Map<WorkDefinition, Transition> wdToTransition = new HashMap<>();
    
    public PetriNet transform(Process process) {
        PetriNet petriNet = petriFactory.createPetriNet();
        petriNet.setName(process.getName() + "_PetriNet");
        
        // Transformation des WorkDefinitions
        for (ProcessElement pe : process.getProcessElements()) {
            if (pe instanceof WorkDefinition) {
                transformWorkDefinition((WorkDefinition) pe, petriNet);
            }
        }
        
        // Transformation des WorkSequences
        for (ProcessElement pe : process.getProcessElements()) {
            if (pe instanceof WorkSequence) {
                transformWorkSequence((WorkSequence) pe, petriNet);
            }
        }
        
        return petriNet;
    }
    
    private void transformWorkDefinition(WorkDefinition wd, PetriNet petriNet) {
        // Création d'une place pour la WorkDefinition
        Place place = petriFactory.createPlace();
        place.setName("p_" + wd.getName());
        place.setTokens(0); // Initialement vide
        petriNet.getPlaces().add(place);
        
        // Création d'une transition pour la WorkDefinition
        Transition transition = petriFactory.createTransition();
        transition.setName("t_" + wd.getName());
        petriNet.getTransitions().add(transition);
        wdToTransition.put(wd, transition);
        
        // Arc d'entrée (place -> transition)
        Arc inArc = petriFactory.createArc();
        inArc.setSourcePlace(place);
        inArc.setTargetTransition(transition);
        inArc.setWeight(1);
        petriNet.getArcs().add(inArc);
    }
    
    private void transformWorkSequence(WorkSequence ws, PetriNet petriNet) {
        Transition sourceTransition = wdToTransition.get(ws.getPredecessor());
        Transition targetTransition = wdToTransition.get(ws.getSuccessor());
        
        if (sourceTransition != null && targetTransition != null) {
            // Création d'une place intermédiaire
            Place intermediatePlace = petriFactory.createPlace();
            intermediatePlace.setName("p_" + ws.getPredecessor().getName() + "_to_" + ws.getSuccessor().getName());
            petriNet.getPlaces().add(intermediatePlace);
            
            // Arc de la transition source vers la place intermédiaire
            Arc outArc = petriFactory.createArc();
            outArc.setSourceTransition(sourceTransition);
            outArc.setTargetPlace(intermediatePlace);
            outArc.setWeight(1);
            petriNet.getArcs().add(outArc);
            
            // Arc de la place intermédiaire vers la transition target
            Arc inArc = petriFactory.createArc();
            inArc.setSourcePlace(intermediatePlace);
            inArc.setTargetTransition(targetTransition);
            inArc.setWeight(1);
            petriNet.getArcs().add(inArc);
        }
    }
    
    public void savePetriNet(PetriNet petriNet, String filePath) {
        // Enregistrement du réseau de Petri
        ResourceSet resourceSet = new ResourceSetImpl();
        resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap()
            .put("xmi", new XMIResourceFactoryImpl());
        
        URI fileURI = URI.createFileURI(filePath);
        Resource resource = resourceSet.createResource(fileURI);
        resource.getContents().add(petriNet);
        
        try {
            resource.save(null);
            System.out.println("PetriNet saved to: " + filePath);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}