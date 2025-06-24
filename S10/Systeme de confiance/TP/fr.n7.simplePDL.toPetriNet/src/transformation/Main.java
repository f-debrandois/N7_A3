package transformation;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;

import petriNet.PetriNet;
import simplepdl.Process;
import simplepdl.SimplepdlPackage;

public class Main {
    public static void main(String[] args) {
    	if (args.length < 2) {
            System.out.println("Usage: java Main <inputFilePath> <outputFilePath>");
            return;
        }
        String inputFilePath = args[0];
        String outputFilePath = args[1];

        // Charger le modèle SimplePDL
        Process process = loadProcessModel(inputFilePath);

        // Effectuer la transformation
        ProcessToPetriNetTransformer transformer = new ProcessToPetriNetTransformer();
        PetriNet petriNet = transformer.transform(process);

        // Sauvegarder le résultat
        transformer.savePetriNet(petriNet, outputFilePath);
    }
    
    private static Process loadProcessModel(String filePath) {
        // Initialisation
        SimplepdlPackage.eINSTANCE.eClass();
        ResourceSet resourceSet = new ResourceSetImpl();
        resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap()
            .put("xmi", new XMIResourceFactoryImpl());
        
        // Chargement
        URI fileURI = URI.createFileURI(filePath);
        Resource resource = resourceSet.getResource(fileURI, true);
        
        return (Process) resource.getContents().get(0);
    }
}