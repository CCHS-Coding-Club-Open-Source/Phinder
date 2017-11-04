//
//  ViewController.swift
//  PhinderDataCollection
//
//  Created by Peter Maar on 11/4/17.
//  Copyright © 2017 alset333. All rights reserved.
//

import UIKit
import SystemConfiguration.CaptiveNetwork
import CoreMotion

class ViewController: UIViewController {

    @IBOutlet weak var dataLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
//        let hoursFromGMT = Double(TimeZone.current.secondsFromGMT()) / 3600.0
        
        var dataString = ""
        
        dataString += "Timezone: " + TimeZone.current.abbreviation()! + "\n"
        print("Timezone:", TimeZone.current.abbreviation()!)
        
        
        let date = Date()
        let calendar = Calendar.current
        
        dataString += "Calendar: " + String(describing: calendar) + "\n"
        print("Calendar: " + String(describing: calendar))
        
        
        
        let hour = calendar.component(.hour, from: date)
        let minutes = calendar.component(.minute, from: date)
        
        dataString += "Time: " + String(hour) + ":" + String(minutes) + "\n"
        print("Time: " + String(hour) + ":" + String(minutes))
        

        let prefLangCode = Locale.preferredLanguages[0] // Get the first preferred language
        dataString += "Region: " + prefLangCode + "\n"
        print("Region: " + prefLangCode)
        
        
//       print(Locale.isoLanguageCodes)
        
//       let identifiers : NSArray = NSLocale.availableLocaleIdentifiers as NSArray
//        let locale = NSLocale(localeIdentifier: "en_US")
//        let list = NSMutableString()
//        for identifier in identifiers {
//            let name = locale.displayName(forKey: NSLocale.Key.identifier, value: identifier)!
//            list.append("\(identifier)\t\(name)\n")
//        }
//        print(list)
        
        dataString += "SSID: " + currentSSIDs()[0] + "\n"
        print("SSID: " + currentSSIDs()[0])
        
        
        
        dataLabel.text = dataString
        
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func currentSSIDs() -> [String] {
        guard let interfaceNames = CNCopySupportedInterfaces() as? [String] else {
            return []
        }
        return interfaceNames.flatMap { name in
            guard let info = CNCopyCurrentNetworkInfo(name as CFString) as? [String:AnyObject] else {
                return nil
            }
            guard let ssid = info[kCNNetworkInfoKeySSID as String] as? String else {
                return nil
            }
            return ssid
        }
    }


}

